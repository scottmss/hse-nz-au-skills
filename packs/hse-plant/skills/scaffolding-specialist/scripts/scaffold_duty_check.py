#!/usr/bin/env python3
"""scaffold_duty_check.py — deterministic scaffold duty-load check.

A scaffold working platform has a DUTY (load) rating. The intended load — people + their
tools/materials on a bay — must stay within the rating for the duty class on the SCAFTAG /
design. This tool checks the load per bay against the duty rating and the concentrated-load
limit, for the standard AS/NZS duty classes (or a special-duty figure you supply).

Standard duty ratings (per working platform per bay) — a planning convenience, the SCAFTAG /
scaffold design GOVERNS, confirm against AS/NZS 1576 / 4576 and the actual tag:
  * light   225 kg/bay  (concentrated 120 kg)  e.g. painting, inspection, electrical
  * medium  450 kg/bay  (concentrated 150 kg)  e.g. general trades, light steel, tiling
  * heavy   675 kg/bay  (concentrated 200 kg)  e.g. bricklaying, blockwork, demolition
  * special  as designed (supply --allowable-per-bay and --concentrated-allow)

What it does NOT do (the scaffold design / scaftag / a competent person govern):
  * Person mass is an ASSUMPTION you supply (default 80 kg/person) — not chart data.
  * The number of bays/platforms loaded at once, ties/bracing, foundations, height and wind
    are governed by the DESIGN — this tool flags that; it cannot compute structural adequacy.

This is a planning aid, NOT a substitute for the scaftag, the scaffold design, AS/NZS 1576/4576
or a competent person. Confirm every figure before loading a scaffold.

Pure standard library. No network, no file writes, no side effects. Safe to read and run.

Usage:
    # medium-duty bay: 2 people + 180 kg of block
    python3 scaffold_duty_check.py --duty medium --persons 2 --materials 180

    # check a concentrated (point) load too
    python3 scaffold_duty_check.py --duty heavy --persons 1 --materials 400 --concentrated 180

    # special-duty: supply the design figures
    python3 scaffold_duty_check.py --duty special --allowable-per-bay 900 \
        --concentrated-allow 250 --persons 2 --materials 600

    python3 scaffold_duty_check.py --self-test
"""
from __future__ import annotations

import argparse
import sys

DEFAULT_PERSON_MASS_KG = 80.0  # assumption — NOT chart data; override with --person-mass

# (allowable UDL per platform per bay kg, concentrated allowance kg) — confirm on the scaftag.
DUTY = {
    "light": (225.0, 120.0),
    "medium": (450.0, 150.0),
    "heavy": (675.0, 200.0),
}


def duty_check(
    allowable_per_bay_kg: float,
    persons: int,
    person_mass_kg: float = DEFAULT_PERSON_MASS_KG,
    materials_kg: float = 0.0,
    concentrated_kg: float | None = None,
    concentrated_allow_kg: float | None = None,
) -> dict:
    """Check the per-bay load (and optional concentrated load) against the duty rating."""
    if allowable_per_bay_kg <= 0:
        raise ValueError("allowable_per_bay_kg must be positive (read the duty rating / scaftag)")
    if persons < 0 or materials_kg < 0 or person_mass_kg <= 0:
        raise ValueError("persons/materials must be >= 0 and person_mass > 0")

    persons_load = persons * person_mass_kg
    total = persons_load + materials_kg
    within = total <= allowable_per_bay_kg
    result = {
        "persons_load_kg": round(persons_load, 1),
        "materials_kg": round(materials_kg, 1),
        "total_per_bay_kg": round(total, 1),
        "allowable_per_bay_kg": round(allowable_per_bay_kg, 1),
        "utilisation_pct": round(total / allowable_per_bay_kg * 100, 1),
        "remaining_kg": round(allowable_per_bay_kg - total, 1),
        "within_udl": within,
        "person_mass_kg": person_mass_kg,
        "concentrated_kg": None,
        "concentrated_allow_kg": None,
        "within_concentrated": True,
    }
    if concentrated_kg is not None:
        if concentrated_kg < 0:
            raise ValueError("concentrated_kg must be >= 0")
        result["concentrated_kg"] = round(concentrated_kg, 1)
        if concentrated_allow_kg is not None:
            if concentrated_allow_kg <= 0:
                raise ValueError("concentrated_allow_kg must be positive")
            result["concentrated_allow_kg"] = round(concentrated_allow_kg, 1)
            result["within_concentrated"] = concentrated_kg <= concentrated_allow_kg
    result["ok"] = result["within_udl"] and result["within_concentrated"]
    return result


def _fmt(c: dict, duty_label: str) -> str:
    lines = [
        f"Duty: {duty_label}  (allowable {c['allowable_per_bay_kg']} kg per platform per bay)",
        f"Load per bay: {c['persons_load_kg']} kg persons + {c['materials_kg']} kg materials "
        f"= {c['total_per_bay_kg']} kg",
        f"Utilisation: {c['utilisation_pct']}% of duty  |  remaining {c['remaining_kg']} kg",
        f"Within duty (UDL): {'YES' if c['within_udl'] else 'NO — OVER DUTY RATING'}",
    ]
    if c["concentrated_kg"] is not None:
        if c["concentrated_allow_kg"] is not None:
            lines.append(
                f"Concentrated load: {c['concentrated_kg']} kg vs allowance "
                f"{c['concentrated_allow_kg']} kg — "
                f"{'YES' if c['within_concentrated'] else 'NO — OVER CONCENTRATED LIMIT'}"
            )
        else:
            lines.append(
                f"Concentrated load: {c['concentrated_kg']} kg (no allowance supplied — confirm on scaftag)"
            )
    lines += [
        f"RESULT: {'OK to plan around (verify on the scaftag)' if c['ok'] else 'NOT ACCEPTABLE — reduce load or use a higher duty'}",
        "NOTE: person mass is an assumption, not chart data. Number of loaded bays, ties/bracing,",
        "foundations, height and wind are governed by the DESIGN — the scaftag and a competent",
        "scaffolder/engineer govern. Confirm against AS/NZS 1576/4576 before loading.",
    ]
    return "\n".join(lines)


def _self_test() -> int:
    # medium duty, within
    c = duty_check(450, 2, person_mass_kg=80, materials_kg=180)
    assert c["total_per_bay_kg"] == 340.0 and c["within_udl"] and c["ok"], c
    assert c["remaining_kg"] == 110.0, c
    # over duty
    c = duty_check(225, 2, person_mass_kg=80, materials_kg=120)
    assert c["total_per_bay_kg"] == 280.0 and not c["within_udl"] and not c["ok"], c
    # concentrated over limit fails overall even if UDL ok
    c = duty_check(675, 1, person_mass_kg=80, materials_kg=200,
                   concentrated_kg=250, concentrated_allow_kg=200)
    assert c["within_udl"] and not c["within_concentrated"] and not c["ok"], c
    # utilisation maths
    c = duty_check(450, 0, materials_kg=225)
    assert c["utilisation_pct"] == 50.0, c
    # duty table values
    assert DUTY["light"] == (225.0, 120.0) and DUTY["heavy"] == (675.0, 200.0)
    # validation
    for bad in (lambda: duty_check(0, 1),
                lambda: duty_check(225, -1),
                lambda: duty_check(225, 1, concentrated_kg=10, concentrated_allow_kg=0)):
        try:
            bad()
        except ValueError:
            pass
        else:
            raise AssertionError("expected ValueError")
    print("scaffold_duty_check: all self-tests passed")
    return 0


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Scaffold duty-load check (per platform per bay).")
    p.add_argument("--duty", choices=["light", "medium", "heavy", "special"],
                   help="duty class; 'special' requires --allowable-per-bay")
    p.add_argument("--allowable-per-bay", type=float,
                   help="special-duty allowable load per bay (kg), from the design/scaftag")
    p.add_argument("--concentrated-allow", type=float,
                   help="special-duty concentrated-load allowance (kg)")
    p.add_argument("--persons", type=int, default=0, help="people on the bay")
    p.add_argument("--person-mass", type=float, default=DEFAULT_PERSON_MASS_KG,
                   help=f"assumed mass per person kg (default {DEFAULT_PERSON_MASS_KG:.0f}; an assumption)")
    p.add_argument("--materials", type=float, default=0.0, help="materials mass on the bay (kg)")
    p.add_argument("--concentrated", type=float, help="a concentrated (point) load to check (kg)")
    p.add_argument("--self-test", action="store_true", help="run built-in checks and exit")
    args = p.parse_args(argv)

    if args.self_test:
        return _self_test()
    if not args.duty:
        p.print_help()
        return 2

    if args.duty == "special":
        if args.allowable_per_bay is None:
            p.error("--duty special requires --allowable-per-bay")
        allow, conc_allow = args.allowable_per_bay, args.concentrated_allow
        label = f"special ({allow:.0f} kg/bay)"
    else:
        allow, conc_allow = DUTY[args.duty]
        label = args.duty
        if args.concentrated_allow is not None:
            conc_allow = args.concentrated_allow

    c = duty_check(allow, args.persons, person_mass_kg=args.person_mass,
                   materials_kg=args.materials, concentrated_kg=args.concentrated,
                   concentrated_allow_kg=conc_allow)
    print(_fmt(c, label))
    return 0


if __name__ == "__main__":
    sys.exit(main())
