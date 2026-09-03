#!/usr/bin/env python3
"""energy_calculator.py — deterministic energy-magnitude estimation for energy-based safety.

Computes the physical energy of a hazard in joules and classifies it against the
energy-based safety bands used by CHASNZ / the CSRA research:

    < 500 J        low energy      most likely outcome: first-aid injury
    500 - 1500 J   moderate        most likely outcome: medical / lost-time injury
    > 1500 J       HIGH ENERGY     most likely outcome: serious injury or fatality (SIF)

Use this when no quick classifier in references/high-energy-thresholds.md applies -
dropped tools, materials at height, hoses under pressure, hand tools, small components -
rather than guessing. Guessing is wrong in both directions: people over-classify tape
measures and under-classify pressurised lines.

IMPORTANT LIMITS - read before relying on a number:
  * Health hazards (chemical, biological, noise, vibration, radiation, thermal) are NOT
    assessed in joules. They are high energy when exposure exceeds the workplace exposure
    standard, when oxygen falls below ~16%, or for pH < 2 / > 12.5. This tool will refuse
    to pretend otherwise.
  * ELECTRICAL results are informative only. The energy model treats electrocution as heat
    deposition; the actual killing mechanism is ventricular fibrillation from current across
    the heart. Mains voltage computes "low" and still kills. Use the >= 50 V classifier.
  * Low energy does NOT mean safe. It means a SIF is not the most likely outcome, so the
    hazard is managed through the ordinary risk process rather than as a fatal exposure.
  * A calculated figure is a decision aid, not a statutory test, and not a substitute for a
    competent person's judgement.

Pure standard library. No network, no file writes, no side effects. Safe to read and run.

Usage:
    # a 12 kg tool dropped 8 m
    python3 energy_calculator.py gravity --mass 12 --height 8

    # a 3.5 t excavator slewing at 1.5 m/s next to a worker on foot
    python3 energy_calculator.py motion --mass 3500 --velocity 1.5

    # ... or give speed in km/h
    python3 energy_calculator.py motion --mass 1200 --kmh 40

    # a 50 L receiver at 120 psi
    python3 energy_calculator.py pressure-vessel --psi 120 --litres 50

    # 1 m of 100 mm line at 60 psi
    python3 energy_calculator.py pressure-pipe --psi 60 --diameter 0.1

    # a 230 mm 0.8 kg cutting disc at 6600 rpm
    python3 energy_calculator.py rotation --mass 0.8 --radius 0.115 --rpm 6600

    # a cable stretched 0.3 m under 20 kN
    python3 energy_calculator.py elastic --force 20000 --extension 0.3

    # electrical (informative only)
    python3 energy_calculator.py electrical --volts 400 --seconds 0.2

    # machine-readable
    python3 energy_calculator.py gravity --mass 90 --height 4.6 --json

    # built-in self-test against the published worked examples
    python3 energy_calculator.py --selftest

Exit codes: 0 = success / tests passed, 1 = self-test failure, 2 = bad input.
"""
from __future__ import annotations

import argparse
import json
import math
import sys

G = 9.8                 # m/s^2
BODY_RESISTANCE = 1500  # ohms, assumed, for the electrical estimate
PA_PER_PSI = 7000       # the convention used in the source equations

LOW_BAND = 500.0        # J
HIGH_BAND = 1500.0      # J

BANDS = (
    (LOW_BAND, "Low energy", "Most likely outcome: first-aid injury."),
    (HIGH_BAND, "Moderate energy", "Most likely outcome: medical treatment or lost-time injury."),
    (math.inf, "HIGH ENERGY", "Most likely outcome: SERIOUS INJURY OR FATALITY. "
                              "Requires a direct control."),
)

ELECTRICAL_NOTE = (
    "INFORMATIVE ONLY. The energy model treats electrical harm as heat deposition, but "
    "electrocution kills by ventricular fibrillation from current across the heart. Mains "
    "voltage computes as low energy and still kills. For electrical work use the >= 50 V "
    "classifier and treat any contact with >= 50 V, and any arc flash, as HIGH ENERGY."
)


def classify(joules: float) -> dict:
    """Band a joule figure. Returns a dict; never raises for a finite non-negative value."""
    for upper, label, meaning in BANDS:
        if joules < upper:
            return {
                "joules": round(joules, 1),
                "band": label,
                "high_energy": label == "HIGH ENERGY",
                "meaning": meaning,
            }
    raise AssertionError("unreachable: bands are exhaustive")


def _positive(name: str, value: float, allow_zero: bool = False) -> float:
    if value is None:
        raise ValueError(f"{name} is required")
    if value < 0 or (value == 0 and not allow_zero):
        raise ValueError(f"{name} must be a positive number (got {value})")
    return float(value)


# --- energy models ---------------------------------------------------------------

def gravity(mass_kg: float, height_m: float) -> float:
    """Potential energy of a raised mass: E = m x h x g."""
    return _positive("mass", mass_kg) * _positive("height", height_m) * G


def motion(mass_kg: float, velocity_ms: float) -> float:
    """Kinetic energy of a moving mass: E = 0.5 x m x v^2."""
    return 0.5 * _positive("mass", mass_kg) * _positive("velocity", velocity_ms) ** 2


def electrical_from_voltage(volts: float, seconds: float) -> float:
    """E = t x V^2 / R, assuming a 1500 ohm body and full conversion to heat."""
    return _positive("seconds", seconds) * _positive("volts", volts) ** 2 / BODY_RESISTANCE


def electrical_from_current(amps: float, seconds: float) -> float:
    """E = t x I^2 x R."""
    return _positive("seconds", seconds) * _positive("amps", amps) ** 2 * BODY_RESISTANCE


def pressure_vessel(psi: float, litres: float) -> float:
    """Stored energy in a vessel: E = 7000 x psi x 0.001 x volume(L)."""
    return PA_PER_PSI * _positive("psi", psi) * 0.001 * _positive("litres", litres)


def pressure_pipe(psi: float, diameter_m: float) -> float:
    """Stored energy per metre of line: E = 7000 x psi x pi x (0.5 x d)^2."""
    return PA_PER_PSI * _positive("psi", psi) * math.pi * (0.5 * _positive("diameter", diameter_m)) ** 2


def rotation(mass_kg: float, rpm: float, radius_m: float = None, length_m: float = None) -> float:
    """Rotational energy: E = 0.5 x I x omega^2.

    Rotational inertia I = 0.5 x m x r^2 for a cylinder about its axis (give --radius),
    or I = 0.33 x m x L^2 for a rod rotating about one end (give --length).
    """
    m = _positive("mass", mass_kg)
    if (radius_m is None) == (length_m is None):
        raise ValueError("give exactly one of --radius (cylinder) or --length (rod about one end)")
    inertia = 0.5 * m * _positive("radius", radius_m) ** 2 if radius_m is not None \
        else 0.33 * m * _positive("length", length_m) ** 2
    omega = _positive("rpm", rpm) * 0.104   # rad/s
    return 0.5 * inertia * omega ** 2


def elastic(stiffness_n_per_m: float, distance_m: float) -> float:
    """Elastic energy in tension or compression: E = 0.5 x k x d^2."""
    return 0.5 * _positive("stiffness", stiffness_n_per_m) * _positive("distance", distance_m) ** 2


# --- cli -------------------------------------------------------------------------

def _fmt(title: str, result: dict, detail: str = "", note: str = "") -> str:
    lines = [title, "=" * len(title), ""]
    if detail:
        lines += [detail, ""]
    lines += [
        f"  Energy      {result['joules']:,.1f} J",
        f"  Band        {result['band']}",
        f"  {result['meaning']}",
    ]
    if note:
        lines += ["", f"  ! {note}"]
    return "\n".join(lines)


SELFTESTS = [
    # (label, computed joules, expected joules, tolerance, expected band)
    ("90 kg person falls 4.6 m", gravity(90, 4.6), 4057, 5, "HIGH ENERGY"),
    ("0.45 kg tape measure falls 3 m", gravity(0.45, 3), 13.2, 1, "Low energy"),
    ("1200 kg vehicle at 11 m/s", motion(1200, 11), 72600, 10, "HIGH ENERGY"),
    ("100 kg pipe carried at 1.34 m/s", motion(100, 1.34), 90, 2, "Low energy"),
    ("220 V for 2 s", electrical_from_voltage(220, 2), 64.5, 1, "Low energy"),
    ("10 kV arc flash for 0.05 s", electrical_from_voltage(10000, 0.05), 3333, 5, "HIGH ENERGY"),
    ("10 L acetylene cylinder at 250 psi", pressure_vessel(250, 10), 17500, 5, "HIGH ENERGY"),
    ("50 mm gas line at 40 psi", pressure_pipe(40, 0.05), 550, 5, "Moderate energy"),
    ("0.3 kg grinder wheel, 114 mm dia, 11000 rpm",
     rotation(0.3, 11000, radius_m=0.114 / 2), 320, 5, "Low energy"),
    ("cable extended 0.25 m, k = 17792 N/m", elastic(17792, 0.25), 556, 5, "Moderate energy"),
]


def selftest() -> int:
    failures = 0
    print("Self-test against the published worked examples\n")
    for label, got, expected, tol, band in SELFTESTS:
        result = classify(got)
        ok = abs(got - expected) <= tol and result["band"] == band
        print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n"
              f"         {got:,.1f} J (expected ~{expected:,.0f}) -> {result['band']}")
        if not ok:
            failures += 1
    # band boundaries
    for joules, band in ((499.9, "Low energy"), (500.0, "Moderate energy"),
                         (1499.9, "Moderate energy"), (1500.0, "HIGH ENERGY")):
        got_band = classify(joules)["band"]
        ok = got_band == band
        print(f"  [{'PASS' if ok else 'FAIL'}] boundary {joules} J -> {got_band}")
        if not ok:
            failures += 1
    print()
    if failures:
        print(f"{failures} failure(s)")
        return 1
    print("All self-tests passed.")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="Estimate hazard energy in joules and classify it against the "
                    "1,500 J high-energy (SIF) threshold.",
        epilog="Health hazards are assessed against exposure standards, not joules. "
               "Not legal advice.",
    )
    p.add_argument("--selftest", action="store_true", help="run the built-in worked examples")
    p.add_argument("--json", action="store_true", help="machine-readable output")

    # --json is accepted either before or after the subcommand. SUPPRESS keeps the
    # subparser from overwriting a --json given at the top level with its own default.
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--json", action="store_true", default=argparse.SUPPRESS,
                        help="machine-readable output")

    sub = p.add_subparsers(dest="model", parser_class=argparse.ArgumentParser)

    def add(name, **kw):
        return sub.add_parser(name, parents=[common], **kw)

    g = add("gravity", help="a raised or falling mass (person, tool, load)")
    g.add_argument("--mass", type=float, required=True, help="kg")
    g.add_argument("--height", type=float, required=True, help="m")

    m = add("motion", help="a moving mass (vehicle, plant, projectile)")
    m.add_argument("--mass", type=float, required=True, help="kg")
    mv = m.add_mutually_exclusive_group(required=True)
    mv.add_argument("--velocity", type=float, help="m/s")
    mv.add_argument("--kmh", type=float, help="km/h")

    e = add("electrical", help="electrical contact (INFORMATIVE ONLY - see the note)")
    e.add_argument("--seconds", type=float, required=True, help="contact time, s")
    ev = e.add_mutually_exclusive_group(required=True)
    ev.add_argument("--volts", type=float, help="V")
    ev.add_argument("--amps", type=float, help="A")

    pv = add("pressure-vessel", help="stored energy in a pressurised vessel")
    pv.add_argument("--psi", type=float, required=True, help="internal pressure, psi (1 psi = 6.89 kPa)")
    pv.add_argument("--litres", type=float, required=True, help="vessel volume, L")

    pp = add("pressure-pipe", help="stored energy per metre of pressurised line")
    pp.add_argument("--psi", type=float, required=True, help="internal pressure, psi")
    pp.add_argument("--diameter", type=float, required=True, help="internal diameter, m")

    r = add("rotation", help="a rotating mass (disc, wheel, rotor)")
    r.add_argument("--mass", type=float, required=True, help="kg")
    r.add_argument("--rpm", type=float, required=True, help="revolutions per minute")
    rg = r.add_mutually_exclusive_group(required=True)
    rg.add_argument("--radius", type=float, help="m - cylinder/disc about its axis")
    rg.add_argument("--length", type=float, help="m - rod about one end")

    el = add("elastic", help="tension or compression (cable, spring, tensioned member)")
    el.add_argument("--extension", type=float, required=True, help="m from rest length")
    eg = el.add_mutually_exclusive_group(required=True)
    eg.add_argument("--stiffness", type=float, help="N/m")
    eg.add_argument("--force", type=float, help="N at the given extension (k is derived)")

    return p


def main() -> int:
    p = build_parser()
    args = p.parse_args()

    if args.selftest:
        return selftest()
    if not args.model:
        p.print_help()
        return 0

    detail = ""
    note = ""
    try:
        if args.model == "gravity":
            joules = gravity(args.mass, args.height)
            title = "Gravity - potential energy"
            detail = f"E = {args.mass} kg x {args.height} m x {G} m/s^2"
        elif args.model == "motion":
            v = args.velocity if args.velocity is not None else args.kmh / 3.6
            joules = motion(args.mass, v)
            title = "Motion - kinetic energy"
            detail = (f"E = 0.5 x {args.mass} kg x ({v:.2f} m/s)^2"
                      f"{'' if args.velocity is not None else f'   [{args.kmh} km/h]'}")
            note = ("Assess from the point of view of the person exposed - a plant strike is "
                    "assessed for the worker on foot, a crash for the vehicle occupants.")
        elif args.model == "electrical":
            if args.volts is not None:
                joules = electrical_from_voltage(args.volts, args.seconds)
                detail = f"E = {args.seconds} s x ({args.volts} V)^2 / {BODY_RESISTANCE} ohm"
            else:
                joules = electrical_from_current(args.amps, args.seconds)
                detail = f"E = {args.seconds} s x ({args.amps} A)^2 x {BODY_RESISTANCE} ohm"
            title = "Electrical - estimated thermal energy"
            note = ELECTRICAL_NOTE
        elif args.model == "pressure-vessel":
            joules = pressure_vessel(args.psi, args.litres)
            title = "Pressure - stored energy in a vessel"
            detail = f"E = {PA_PER_PSI} x {args.psi} psi x 0.001 x {args.litres} L"
        elif args.model == "pressure-pipe":
            joules = pressure_pipe(args.psi, args.diameter)
            title = "Pressure - stored energy per metre of line"
            detail = f"E = {PA_PER_PSI} x {args.psi} psi x pi x (0.5 x {args.diameter} m)^2"
            note = "Per metre of line. A long run stores proportionally more."
        elif args.model == "rotation":
            joules = rotation(args.mass, args.rpm, radius_m=args.radius, length_m=args.length)
            title = "Mechanical - rotational energy"
            shape = f"cylinder r = {args.radius} m" if args.radius is not None \
                else f"rod L = {args.length} m about one end"
            detail = f"{shape}, {args.mass} kg at {args.rpm} rpm ({args.rpm * 0.104:.1f} rad/s)"
            note = ("Heavy rotating equipment beyond a powered hand tool should be treated as "
                    "high energy by default rather than calculated.")
        elif args.model == "elastic":
            k = args.stiffness if args.stiffness is not None else args.force / args.extension
            joules = elastic(k, args.extension)
            title = "Mechanical - elastic energy in tension or compression"
            detail = f"k = {k:,.0f} N/m, extension {args.extension} m"
        else:  # pragma: no cover - argparse restricts the choices
            p.error(f"unknown model {args.model}")
    except ValueError as e:
        p.error(str(e))
    except ZeroDivisionError:
        p.error("extension must be greater than zero when deriving stiffness from force")

    result = classify(joules)

    if args.json:
        out = dict(result)
        out["model"] = args.model
        if note:
            out["note"] = note
        print(json.dumps(out, indent=2))
        return 0

    print(_fmt(title, result, detail, note))
    print("\nBands: <500 J first-aid | 500-1500 J medical/LTI | >1500 J SIF most likely.")
    print("Low energy does not mean safe. Health hazards are assessed against exposure")
    print("standards, not joules. Decision aid only - not legal advice, and requires")
    print("competent-person validation.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
