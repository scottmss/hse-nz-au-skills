#!/usr/bin/env python3
"""ewp_load_check.py — deterministic EWP/MEWP platform-load and ground-bearing check.

A mobile elevating work platform's data plate states a RATED PLATFORM CAPACITY (kg) and a
MAX NUMBER OF PERSONS (and often a max manual force). The platform load — occupants + their
tools + materials — must stay within BOTH limits. This tool sums the platform load and checks
it against the data-plate figures, and (optionally) estimates the ground-bearing pressure under
a wheel or outrigger pad so it can be compared with the allowable ground bearing.

What it does NOT do (the data plate / manufacturer / a competent person govern):
  * It never reports capacity above the data-plate rating.
  * Person mass is an ASSUMPTION you supply (default 80 kg/person) — it is not chart data.
  * Wind, slope/grade, dynamic loads, manual force, boom position and outreach ALSO affect
    stability and the rated capacity — these need the manufacturer's chart and a competent
    person. This tool flags that; it cannot compute it.

This is a planning aid, NOT a substitute for the EWP data plate, the manufacturer's manual, or
a competent person. Confirm every figure before use.

Pure standard library. No network, no file writes, no side effects. Safe to read and run.

Usage:
    # 230 kg rated platform, max 2 persons; 2 people, 25 kg tools, 30 kg materials
    python3 ewp_load_check.py --rated-capacity 230 --max-persons 2 \
        --occupants 2 --tools 25 --materials 30

    # override the assumed person mass (e.g. 90 kg incl. PPE)
    python3 ewp_load_check.py --rated-capacity 230 --max-persons 2 --occupants 2 \
        --person-mass 90

    # ground-bearing pressure under one outrigger pad: 3200 kg point load on a 0.25 m2 pad
    python3 ewp_load_check.py --point-load 3200 --pad-area 0.25

    python3 ewp_load_check.py --self-test
"""
from __future__ import annotations

import argparse
import sys

DEFAULT_PERSON_MASS_KG = 80.0  # assumption — NOT chart data; override with --person-mass
G = 9.81  # m/s^2


def platform_load_check(
    rated_capacity_kg: float,
    max_persons: int,
    occupants: int,
    person_mass_kg: float = DEFAULT_PERSON_MASS_KG,
    tools_kg: float = 0.0,
    materials_kg: float = 0.0,
) -> dict:
    """Sum the platform load and check it against the data-plate capacity and persons limit."""
    if rated_capacity_kg <= 0:
        raise ValueError("rated_capacity_kg must be positive (read it from the data plate)")
    if max_persons <= 0:
        raise ValueError("max_persons must be positive (read it from the data plate)")
    if occupants < 0 or tools_kg < 0 or materials_kg < 0 or person_mass_kg <= 0:
        raise ValueError("occupants/tools/materials must be >= 0 and person_mass > 0")

    persons_load = occupants * person_mass_kg
    total_load = persons_load + tools_kg + materials_kg
    utilisation = total_load / rated_capacity_kg  # fraction of rated capacity
    within_capacity = total_load <= rated_capacity_kg
    within_persons = occupants <= max_persons
    return {
        "persons_load_kg": round(persons_load, 1),
        "tools_kg": round(tools_kg, 1),
        "materials_kg": round(materials_kg, 1),
        "total_load_kg": round(total_load, 1),
        "rated_capacity_kg": round(rated_capacity_kg, 1),
        "utilisation_pct": round(utilisation * 100, 1),
        "remaining_kg": round(rated_capacity_kg - total_load, 1),
        "within_capacity": within_capacity,
        "within_persons": within_persons,
        "max_persons": max_persons,
        "occupants": occupants,
        "person_mass_kg": person_mass_kg,
        "ok": within_capacity and within_persons,
    }


def ground_bearing_pressure_kpa(point_load_kg: float, pad_area_m2: float) -> float:
    """Estimate ground-bearing pressure (kPa) from a point load on a pad/wheel contact area.

    Compare the result with the allowable ground-bearing pressure for the surface (from a
    competent/geotechnical person). point_load_kg is the load through ONE leg/pad/wheel — read
    the per-leg loads from the manufacturer's data, do not guess them.
    """
    if point_load_kg <= 0 or pad_area_m2 <= 0:
        raise ValueError("point_load_kg and pad_area_m2 must be positive")
    force_kn = point_load_kg * G / 1000.0
    return round(force_kn / pad_area_m2, 1)  # kN/m^2 == kPa


def _fmt(check: dict) -> str:
    lines = [
        f"Platform load: {check['occupants']} persons x {check['person_mass_kg']:.0f} kg "
        f"= {check['persons_load_kg']} kg + tools {check['tools_kg']} kg "
        f"+ materials {check['materials_kg']} kg = {check['total_load_kg']} kg",
        f"Rated platform capacity: {check['rated_capacity_kg']} kg "
        f"(max {check['max_persons']} persons)",
        f"Utilisation: {check['utilisation_pct']}% of rated  |  remaining {check['remaining_kg']} kg",
        f"Within capacity: {'YES' if check['within_capacity'] else 'NO — OVERLOADED'}",
        f"Within persons limit: {'YES' if check['within_persons'] else 'NO — TOO MANY PERSONS'}",
        f"RESULT: {'OK to plan around (verify on the machine)' if check['ok'] else 'NOT ACCEPTABLE — reduce load/persons'}",
        "NOTE: person mass is an assumption, not chart data. Wind, slope, dynamic loads, manual",
        "force, boom outreach and lift height ALSO govern — confirm against the manufacturer's",
        "chart, the data plate and a competent person before use.",
    ]
    return "\n".join(lines)


def _self_test() -> int:
    # within both limits
    c = platform_load_check(230, 2, 2, person_mass_kg=80, tools_kg=25, materials_kg=30)
    assert c["total_load_kg"] == 215.0, c
    assert c["within_capacity"] and c["within_persons"] and c["ok"], c
    assert c["remaining_kg"] == 15.0, c
    # overloaded by mass
    c = platform_load_check(230, 2, 2, person_mass_kg=90, tools_kg=40, materials_kg=20)
    assert c["total_load_kg"] == 240.0 and not c["within_capacity"] and not c["ok"], c
    # too many persons (even if mass ok)
    c = platform_load_check(400, 2, 3, person_mass_kg=80)
    assert c["within_capacity"] and not c["within_persons"] and not c["ok"], c
    # utilisation maths
    c = platform_load_check(200, 2, 1, person_mass_kg=80, tools_kg=20)
    assert c["utilisation_pct"] == 50.0, c
    # ground bearing: 3200 kg on 0.25 m2 -> ~125.6 kPa
    p = ground_bearing_pressure_kpa(3200, 0.25)
    assert abs(p - 125.6) < 0.2, p
    # input validation
    for bad in (lambda: platform_load_check(0, 2, 1),
                lambda: platform_load_check(230, 0, 1),
                lambda: ground_bearing_pressure_kpa(100, 0)):
        try:
            bad()
        except ValueError:
            pass
        else:
            raise AssertionError("expected ValueError")
    print("ewp_load_check: all self-tests passed")
    return 0


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="EWP/MEWP platform-load and ground-bearing check.")
    p.add_argument("--rated-capacity", type=float, help="rated platform capacity (kg), from the data plate")
    p.add_argument("--max-persons", type=int, help="max number of persons, from the data plate")
    p.add_argument("--occupants", type=int, default=0, help="number of people on the platform")
    p.add_argument("--person-mass", type=float, default=DEFAULT_PERSON_MASS_KG,
                   help=f"assumed mass per person in kg (default {DEFAULT_PERSON_MASS_KG:.0f}; an assumption, not chart data)")
    p.add_argument("--tools", type=float, default=0.0, help="tools mass (kg)")
    p.add_argument("--materials", type=float, default=0.0, help="materials mass (kg)")
    p.add_argument("--point-load", type=float, help="per-leg/pad/wheel load (kg) for ground-bearing")
    p.add_argument("--pad-area", type=float, help="pad/wheel contact area (m2) for ground-bearing")
    p.add_argument("--self-test", action="store_true", help="run built-in checks and exit")
    args = p.parse_args(argv)

    if args.self_test:
        return _self_test()

    did = False
    if args.rated_capacity is not None and args.max_persons is not None:
        check = platform_load_check(
            args.rated_capacity, args.max_persons, args.occupants,
            person_mass_kg=args.person_mass, tools_kg=args.tools, materials_kg=args.materials,
        )
        print(_fmt(check))
        did = True
    if args.point_load is not None and args.pad_area is not None:
        kpa = ground_bearing_pressure_kpa(args.point_load, args.pad_area)
        print(f"\nGround-bearing pressure: {kpa} kPa under a {args.pad_area} m2 pad "
              f"({args.point_load} kg). Compare with the allowable ground bearing (competent person).")
        did = True
    if not did:
        p.print_help()
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
