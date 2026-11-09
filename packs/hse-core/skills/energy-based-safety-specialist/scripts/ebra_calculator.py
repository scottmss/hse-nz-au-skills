#!/usr/bin/env python3
"""ebra_calculator.py - deterministic Risk Remaining (RR) and EBRA scoring.

Implements the CSRA Risk Remaining model and Energy-Based Risk Assessment (EBRA) described in
references/rr-ebra.md, and reports the HECA score alongside so the three are never confused.

For each high-energy hazard you give the control configuration, the exposure duration and the
number of workers exposed. The tool:

  1. resolves the control configuration to a Risk Remaining value
         DC-E  direct control that eliminates the exposure           ~0%
         DC-M  direct control that mitigates / isolates it            5%
         ACS1  physical obstacle + dedicated monitoring              20%
         ACS2  physical obstacle + visual reminder                   30%
         ACS3  visual reminder + dedicated monitoring                30%
         PO or DM on its own                                         45%
         VR on its own                                               67%
         no qualifying control                                      100%
  2. multiplies RR x duration (full 1.0 / part 0.5 / momentary 0.1) x workers exposed
  3. sums the hazard contributions into the EBRA total and ranks what is driving it
  4. computes HECA (direct control = success, anything else = exposure)

IMPORTANT LIMITS - read before relying on a number:
  * RR values are expert-consensus relative weights (CSRA Delphi panel), NOT probabilities of
    a serious injury or fatality. EBRA is a relative index with no units.
  * An alternative control system only counts if all five CSRA rules are met (direct control
    not feasible; two controls from different categories; each targeted at the hazard; specialty
    training + safe work plan + quality pre-job brief; in place for the whole exposure). This tool
    cannot check that - it takes your word, and says so in the output.
  * Cases the source does not settle are scored by this skill's stated conventions (see
    references/rr-ebra.md) and flagged in the findings.
  * A low EBRA total never shows a duty has been met. Any hazard at 100% is a stop-work finding
    whatever the total.

Pure standard library. No network, no file writes, no side effects. Reads a JSON file only if
you pass --file. Safe to read and run.

Usage:
    # Risk Remaining for one control set
    python3 ebra_calculator.py --rr po+vr

    # a task, one --hazard per high-energy hazard: NAME CONTROLS DURATION WORKERS
    python3 ebra_calculator.py --task "Water main renewal" \\
        --hazard "Trench collapse" dc-m part 2 \\
        --hazard "Excavator slew - workers on foot" po+dm part 3 \\
        --hazard "Live traffic - workers at trench edge" po+vr full 2 \\
        --hazard "Pipe on excavator - drop zone" none momentary 1

    # the same from a JSON file (allows per-hazard rule flags)
    python3 ebra_calculator.py --file hazards.json
        {"task": "...", "hazards": [
            {"name": "...", "controls": "po+dm", "duration": "part", "workers": 3,
             "acs_rules_met": true, "dc_feasible": false}]}

    # machine-readable
    python3 ebra_calculator.py --file hazards.json --json

    # built-in self-test against the published CSRA worked examples
    python3 ebra_calculator.py --selftest

Controls: dc-e, dc-m, po, dm, vr, none - combine with '+', e.g. po+dm. Aliases: acs1 = po+dm,
acs2 = po+vr, acs3 = vr+dm. Duration: full | part | momentary (or 1.0 | 0.5 | 0.1).

Exit codes: 0 = success / tests passed, 1 = self-test failure, 2 = bad input.
"""
from __future__ import annotations

import argparse
import json
import sys

RR = {
    "DC-E": 0.00,
    "DC-M": 0.05,
    "ACS1": 0.20,
    "ACS2": 0.30,
    "ACS3": 0.30,
    "PO": 0.45,
    "DM": 0.45,
    "VR": 0.67,
    "NONE": 1.00,
}

LABEL = {
    "DC-E": "DC-E (direct - eliminates)",
    "DC-M": "DC-M (direct - mitigates)",
    "ACS1": "ACS1 (PO + DM)",
    "ACS2": "ACS2 (PO + VR)",
    "ACS3": "ACS3 (VR + DM)",
    "PO": "single PO",
    "DM": "single DM",
    "VR": "single VR",
    "NONE": "no qualifying control",
}

DURATION = {"full": 1.0, "part": 0.5, "momentary": 0.1}

TOKENS = {
    "dc-e": "dc-e", "dce": "dc-e", "dc_e": "dc-e",
    "dc-m": "dc-m", "dcm": "dc-m", "dc_m": "dc-m",
    "po": "po", "dm": "dm", "vr": "vr", "none": "none",
}
ALIASES = {"acs1": ("po", "dm"), "acs2": ("po", "vr"), "acs3": ("vr", "dm")}

NOT_PROBABILITY = "Relative index - not a probability of a serious injury or fatality."


class InputError(ValueError):
    pass


def parse_controls(spec) -> set:
    """Turn 'po+dm', 'acs1', ['po','vr'] etc. into a set of canonical tokens."""
    if isinstance(spec, (list, tuple)):
        parts = [str(p) for p in spec]
    else:
        parts = str(spec).replace(",", "+").split("+")
    out = set()
    for raw in parts:
        t = raw.strip().lower()
        if not t:
            continue
        if t in ALIASES:
            out.update(ALIASES[t])
        elif t in TOKENS:
            out.add(TOKENS[t])
        else:
            raise InputError(
                f"unknown control '{raw}'. Use dc-e, dc-m, po, dm, vr, none, or acs1/acs2/acs3.")
    if not out:
        raise InputError("no controls given - use 'none' if nothing qualifies.")
    if "none" in out and len(out) > 1:
        raise InputError("'none' cannot be combined with other controls.")
    return out


def parse_duration(value) -> float:
    if isinstance(value, str):
        key = value.strip().lower()
        if key in DURATION:
            return DURATION[key]
        try:
            value = float(key)
        except ValueError:
            raise InputError(f"duration '{value}' - use full, part or momentary.") from None
    for d in DURATION.values():
        if abs(float(value) - d) < 1e-9:
            return d
    raise InputError(
        f"duration {value} is not a standard category. EBRA uses full = 1.0, part = 0.5, "
        "momentary = 0.1 so that assessments stay comparable.")


def parse_workers(value) -> int:
    try:
        w = int(value)
    except (TypeError, ValueError):
        raise InputError(f"workers '{value}' must be a whole number.") from None
    if w < 0 or float(value) != w:
        raise InputError(f"workers '{value}' must be a whole number of 0 or more.")
    return w


def resolve(controls: set, acs_rules_met: bool = True, dc_feasible: bool = False) -> dict:
    """Walk the CSRA Risk Remaining decision order. Returns the configuration and notes."""
    notes = []
    if "dc-e" in controls:
        return {"config": "DC-E", "notes": notes}
    if "dc-m" in controls:
        return {"config": "DC-M", "notes": notes}

    qualifying = controls & {"po", "dm", "vr"}
    if len(qualifying) >= 2:
        if dc_feasible:
            notes.append("ACS rule 1 not met: a direct control is feasible, so this is not an "
                         "acceptable alternative control system. The finding is the missing "
                         "direct control. Scored as the strongest single control (skill convention).")
        elif not acs_rules_met:
            notes.append("ACS rules not all met, so this is not an alternative control system. "
                         "Scored as the strongest single control (skill convention).")
        else:
            if {"po", "dm"} <= qualifying:
                if len(qualifying) == 3:
                    notes.append("PO + DM + VR present: scored as ACS1. CSRA gives no further "
                                 "credit for a third control (skill convention).")
                return {"config": "ACS1", "notes": notes}
            if {"po", "vr"} <= qualifying:
                return {"config": "ACS2", "notes": notes}
            return {"config": "ACS3", "notes": notes}

    if "po" in qualifying:
        return {"config": "PO", "notes": notes}
    if "dm" in qualifying:
        return {"config": "DM", "notes": notes}
    if "vr" in qualifying:
        return {"config": "VR", "notes": notes}
    return {"config": "NONE", "notes": notes}


def assess(hazards: list, task: str = "") -> dict:
    if not hazards:
        raise InputError("no high-energy hazards given. If none were identified, there is "
                         "nothing to score - do not record a zero.")
    rows = []
    for i, h in enumerate(hazards, 1):
        name = str(h.get("name") or f"Hazard {i}")
        controls = parse_controls(h.get("controls", "none"))
        d = parse_duration(h.get("duration", ""))
        w = parse_workers(h.get("workers"))
        rules_given = "acs_rules_met" in h
        r = resolve(controls, bool(h.get("acs_rules_met", True)), bool(h.get("dc_feasible", False)))
        cfg = r["config"]
        rr = RR[cfg]
        notes = list(r["notes"])
        if cfg in ("ACS1", "ACS2", "ACS3") and not rules_given:
            notes.append("ACS rules assumed met - confirm all five (references/rr-ebra.md).")
        if cfg == "NONE" and w > 0:
            notes.append("No qualifying control (RR 100%): stop-work finding whatever the total.")
        elif cfg == "NONE":
            notes.append("No qualifying control and nobody recorded as exposed - check what "
                         "actually keeps people out. If it is only an instruction, W is not 0.")
        if w == 0:
            notes.append("Nobody exposed (W = 0): contributes nothing, but the hazard and its "
                         "control still count for HECA.")
        rows.append({
            "name": name,
            "controls": sorted(controls),
            "config": cfg,
            "config_label": LABEL[cfg],
            "rr": rr,
            "duration": d,
            "workers": w,
            "contribution": round(rr * d * w, 6),
            "heca": "success" if cfg in ("DC-E", "DC-M") else "exposure",
            "notes": notes,
        })

    total = round(sum(r["contribution"] for r in rows), 6)
    for r in rows:
        r["share"] = round(r["contribution"] / total, 4) if total > 0 else None

    successes = sum(1 for r in rows if r["heca"] == "success")
    heca = round(100.0 * successes / len(rows), 1)
    drivers = sorted((r for r in rows if r["contribution"] > 0),
                     key=lambda r: r["contribution"], reverse=True)
    return {
        "task": task,
        "hazards": rows,
        "ebra_total": total,
        "heca": {"successes": successes, "hazards": len(rows), "percent": heca},
        "drivers": [r["name"] for r in drivers],
        "note": NOT_PROBABILITY,
    }


def _driver_reason(r: dict) -> str:
    bits = []
    if r["rr"] >= 1.0:
        bits.append("no qualifying control")
    elif r["rr"] >= 0.45:
        bits.append("single alternate control only")
    elif r["rr"] >= 0.20:
        bits.append("alternative controls only")
    if r["duration"] == 1.0:
        bits.append("full-shift exposure")
    if r["workers"] >= 3:
        bits.append(f"{r['workers']} workers exposed")
    return ", ".join(bits) or "combination of control, time and headcount"


def _clip(text: str, width: int) -> str:
    return text if len(text) <= width else text[:width - 1] + "~"


def render(result: dict) -> str:
    out = []
    title = "Energy-Based Risk Assessment"
    if result["task"]:
        title += f" - {result['task']}"
    out.append(title)
    out.append("=" * len(title))
    hdr = f"{'#':>2}  {'Hazard':<42} {'Control configuration':<27} {'RR':>5} {'D':>4} {'W':>3} " \
          f"{'RRxDxW':>7} {'Share':>6}  HECA"
    out.append(hdr)
    out.append("-" * len(hdr))
    for i, r in enumerate(result["hazards"], 1):
        share = f"{r['share'] * 100:.0f}%" if r["share"] is not None else "-"
        rr = f"{r['rr'] * 100:.0f}%"
        out.append(f"{i:>2}  {_clip(r['name'], 42):<42} {r['config_label']:<27} {rr:>5} "
                   f"{r['duration']:>4} {r['workers']:>3} {r['contribution']:>7.3f} {share:>6}  "
                   f"{r['heca']}")
    out.append("")
    out.append(f"EBRA total: {result['ebra_total']:.3f}   ({result['note']})")
    h = result["heca"]
    out.append(f"HECA: {h['successes']} success / {h['hazards']} high-energy hazards = "
               f"{h['percent']:.1f}%")
    rows = {r["name"]: r for r in result["hazards"]}
    if result["drivers"]:
        out.append("")
        out.append("Largest contributors:")
        for name in result["drivers"][:3]:
            r = rows[name]
            out.append(f"  - {name}: {r['contribution']:.3f} ({r['share'] * 100:.0f}%) - "
                       f"{_driver_reason(r)}")
    findings = [(r["name"], n) for r in result["hazards"] for n in r["notes"]]
    if findings:
        out.append("")
        out.append("Findings and assumptions:")
        for name, n in findings:
            out.append(f"  - {name}: {n}")
    out.append("")
    out.append("Draft decision aid - a competent person must confirm every hazard, control "
               "classification, duration and headcount.")
    return "\n".join(out)


def selftest() -> int:
    failures = []

    def check(label, got, want, tol=1e-9):
        if abs(got - want) > tol:
            failures.append(f"{label}: got {got}, want {want}")

    # CSRA EBRA report 2026, Appendix 2 scenario 1 - steel erection.
    s1 = assess([
        {"name": "Suspended load", "controls": "dc-e", "duration": "part", "workers": 0},
        {"name": "Fall from elevation", "controls": "dc-m", "duration": "part", "workers": 1},
    ])
    check("scenario 1 EBRA", s1["ebra_total"], 0.025)
    check("scenario 1 HECA", s1["heca"]["percent"], 100.0)

    # Appendix 2 scenario 2 - industrial construction and maintenance.
    s2 = assess([
        {"name": "Suspended load", "controls": "dc-e", "duration": "part", "workers": 0},
        {"name": "Fall from elevation", "controls": "dc-m", "duration": "full", "workers": 2},
        {"name": "Mobile equipment", "controls": "acs1", "duration": "part", "workers": 2,
         "acs_rules_met": True},
        {"name": "Trench", "controls": "po+vr", "duration": "part", "workers": 2,
         "acs_rules_met": True},
        {"name": "Electrical contact", "controls": "po", "duration": "momentary", "workers": 1},
        {"name": "Rotating equipment", "controls": "none", "duration": "momentary", "workers": 1},
    ])
    check("scenario 2 EBRA", s2["ebra_total"], 0.745)
    check("scenario 2 HECA", s2["heca"]["percent"], 33.3)
    if s2["drivers"][0] != "Trench":
        failures.append(f"scenario 2 top driver: got {s2['drivers'][0]}, want Trench")

    # Section 7 example - steel erection with an ACS1 exclusion zone.
    s3 = assess([
        {"name": "Working at height", "controls": "dc-m", "duration": 0.5, "workers": 1},
        {"name": "Suspended load falling", "controls": "acs1", "duration": 0.1, "workers": 1},
        {"name": "Lateral movement of load", "controls": "acs1", "duration": 0.1, "workers": 1},
        {"name": "Mobile equipment", "controls": "acs1", "duration": 0.5, "workers": 3},
    ])
    check("section 7 EBRA", s3["ebra_total"], 0.365)
    check("section 7 HECA", s3["heca"]["percent"], 25.0)

    # Decision order and skill conventions.
    cases = [
        ("po+dm", True, False, "ACS1"),
        ("vr+dm", True, False, "ACS3"),
        ("po+dm+vr", True, False, "ACS1"),
        ("dc-m+po+dm", True, False, "DC-M"),
        ("po+dm", False, False, "PO"),     # rules not met -> strongest single
        ("po+vr", True, True, "PO"),       # DC feasible -> not an ACS
        ("vr+dm", False, False, "DM"),
        ("vr", True, False, "VR"),
        ("none", True, False, "NONE"),
    ]
    for spec, rules, feasible, want in cases:
        got = resolve(parse_controls(spec), rules, feasible)["config"]
        if got != want:
            failures.append(f"resolve({spec}, rules={rules}, dc_feasible={feasible}): "
                            f"got {got}, want {want}")

    # Single-control values reproduce the ACS values as products (CSRA derived them jointly).
    check("PO x DM ~ ACS1", round(RR["PO"] * RR["DM"], 2), RR["ACS1"], tol=0.005)
    check("PO x VR ~ ACS2", round(RR["PO"] * RR["VR"], 2), RR["ACS2"], tol=0.005)

    # Bad input is rejected, not guessed.
    for bad in (lambda: parse_duration("half"), lambda: parse_duration(0.25),
                lambda: parse_controls("po+none"), lambda: parse_controls("harness"),
                lambda: parse_workers(-1), lambda: assess([])):
        try:
            bad()
            failures.append("bad input accepted")
        except InputError:
            pass

    if failures:
        print("SELF-TEST FAILED")
        for f in failures:
            print("  - " + f)
        return 1
    print("Self-test passed: CSRA worked examples reproduced (0.025, 0.745, 0.365), "
          "decision order and conventions hold.")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="Risk Remaining (RR) and Energy-Based Risk Assessment (EBRA) calculator.",
        epilog=NOT_PROBABILITY)
    src = p.add_mutually_exclusive_group()
    src.add_argument("--hazard", nargs=4, action="append",
                     metavar=("NAME", "CONTROLS", "DURATION", "WORKERS"),
                     help="one high-energy hazard; repeat for each (ACS rules assumed met)")
    src.add_argument("--file", help="JSON file with a 'hazards' list (see --help in source)")
    src.add_argument("--rr", metavar="CONTROLS", help="just give the Risk Remaining for a control set")
    src.add_argument("--selftest", action="store_true", help="run the built-in worked examples")
    p.add_argument("--task", default="", help="task or activity name for the report header")
    p.add_argument("--json", action="store_true", help="machine-readable output")
    return p


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    if args.selftest:
        return selftest()
    try:
        if args.rr:
            r = resolve(parse_controls(args.rr))
            res = {"controls": args.rr, "config": r["config"], "config_label": LABEL[r["config"]],
                   "rr": RR[r["config"]], "notes": r["notes"], "note": NOT_PROBABILITY}
            if args.json:
                print(json.dumps(res, indent=2))
            else:
                print(f"{res['config_label']}: Risk Remaining {res['rr'] * 100:.0f}%  "
                      f"({NOT_PROBABILITY})")
                if r["config"].startswith("ACS"):
                    print("Counts only if all five alternative-control-system rules are met.")
            return 0
        if args.file:
            with open(args.file, encoding="utf-8") as fh:
                data = json.load(fh)
            hazards = data.get("hazards", []) if isinstance(data, dict) else data
            task = args.task or (data.get("task", "") if isinstance(data, dict) else "")
        elif args.hazard:
            hazards = [{"name": n, "controls": c, "duration": d, "workers": w}
                       for n, c, d, w in args.hazard]
            task = args.task
        else:
            build_parser().print_help()
            return 2
        result = assess(hazards, task)
    except (InputError, OSError, json.JSONDecodeError) as e:
        print(f"error: {e}", file=sys.stderr)
        return 2
    print(json.dumps(result, indent=2) if args.json else render(result))
    return 0


if __name__ == "__main__":
    sys.exit(main())
