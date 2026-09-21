#!/usr/bin/env python3
"""sling_wll_calculator.py — deterministic sling-angle de-rating for lifting-rigging-specialist.

Given the WLL of a SINGLE leg of a sling set, the number of legs, and the sling angle,
computes the de-rated capacity of the assembly and the tension in each loaded leg. This is
the calculation a rigger must not eyeball — the WLL of a multi-leg sling falls as the
included angle between the legs opens up.

Two rating methods (NZ ACOP for Load-lifting Rigging):
  * uniform  (general-purpose, DEFAULT) — conservative: rates 3- and 4-leg slings on 3
             EFFECTIVE legs, because a rigid load may be carried on only two or three legs.
  * trig     (special-purpose) — credits the ACTUAL number of legs; ONLY valid where equal
             load-sharing genuinely occurs (flexible load or adjustable-length legs).

Capacity factor for a leg at angle B from the vertical = cos(B).
Assembly WLL = single_leg_WLL * effective_legs * cos(B).

Angle input is the angle from the VERTICAL by default; pass --included to give the total
included angle between opposite legs instead (B = included / 2).

This is a planning aid, NOT a substitute for the marked WLL / sling tag, the manufacturer's
rating, or a competent person. Confirm every figure against the actual gear before lifting.

Pure standard library. No network, no file writes, no side effects. Safe to read and run.

Usage:
    # 2-leg sling, single-leg WLL 2.0 t, 45 deg from vertical
    python3 sling_wll_calculator.py --wll 2.0 --legs 2 --angle 45

    # give the included angle instead of angle-from-vertical
    python3 sling_wll_calculator.py --wll 2.0 --legs 2 --included 90

    # 4-leg, special-purpose trig method (equal sharing assured)
    python3 sling_wll_calculator.py --wll 5.3 --legs 4 --angle 30 --method trig

    # machine-readable / self-test
    python3 sling_wll_calculator.py --wll 2 --legs 2 --angle 45 --json
    python3 sling_wll_calculator.py --selftest

Exit codes: 0 = success / tests passed, 1 = test failure, 2 = bad input.
"""
from __future__ import annotations

import argparse
import json
import math
import sys

# Practical angle guidance (angle from vertical, degrees).
ANGLE_PREFERRED_MAX = 45.0   # <=45 deg from vertical (<=90 deg included): keep here where practicable
ANGLE_HARD_MAX = 60.0        # 60 deg from vertical (120 deg included): practical maximum, do not exceed

# Choke-hitch WLL reduction (fraction of straight-pull WLL).
CHOKE_FACTOR = {"square": 0.80, "oblong": 0.80, "round": 0.75}


def effective_legs(legs: int, method: str) -> int:
    """How many legs are credited with carrying load."""
    if legs not in (1, 2, 3, 4):
        raise ValueError(f"legs must be 1, 2, 3 or 4, got {legs!r}")
    if method == "trig":
        return legs                      # credit actual legs (equal sharing must be assured)
    if method == "uniform":
        return min(legs, 3)              # conservative: 3- and 4-leg rated on 3 legs
    raise ValueError(f"method must be 'uniform' or 'trig', got {method!r}")


def compute(wll: float, legs: int, angle_from_vertical: float, method: str = "uniform",
            choke: str | None = None) -> dict:
    """De-rate a sling set. angle_from_vertical in degrees (0 = vertical legs)."""
    if wll <= 0:
        raise ValueError(f"--wll (single-leg WLL) must be positive, got {wll!r}")
    if not 0.0 <= angle_from_vertical < 90.0:
        raise ValueError("angle from vertical must be >=0 and <90 degrees "
                         f"(included angle <180), got {angle_from_vertical!r}")

    eff = effective_legs(legs, method)
    cos_b = math.cos(math.radians(angle_from_vertical))
    factor = eff * cos_b
    assembly_wll = wll * factor

    if choke:
        c = choke.lower()
        if c not in CHOKE_FACTOR:
            raise ValueError(f"--choke must be one of {sorted(CHOKE_FACTOR)}, got {choke!r}")
        assembly_wll *= CHOKE_FACTOR[c]

    # Tension per loaded leg when the assembly is loaded to its WLL:
    # each effective leg carries (assembly / eff) vertically, = wll*cos_b ... / cos_b at the leg = wll.
    # Reported as the share of the rated load each effective leg sees.
    per_leg_tension = assembly_wll / (eff * cos_b) if cos_b else float("inf")

    warnings = []
    if angle_from_vertical > ANGLE_HARD_MAX:
        warnings.append(f"Angle {angle_from_vertical:.0f} deg from vertical exceeds the 60 deg "
                        "practical maximum (120 deg included). DO NOT lift — shorten/realign the "
                        "legs or use a lifting beam/spreader.")
    elif angle_from_vertical > ANGLE_PREFERRED_MAX:
        warnings.append(f"Angle {angle_from_vertical:.0f} deg from vertical is above the preferred "
                        "45 deg (90 deg included). Reduce the angle where practicable.")
    if method == "trig" and legs >= 3:
        warnings.append("Trig/special-purpose method credits all legs — only valid if EQUAL "
                        "load-sharing is assured (flexible load or adjustable legs). For a rigid "
                        "load use the uniform method.")
    if choke:
        warnings.append(f"Choke hitch applied ({choke}): WLL reduced to "
                        f"{int(CHOKE_FACTOR[choke.lower()]*100)}% of straight pull.")

    return {
        "single_leg_wll": wll,
        "legs": legs,
        "effective_legs": eff,
        "method": method,
        "angle_from_vertical_deg": angle_from_vertical,
        "included_angle_deg": angle_from_vertical * 2,
        "leg_capacity_factor": round(cos_b, 4),
        "assembly_factor": round(factor, 4),
        "choke": choke,
        "assembly_wll": round(assembly_wll, 3),
        "per_leg_tension_at_wll": round(per_leg_tension, 3),
        "warnings": warnings,
    }


def _fmt(r: dict) -> str:
    lines = [
        "Sling assembly de-rating:",
        f"  Single-leg WLL    : {r['single_leg_wll']} t",
        f"  Legs              : {r['legs']}  (effective: {r['effective_legs']}, "
        f"method: {r['method']})",
        f"  Angle             : {r['angle_from_vertical_deg']:.0f} deg from vertical "
        f"({r['included_angle_deg']:.0f} deg included)",
        f"  Leg factor cos(B) : {r['leg_capacity_factor']}",
        f"  Assembly factor   : {r['assembly_factor']}  (effective_legs x cos B"
        + (f" x choke" if r['choke'] else "") + ")",
        f"  ASSEMBLY WLL      : {r['assembly_wll']} t",
    ]
    if r["warnings"]:
        lines.append("  Warnings:")
        lines.extend(f"    - {w}" for w in r["warnings"])
    return "\n".join(lines)


def _approx(a: float, b: float, tol: float = 0.01) -> bool:
    return abs(a - b) <= tol


def _selftest() -> int:
    failures = 0

    def check(desc, got, exp):
        nonlocal failures
        ok = _approx(got, exp)
        print(f"  [{'PASS' if ok else 'FAIL'}] {desc}: got {got}, expected {exp}")
        if not ok:
            failures += 1

    # Vertical legs: factor == effective legs.
    check("2-leg vertical assembly WLL (2.0 t)", compute(2.0, 2, 0)["assembly_wll"], 4.0)
    # 2-leg at 60 deg from vertical: 2 * cos60 = 1.0 -> assembly == single-leg WLL.
    check("2-leg @60deg assembly WLL (2.0 t)", compute(2.0, 2, 60)["assembly_wll"], 2.0)
    # 2-leg at 45 deg: 2 * cos45 = 1.414.
    check("2-leg @45deg assembly WLL (2.0 t)", compute(2.0, 2, 45)["assembly_wll"], 2.828)
    # 4-leg uniform: effective 3 legs.
    check("4-leg uniform vertical (1.0 t)", compute(1.0, 4, 0, "uniform")["assembly_wll"], 3.0)
    # 4-leg trig: effective 4 legs.
    check("4-leg trig vertical (1.0 t)", compute(1.0, 4, 0, "trig")["assembly_wll"], 4.0)
    # Choke on round load: -25%.
    check("1-leg choke round (4.0 t)", compute(4.0, 1, 0, choke="round")["assembly_wll"], 3.0)

    # Effective-legs logic.
    for legs, exp in ((1, 1), (2, 2), (3, 3), (4, 3)):
        check(f"uniform effective legs ({legs}-leg)", effective_legs(legs, "uniform"), exp)
    for legs, exp in ((3, 3), (4, 4)):
        check(f"trig effective legs ({legs}-leg)", effective_legs(legs, "trig"), exp)

    # Warning fires beyond 60 deg.
    over = compute(2.0, 2, 65)
    ok = any("practical maximum" in w for w in over["warnings"])
    print(f"  [{'PASS' if ok else 'FAIL'}] >60deg triggers do-not-lift warning")
    if not ok:
        failures += 1

    # Bad inputs rejected.
    for bad in [
        dict(wll=0, legs=2, angle_from_vertical=30),
        dict(wll=2, legs=5, angle_from_vertical=30),
        dict(wll=2, legs=2, angle_from_vertical=90),
        dict(wll=2, legs=2, angle_from_vertical=30, method="bogus"),
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
        description="Deterministic sling-angle WLL de-rating (NZ ACOP uniform/trig methods).")
    p.add_argument("--wll", type=float, help="WLL of a SINGLE leg, in tonnes")
    p.add_argument("--legs", type=int, choices=[1, 2, 3, 4], help="number of sling legs")
    grp = p.add_mutually_exclusive_group()
    grp.add_argument("--angle", type=float, help="angle from the VERTICAL, degrees (0 = vertical)")
    grp.add_argument("--included", type=float, help="total INCLUDED angle between opposite legs, deg")
    p.add_argument("--method", choices=["uniform", "trig"], default="uniform",
                   help="uniform = general-purpose/conservative (default); trig = special-purpose")
    p.add_argument("--choke", choices=sorted(CHOKE_FACTOR), help="apply a choke-hitch reduction")
    p.add_argument("--json", action="store_true", help="machine-readable output")
    p.add_argument("--selftest", action="store_true", help="run built-in tests and exit")
    args = p.parse_args(argv)

    if args.selftest:
        return _selftest()

    if args.wll is None or args.legs is None or (args.angle is None and args.included is None):
        p.error("--wll, --legs and (--angle or --included) are required (or use --selftest)")

    angle = args.angle if args.angle is not None else args.included / 2.0

    try:
        r = compute(args.wll, args.legs, angle, args.method, args.choke)
    except ValueError as e:
        p.error(str(e))

    if args.json:
        print(json.dumps(r, indent=2))
        return 0

    print(_fmt(r))
    print("\nPlanning aid only — confirm against the sling's marked WLL/tag and a competent person.")
    print("Not legal advice; not engineering certification.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
