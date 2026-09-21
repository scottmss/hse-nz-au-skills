#!/usr/bin/env python3
"""risk_matrix_scorer.py — deterministic 5x5 risk scoring for critical-risk-manager.

Scores a hazard on a generic 5x5 likelihood x consequence matrix, pre-control and
post-control, and applies the critical-consequence override (any credible catastrophic
outcome is surfaced as Critical regardless of a low calculated band).

This is a GENERIC example matrix. Confirm it matches the matrix your assessment is governed
by and substitute the bands if not — see references/critical-risk-definitions.md.

Pure standard library. No network, no file writes, no side effects. Safe to read and run.

Usage:
    # pre-control only
    python3 risk_matrix_scorer.py --likelihood 3 --consequence 5

    # pre- and post-control (shows the risk reduction)
    python3 risk_matrix_scorer.py -l 4 -c 5 --post-likelihood 2 --post-consequence 5

    # machine-readable
    python3 risk_matrix_scorer.py -l 3 -c 5 --json

    # run the built-in self-test
    python3 risk_matrix_scorer.py --selftest

Exit codes: 0 = success / tests passed, 2 = bad input.
"""
from __future__ import annotations

import argparse
import json
import sys

LIKELIHOOD = {
    1: ("Rare", "Only in exceptional circumstances"),
    2: ("Unlikely", "Could occur but not expected"),
    3: ("Possible", "Could occur at some time"),
    4: ("Likely", "Will probably occur"),
    5: ("Almost certain", "Expected to occur in most circumstances"),
}

CONSEQUENCE = {
    1: ("Insignificant", "No / negligible injury"),
    2: ("Minor", "First aid injury"),
    3: ("Moderate", "Medical treatment / lost-time injury"),
    4: ("Major", "Serious injury, hospitalisation, long-term harm"),
    5: ("Catastrophic", "Fatality / permanent disabling injury"),
}

# Upper-bound (inclusive) of each band by score, lowest first.
BANDS = [(4, "Low"), (9, "Medium"), (16, "High"), (25, "Extreme")]

BAND_RESPONSE = {
    "Low": "Manage by routine procedures.",
    "Medium": "Manage with documented controls and monitoring.",
    "High": "Critical controls must be in place, verified, and signed off before work.",
    "Extreme": "Stop / do not proceed without elimination or major control redesign and senior sign-off.",
    "Critical": "Credible fatal outcome: manage as a critical risk regardless of calculated band — "
                "critical controls must be assured and verified before work.",
}


def band_for(score: int) -> str:
    for upper, name in BANDS:
        if score <= upper:
            return name
    return BANDS[-1][1]


def score(likelihood: int, consequence: int) -> dict:
    """Score one likelihood x consequence pair. Applies the critical-consequence override."""
    for value, name in (("likelihood", likelihood), ("consequence", consequence)):
        if name not in (1, 2, 3, 4, 5):
            raise ValueError(f"{value} must be an integer 1-5, got {name!r}")
    raw = likelihood * consequence
    band = band_for(raw)
    critical_override = consequence == 5  # any credible catastrophic outcome
    effective_band = "Critical" if critical_override else band
    return {
        "likelihood": likelihood,
        "likelihood_label": LIKELIHOOD[likelihood][0],
        "consequence": consequence,
        "consequence_label": CONSEQUENCE[consequence][0],
        "score": raw,
        "band": band,
        "critical_consequence_override": critical_override,
        "effective_band": effective_band,
        "response": BAND_RESPONSE[effective_band],
    }


def _fmt(label: str, r: dict) -> str:
    lines = [
        f"{label}:",
        f"  Likelihood : {r['likelihood']} ({r['likelihood_label']})",
        f"  Consequence: {r['consequence']} ({r['consequence_label']})",
        f"  Score      : {r['score']}  ->  band {r['band']}",
    ]
    if r["critical_consequence_override"]:
        lines.append("  Override   : catastrophic consequence -> treated as CRITICAL")
    lines.append(f"  Rating     : {r['effective_band']}")
    lines.append(f"  Response   : {r['response']}")
    return "\n".join(lines)


def _selftest() -> int:
    cases = [
        ((1, 1), 1, "Low", "Low"),
        ((3, 3), 9, "Medium", "Medium"),
        ((4, 4), 16, "High", "High"),
        ((5, 5), 25, "Extreme", "Critical"),
        ((1, 5), 5, "Medium", "Critical"),   # rare x catastrophic -> override fires
        ((5, 1), 5, "Medium", "Medium"),     # almost certain x insignificant -> no override
    ]
    failures = 0
    for (l, c), exp_score, exp_band, exp_eff in cases:
        r = score(l, c)
        ok = r["score"] == exp_score and r["band"] == exp_band and r["effective_band"] == exp_eff
        print(f"  [{'PASS' if ok else 'FAIL'}] L{l} x C{c} -> "
              f"score {r['score']} band {r['band']} rating {r['effective_band']}")
        if not ok:
            failures += 1
    for bad in [(0, 3), (6, 2), (3, 9), ("x", 1)]:
        try:
            score(*bad)  # type: ignore[arg-type]
        except ValueError:
            print(f"  [PASS] rejected bad input {bad}")
        else:
            print(f"  [FAIL] accepted bad input {bad}")
            failures += 1
    print(f"\n{'ALL TESTS PASSED' if failures == 0 else f'{failures} TEST(S) FAILED'}")
    return 0 if failures == 0 else 1


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        description="Deterministic 5x5 risk-matrix scorer (generic example matrix).")
    p.add_argument("-l", "--likelihood", type=int, help="pre-control likelihood 1-5")
    p.add_argument("-c", "--consequence", type=int, help="pre-control consequence 1-5")
    p.add_argument("--post-likelihood", type=int, help="post-control likelihood 1-5")
    p.add_argument("--post-consequence", type=int, help="post-control consequence 1-5")
    p.add_argument("--json", action="store_true", help="machine-readable output")
    p.add_argument("--selftest", action="store_true", help="run built-in tests and exit")
    args = p.parse_args(argv)

    if args.selftest:
        return _selftest()

    if args.likelihood is None or args.consequence is None:
        p.error("--likelihood and --consequence are required (or use --selftest)")

    try:
        pre = score(args.likelihood, args.consequence)
        post = None
        if args.post_likelihood is not None and args.post_consequence is not None:
            post = score(args.post_likelihood, args.post_consequence)
        elif (args.post_likelihood is None) != (args.post_consequence is None):
            p.error("post-control scoring needs BOTH --post-likelihood and --post-consequence")
    except ValueError as e:
        p.error(str(e))

    if args.json:
        out = {"pre_control": pre}
        if post is not None:
            out["post_control"] = post
        print(json.dumps(out, indent=2))
        return 0

    print(_fmt("Pre-control (inherent) risk", pre))
    if post is not None:
        print()
        print(_fmt("Post-control (residual) risk", post))
    print("\nGeneric example matrix — confirm it matches the matrix governing this assessment.")
    print("Not legal advice; requires competent-person validation.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
