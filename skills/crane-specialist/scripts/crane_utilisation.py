#!/usr/bin/env python3
"""crane_utilisation.py — deterministic gross-load build-up and crane chart utilisation.

Builds up the GROSS load (bare load + rigging + hook block + ancillaries), compares it to
the crane's RATED CAPACITY at the working radius/configuration, and reports the utilisation
percentage, whether it is within capacity, and whether it should be treated as a CRITICAL
lift. Supports a de-rating factor for tandem/multi-crane or condition de-rating.

The rated capacity is YOUR figure, read from the actual crane load chart at the actual
radius and configuration — this tool does the arithmetic, it does NOT know any crane's chart.
The chart always governs.

This is a planning aid, NOT a substitute for the crane load chart, the RCI/LMI, or a
competent crane person / lift planner. Confirm every figure before lifting.

Pure standard library. No network, no file writes, no side effects. Safe to read and run.

Usage:
    # 10 t load, 0.5 t rigging, 0.5 t hook block; chart shows 15 t at the working radius
    python3 crane_utilisation.py --load 10 --rigging 0.5 --hook-block 0.5 --rated-capacity 15

    # tandem lift: de-rate each crane's chart capacity to 80%
    python3 crane_utilisation.py --load 18 --hook-block 0.6 --rated-capacity 30 --derate 0.8

    # custom critical-lift threshold, machine-readable, self-test
    python3 crane_utilisation.py --load 10 --rated-capacity 15 --critical-threshold 66 --json
    python3 crane_utilisation.py --selftest

Exit codes: 0 = success / tests passed, 1 = test failure, 2 = bad input.
"""
from __future__ import annotations

import argparse
import json
import sys

DEFAULT_CRITICAL_THRESHOLD = 75.0   # % of rated capacity commonly triggering a documented lift study


def compute(load: float, rated_capacity: float, rigging: float = 0.0, hook_block: float = 0.0,
            ancillaries: float = 0.0, derate: float = 1.0,
            critical_threshold: float = DEFAULT_CRITICAL_THRESHOLD) -> dict:
    """Build the gross load and compute utilisation against the (de-rated) chart capacity."""
    for name, val in (("--load", load), ("--rigging", rigging), ("--hook-block", hook_block),
                      ("--ancillaries", ancillaries)):
        if val < 0:
            raise ValueError(f"{name} must be >= 0, got {val!r}")
    if load <= 0:
        raise ValueError(f"--load must be positive, got {load!r}")
    if rated_capacity <= 0:
        raise ValueError(f"--rated-capacity must be positive, got {rated_capacity!r}")
    if not 0.0 < derate <= 1.0:
        raise ValueError(f"--derate must be >0 and <=1.0, got {derate!r}")
    if not 0.0 < critical_threshold <= 100.0:
        raise ValueError(f"--critical-threshold must be >0 and <=100, got {critical_threshold!r}")

    gross = load + rigging + hook_block + ancillaries
    effective_capacity = rated_capacity * derate
    utilisation = gross / effective_capacity * 100.0
    within_capacity = utilisation <= 100.0 + 1e-9
    is_critical = utilisation >= critical_threshold
    margin = effective_capacity - gross

    warnings = []
    if not within_capacity:
        warnings.append(f"OVER CAPACITY: gross load {gross:.2f} t exceeds the available capacity "
                        f"{effective_capacity:.2f} t ({utilisation:.1f}%). DO NOT LIFT — larger crane, "
                        "shorter radius, or different configuration required.")
    elif is_critical:
        warnings.append(f"CRITICAL LIFT: utilisation {utilisation:.1f}% is at/above the "
                        f"{critical_threshold:.0f}% threshold. Requires a documented lift study and a "
                        "lift supervisor.")
    if derate < 1.0:
        warnings.append(f"De-rating applied: chart capacity {rated_capacity:.2f} t x {derate:.2f} = "
                        f"{effective_capacity:.2f} t (e.g. tandem lift / dynamic / condition de-rate).")
    warnings.append("Rated capacity must be read from the actual crane chart at the actual radius and "
                    "configuration (outriggers/on-rubber, over-side/over-front, boom/jib). Chart governs.")

    return {
        "load": load,
        "rigging": rigging,
        "hook_block": hook_block,
        "ancillaries": ancillaries,
        "gross_load": round(gross, 3),
        "rated_capacity": rated_capacity,
        "derate": derate,
        "effective_capacity": round(effective_capacity, 3),
        "utilisation_pct": round(utilisation, 1),
        "within_capacity": within_capacity,
        "margin": round(margin, 3),
        "critical_threshold_pct": critical_threshold,
        "is_critical_lift": is_critical,
        "warnings": warnings,
    }


def _fmt(r: dict) -> str:
    verdict = "WITHIN CAPACITY" if r["within_capacity"] else "OVER CAPACITY"
    if r["within_capacity"] and r["is_critical_lift"]:
        verdict = "WITHIN CAPACITY (CRITICAL LIFT)"
    lines = [
        "Crane utilisation:",
        f"  Gross load build-up : load {r['load']} + rigging {r['rigging']} + hook block "
        f"{r['hook_block']} + ancillaries {r['ancillaries']}",
        f"  GROSS LOAD          : {r['gross_load']} t",
        f"  Rated capacity      : {r['rated_capacity']} t"
        + (f"  x de-rate {r['derate']} -> {r['effective_capacity']} t" if r['derate'] < 1.0 else ""),
        f"  Utilisation         : {r['utilisation_pct']}%  (margin {r['margin']} t)",
        f"  Critical threshold  : {r['critical_threshold_pct']:.0f}%",
        f"  Verdict             : {verdict}",
    ]
    if r["warnings"]:
        lines.append("  Notes:")
        lines.extend(f"    - {w}" for w in r["warnings"])
    return "\n".join(lines)


def _approx(a: float, b: float, tol: float = 0.1) -> bool:
    return abs(a - b) <= tol


def _selftest() -> int:
    failures = 0

    def check(desc, got, exp):
        nonlocal failures
        ok = (got == exp) if isinstance(exp, bool) else _approx(got, exp)
        print(f"  [{'PASS' if ok else 'FAIL'}] {desc}: got {got}, expected {exp}")
        if not ok:
            failures += 1

    # 10 + 0.5 + 0.5 = 11 t gross; 15 t chart -> 73.3% -> within, not critical (threshold 75).
    r = compute(10, 15, rigging=0.5, hook_block=0.5)
    check("gross load", r["gross_load"], 11.0)
    check("utilisation %", r["utilisation_pct"], 73.3)
    check("within capacity", r["within_capacity"], True)
    check("not critical at 73%", r["is_critical_lift"], False)

    # 11 t gross vs 14 t -> 78.6% -> critical.
    r = compute(10, 14, rigging=0.5, hook_block=0.5)
    check("critical at 78%", r["is_critical_lift"], True)
    check("still within capacity", r["within_capacity"], True)

    # 11 t gross vs 10 t -> 110% -> over capacity.
    r = compute(10, 10, rigging=0.5, hook_block=0.5)
    check("over capacity util", r["utilisation_pct"], 110.0)
    check("over capacity flag", r["within_capacity"], False)
    ok = any("OVER CAPACITY" in w for w in r["warnings"])
    print(f"  [{'PASS' if ok else 'FAIL'}] over-capacity warning present")
    if not ok:
        failures += 1

    # De-rate: 30 t chart x 0.8 = 24 t; gross 18.6 -> 77.5%.
    r = compute(18, 30, hook_block=0.6, derate=0.8)
    check("effective capacity (de-rated)", r["effective_capacity"], 24.0)
    check("de-rated utilisation", r["utilisation_pct"], 77.5)

    # Bad inputs rejected.
    for bad in [
        dict(load=0, rated_capacity=15),
        dict(load=10, rated_capacity=0),
        dict(load=10, rated_capacity=15, rigging=-1),
        dict(load=10, rated_capacity=15, derate=0),
        dict(load=10, rated_capacity=15, derate=1.5),
        dict(load=10, rated_capacity=15, critical_threshold=0),
        dict(load=10, rated_capacity=15, critical_threshold=120),
    ]:
        try:
            compute(**bad)
        except ValueError:
            print(f"  [PASS] rejected bad input {bad}")
        else:
            print(f"  [FAIL] accepted bad input {bad}")
            failures += 1

    print(f"\n{'ALL TESTS PASSED' if failures == 0 else f'{failures} TEST(S) FAILED'}")
    return 0 if failures == 0 else 1


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        description="Deterministic crane gross-load build-up and chart utilisation.")
    p.add_argument("--load", type=float, help="bare load weight, tonnes")
    p.add_argument("--rated-capacity", type=float,
                   help="crane rated capacity at the working radius/config (from the load chart), t")
    p.add_argument("--rigging", type=float, default=0.0, help="slings/shackles/lifting beam, t")
    p.add_argument("--hook-block", type=float, default=0.0, help="hook block weight, t")
    p.add_argument("--ancillaries", type=float, default=0.0, help="other below-the-hook items, t")
    p.add_argument("--derate", type=float, default=1.0,
                   help="multiply chart capacity by this (0<f<=1) for tandem/dynamic de-rating")
    p.add_argument("--critical-threshold", type=float, default=DEFAULT_CRITICAL_THRESHOLD,
                   help=f"utilisation %% flagged as a critical lift (default {DEFAULT_CRITICAL_THRESHOLD:.0f})")
    p.add_argument("--json", action="store_true", help="machine-readable output")
    p.add_argument("--selftest", action="store_true", help="run built-in tests and exit")
    args = p.parse_args(argv)

    if args.selftest:
        return _selftest()

    if args.load is None or args.rated_capacity is None:
        p.error("--load and --rated-capacity are required (or use --selftest)")

    try:
        r = compute(args.load, args.rated_capacity, args.rigging, args.hook_block,
                    args.ancillaries, args.derate, args.critical_threshold)
    except ValueError as e:
        p.error(str(e))

    if args.json:
        print(json.dumps(r, indent=2))
        return 0

    print(_fmt(r))
    print("\nPlanning aid only — the actual crane load chart and a competent person govern.")
    print("Not legal advice; not engineering certification.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
