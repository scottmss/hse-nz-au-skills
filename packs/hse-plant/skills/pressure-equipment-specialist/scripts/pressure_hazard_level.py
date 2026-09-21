#!/usr/bin/env python3
"""pressure_hazard_level.py — deterministic pressure-equipment pV / hazard-level helper.

Pressure equipment is classified by HAZARD LEVEL (AS 4343 — levels A highest to E lowest),
which drives design verification, registration and in-service inspection. The classification is
built on the **pV product** (design pressure x volume) and a content factor Fc:

    pV (MPa.L) = design_pressure[MPa] x volume[L]
    hazard figure = pV x Fc        (Fc = 0.1 vacuum, 1 liquid, 10 gas/vapour)

This tool does that arithmetic (with unit handling) and reports the pV, the Fc-weighted figure,
and an indicative stored (pressure-volume) energy. It does NOT assign the A-E level itself:
**AS 4343 (and harmfulness/special factors) and a competent person GOVERN** the actual level and
whether design verification + registration + inspection apply.

Reference example (from AS 4343 commentary): an industrial **gas** air-receiver of ~1250 L at
800 kPa gives pV = 1000 MPa.L, hazard figure 10000 — about **Hazard Level B**, which triggers
design and plant registration in AU. Use that only as a sanity check.

This is a planning aid, NOT a substitute for AS 4343, AS/NZS 1200, the jurisdiction's regs
(NZ PECPR / AU plant registration) or a competent person. Confirm every figure before relying on it.

Pure standard library. No network, no file writes, no side effects. Safe to read and run.

Usage:
    # 1250 L gas air-receiver at 800 kPa
    python3 pressure_hazard_level.py --pressure-kpa 800 --volume-l 1250 --contents gas

    # a liquid vessel, pressure given in MPa
    python3 pressure_hazard_level.py --pressure-mpa 2.5 --volume-l 500 --contents liquid

    python3 pressure_hazard_level.py --self-test
"""
from __future__ import annotations

import argparse
import sys

FC = {"vacuum": 0.1, "liquid": 1.0, "gas": 10.0}


def hazard_figures(design_pressure_mpa: float, volume_l: float, contents: str) -> dict:
    """Compute pV (MPa.L), the Fc-weighted hazard figure, and the pV energy (kJ)."""
    if design_pressure_mpa <= 0 or volume_l <= 0:
        raise ValueError("design pressure and volume must be positive")
    if contents not in FC:
        raise ValueError(f"contents must be one of {sorted(FC)}")
    fc = FC[contents]
    pv = design_pressure_mpa * volume_l                       # MPa.L
    figure = pv * fc                                          # Fc-weighted (AS 4343 input)
    # pressure-volume energy: p[Pa] x V[m3] = J ; = (MPa*1e6) * (L/1000) = MPa*L*1000 J
    energy_kj = pv * 1000.0 / 1000.0                          # == pv (MPa.L) in kJ
    return {
        "design_pressure_mpa": round(design_pressure_mpa, 4),
        "volume_l": round(volume_l, 2),
        "contents": contents,
        "fc": fc,
        "pv_mpa_l": round(pv, 2),
        "hazard_figure": round(figure, 2),
        "pv_energy_kj": round(energy_kj, 1),
    }


def _fmt(r: dict) -> str:
    return "\n".join([
        f"Design pressure: {r['design_pressure_mpa']} MPa   Volume: {r['volume_l']} L   "
        f"Contents: {r['contents']} (Fc={r['fc']})",
        f"pV = {r['pv_mpa_l']} MPa.L",
        f"Hazard figure (pV x Fc) = {r['hazard_figure']}",
        f"Indicative stored (pV) energy = {r['pv_energy_kj']} kJ",
        "",
        "Read the HAZARD LEVEL (A-E) from AS 4343 using these inputs — higher figure = higher",
        "hazard = more likely to need design verification + registration + in-service inspection.",
        "Harmfulness of the fluid and special factors also apply. AS 4343, AS/NZS 1200, the",
        "jurisdiction's regs (NZ PECPR / AU plant registration) and a competent person GOVERN.",
    ])


def _self_test() -> int:
    # canonical example: 1250 L gas @ 800 kPa -> pV 1000, figure 10000
    r = hazard_figures(0.8, 1250, "gas")
    assert r["pv_mpa_l"] == 1000.0, r
    assert r["hazard_figure"] == 10000.0, r
    assert r["pv_energy_kj"] == 1000.0, r
    # liquid factor 1
    r = hazard_figures(2.5, 500, "liquid")
    assert r["pv_mpa_l"] == 1250.0 and r["hazard_figure"] == 1250.0, r
    # vacuum factor 0.1
    r = hazard_figures(0.1, 1000, "vacuum")
    assert abs(r["hazard_figure"] - 10.0) < 1e-9, r
    # validation
    for bad in (lambda: hazard_figures(0, 100, "gas"),
                lambda: hazard_figures(1, 0, "gas"),
                lambda: hazard_figures(1, 100, "plasma")):
        try:
            bad()
        except ValueError:
            pass
        else:
            raise AssertionError("expected ValueError")
    print("pressure_hazard_level: all self-tests passed")
    return 0


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Pressure-equipment pV / hazard-level helper (AS 4343 input).")
    g = p.add_mutually_exclusive_group()
    g.add_argument("--pressure-mpa", type=float, help="design pressure in MPa")
    g.add_argument("--pressure-kpa", type=float, help="design pressure in kPa")
    p.add_argument("--volume-l", type=float, help="volume in litres")
    p.add_argument("--contents", choices=sorted(FC), help="fluid contents (sets Fc)")
    p.add_argument("--self-test", action="store_true", help="run built-in checks and exit")
    args = p.parse_args(argv)

    if args.self_test:
        return _self_test()

    if args.pressure_mpa is not None:
        pressure_mpa = args.pressure_mpa
    elif args.pressure_kpa is not None:
        pressure_mpa = args.pressure_kpa / 1000.0
    else:
        pressure_mpa = None
    if pressure_mpa is None or args.volume_l is None or args.contents is None:
        p.print_help()
        return 2

    print(_fmt(hazard_figures(pressure_mpa, args.volume_l, args.contents)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
