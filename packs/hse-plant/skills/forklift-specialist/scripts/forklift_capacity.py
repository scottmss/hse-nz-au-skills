#!/usr/bin/env python3
"""forklift_capacity.py — deterministic forklift load-centre capacity de-rating.

A forklift's rated capacity is quoted at a RATED LOAD CENTRE (commonly 500 mm from the fork
face). As the load's centre of gravity moves further out, the safe capacity FALLS. This tool
de-rates the rated capacity for the actual load centre and checks a load against it.

Two methods:
  * conservative (DEFAULT) — inverse-proportion: capacity ~ rated_capacity * D / d.
    Needs no truck-specific geometry; it UNDERSTATES capacity slightly (safe side).
  * exact — load-moment about the front axle, if you supply --fulcrum-offset (the horizontal
    distance from the fork face to the front-axle centreline, from the truck manual):
    capacity = rated_capacity * (D + a) / (d + a).

Capacity is never reported above the data-plate rating (closer-than-rated loads are not an
excuse to overload). Lift height and attachments ALSO reduce capacity and require the
manufacturer's capacity chart / attachment data plate — this tool flags that, it cannot
compute it. The DATA PLATE GOVERNS.

This is a planning aid, NOT a substitute for the forklift data plate, capacity chart, or a
competent person. Confirm every figure before lifting.

Pure standard library. No network, no file writes, no side effects. Safe to read and run.

Usage:
    # 2000 kg @ 500 mm rated; actual load centre 900 mm; load 1200 kg
    python3 forklift_capacity.py --rated-capacity 2000 --load-centre 900 --load-weight 1200

    # exact load-moment method with a known fork-face-to-front-axle distance of 400 mm
    python3 forklift_capacity.py --rated-capacity 2000 --load-centre 900 --load-weight 1200 \
        --fulcrum-offset 400

    # non-standard rated load centre, machine-readable, self-test
    python3 forklift_capacity.py --rated-capacity 2500 --rated-load-centre 600 --load-centre 1000 \
        --load-weight 1500 --json
    python3 forklift_capacity.py --selftest

Exit codes: 0 = success / tests passed, 1 = test failure, 2 = bad input.
"""
from __future__ import annotations

import argparse
import json
import sys

DEFAULT_RATED_LOAD_CENTRE = 500.0   # mm from the fork face (common standard)


def derate(rated_capacity: float, load_centre: float, rated_load_centre: float = DEFAULT_RATED_LOAD_CENTRE,
           fulcrum_offset: float | None = None) -> dict:
    """De-rate capacity for an actual load centre. fulcrum_offset (mm) -> exact load-moment method."""
    if rated_capacity <= 0:
        raise ValueError(f"--rated-capacity must be positive, got {rated_capacity!r}")
    if rated_load_centre <= 0:
        raise ValueError(f"--rated-load-centre must be positive, got {rated_load_centre!r}")
    if load_centre <= 0:
        raise ValueError(f"--load-centre must be positive, got {load_centre!r}")
    if fulcrum_offset is not None and fulcrum_offset < 0:
        raise ValueError(f"--fulcrum-offset must be >= 0, got {fulcrum_offset!r}")

    d_rated, d_act = rated_load_centre, load_centre
    if fulcrum_offset is not None:
        a = fulcrum_offset
        capacity = rated_capacity * (d_rated + a) / (d_act + a)
        method = "exact (load-moment about front axle)"
    else:
        capacity = rated_capacity * d_rated / d_act
        method = "conservative (inverse-proportion)"

    # Never rate above the data-plate capacity.
    capped = capacity > rated_capacity
    if capped:
        capacity = rated_capacity

    return {
        "method": method,
        "rated_capacity": rated_capacity,
        "rated_load_centre": d_rated,
        "load_centre": d_act,
        "fulcrum_offset": fulcrum_offset,
        "derated_capacity": round(capacity, 1),
        "capped_at_rated": capped,
    }


def assess(rated_capacity: float, load_centre: float, load_weight: float,
           rated_load_centre: float = DEFAULT_RATED_LOAD_CENTRE,
           fulcrum_offset: float | None = None) -> dict:
    if load_weight <= 0:
        raise ValueError(f"--load-weight must be positive, got {load_weight!r}")
    d = derate(rated_capacity, load_centre, rated_load_centre, fulcrum_offset)
    cap = d["derated_capacity"]
    utilisation = load_weight / cap * 100.0 if cap else float("inf")
    within = load_weight <= cap + 1e-9
    margin = cap - load_weight

    warnings = []
    if not within:
        warnings.append(f"OVER CAPACITY: load {load_weight:.0f} kg exceeds the de-rated capacity "
                        f"{cap:.0f} kg at a {load_centre:.0f} mm load centre ({utilisation:.0f}%). "
                        "DO NOT lift.")
    if d["fulcrum_offset"] is None:
        warnings.append("Conservative method (no fulcrum offset). For the exact load-moment value "
                        "supply --fulcrum-offset from the truck manual; the data-plate chart governs.")
    if d["capped_at_rated"]:
        warnings.append("Load centre is closer than rated; capacity capped at the data-plate rating "
                        "(never rate a forklift above its nameplate).")
    warnings.append("Lift HEIGHT and any ATTACHMENT further reduce capacity and shift the centre of "
                    "gravity — use the manufacturer's capacity chart / attachment data plate. Keep the "
                    "combined CoG inside the stability triangle.")

    return {**d, "load_weight": load_weight, "utilisation_pct": round(utilisation, 1),
            "within_capacity": within, "margin": round(margin, 1), "warnings": warnings}


def _fmt(r: dict) -> str:
    verdict = "WITHIN CAPACITY" if r["within_capacity"] else "OVER CAPACITY"
    lines = [
        "Forklift capacity check:",
        f"  Rated         : {r['rated_capacity']:.0f} kg @ {r['rated_load_centre']:.0f} mm load centre",
        f"  Actual load   : {r['load_weight']:.0f} kg @ {r['load_centre']:.0f} mm load centre",
        f"  Method        : {r['method']}",
        f"  De-rated cap. : {r['derated_capacity']:.0f} kg",
        f"  Utilisation   : {r['utilisation_pct']:.0f}%  (margin {r['margin']:.0f} kg)",
        f"  Verdict       : {verdict}",
    ]
    if r["warnings"]:
        lines.append("  Notes:")
        lines.extend(f"    - {w}" for w in r["warnings"])
    return "\n".join(lines)


def _approx(a: float, b: float, tol: float = 1.0) -> bool:
    return abs(a - b) <= tol


def _selftest() -> int:
    failures = 0

    def check(desc, got, exp, tol=1.0):
        nonlocal failures
        ok = (got == exp) if isinstance(exp, bool) else _approx(got, exp, tol)
        print(f"  [{'PASS' if ok else 'FAIL'}] {desc}: got {got}, expected {exp}")
        if not ok:
            failures += 1

    # Conservative: 2000 * 500/1000 = 1000 kg.
    r = assess(2000, 1000, 900)
    check("conservative de-rated capacity", r["derated_capacity"], 1000.0)
    check("within at 900 kg", r["within_capacity"], True)
    check("utilisation 90%", r["utilisation_pct"], 90.0)

    # Over capacity: load 1200 vs 1000.
    r = assess(2000, 1000, 1200)
    check("over capacity flag", r["within_capacity"], False)
    ok = any("OVER CAPACITY" in w for w in r["warnings"])
    print(f"  [{'PASS' if ok else 'FAIL'}] over-capacity warning present")
    if not ok:
        failures += 1

    # Exact load-moment: 2000 * (500+400)/(1000+400) = 1285.7 kg.
    r = assess(2000, 1000, 900, fulcrum_offset=400)
    check("exact de-rated capacity", r["derated_capacity"], 1285.7, tol=1.0)

    # Closer-than-rated load centre -> capped at rated 2000 (not 4000).
    r = assess(2000, 250, 1500)
    check("capped at rated", r["derated_capacity"], 2000.0)
    check("capped flag", r["capped_at_rated"], True)

    # Non-standard rated load centre: 2500 * 600/1000 = 1500.
    r = assess(2500, 1000, 1400, rated_load_centre=600)
    check("non-standard rated centre", r["derated_capacity"], 1500.0)

    # Bad inputs rejected.
    for bad in [
        dict(rated_capacity=0, load_centre=900, load_weight=500),
        dict(rated_capacity=2000, load_centre=0, load_weight=500),
        dict(rated_capacity=2000, load_centre=900, load_weight=0),
        dict(rated_capacity=2000, load_centre=900, load_weight=500, rated_load_centre=0),
        dict(rated_capacity=2000, load_centre=900, load_weight=500, fulcrum_offset=-5),
    ]:
        try:
            assess(**bad)
        except ValueError:
            print(f"  [PASS] rejected bad input {bad}")
        else:
            print(f"  [FAIL] accepted bad input {bad}")
            failures += 1

    print(f"\n{'ALL TESTS PASSED' if failures == 0 else f'{failures} TEST(S) FAILED'}")
    return 0 if failures == 0 else 1


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        description="Deterministic forklift load-centre capacity de-rating.")
    p.add_argument("--rated-capacity", type=float, help="data-plate rated capacity, kg")
    p.add_argument("--rated-load-centre", type=float, default=DEFAULT_RATED_LOAD_CENTRE,
                   help=f"rated load centre, mm from fork face (default {DEFAULT_RATED_LOAD_CENTRE:.0f})")
    p.add_argument("--load-centre", type=float, help="actual load centre, mm from fork face")
    p.add_argument("--load-weight", type=float, help="actual load weight, kg")
    p.add_argument("--fulcrum-offset", type=float,
                   help="fork-face to front-axle distance, mm (truck manual) -> exact load-moment method")
    p.add_argument("--json", action="store_true", help="machine-readable output")
    p.add_argument("--selftest", action="store_true", help="run built-in tests and exit")
    args = p.parse_args(argv)

    if args.selftest:
        return _selftest()

    if args.rated_capacity is None or args.load_centre is None or args.load_weight is None:
        p.error("--rated-capacity, --load-centre and --load-weight are required (or use --selftest)")

    try:
        r = assess(args.rated_capacity, args.load_centre, args.load_weight,
                   args.rated_load_centre, args.fulcrum_offset)
    except ValueError as e:
        p.error(str(e))

    if args.json:
        print(json.dumps(r, indent=2))
        return 0

    print(_fmt(r))
    print("\nPlanning aid only — the forklift data plate / capacity chart and a competent person govern.")
    print("Not legal advice; not engineering certification.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
