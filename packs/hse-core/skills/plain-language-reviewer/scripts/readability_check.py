#!/usr/bin/env python3
"""readability_check.py - deterministic plain-language linting for H&S documents.

Runs the mechanical half of a plain-language review so attention goes to the judgement
calls. Reports sentence length, a readability estimate, passive voice, unexplained
acronyms, complex words with plainer alternatives, contractions, shouting capitals,
nominalisations, and - most importantly - VAGUE WORDS that usually mean a control has
not actually been decided.

WHAT THIS IS NOT:
  * Not a compliance test. No NZ or AU law prescribes a reading level, a sentence length
    or a readability score, and no score discharges any duty. The thresholds below are
    this tool's own conventions, not a regulator's.
  * Not a substitute for testing with workers. Readability formulas were built for US
    school texts and know nothing about your workforce, your jargon or your diagrams.
    The real test is demonstration or thinking-aloud - see
    references/comprehension-testing.md.
  * Not an accuracy check. A document can score perfectly and still be wrong. Accuracy
    outranks readability every time.

The VAGUE WORDS check is the one worth acting on first. "Wear appropriate PPE" and
"inspect regularly" are not writing problems - they are missing controls wearing a
sentence.

Pure standard library. No network, no file writes, no side effects. Safe to read and run.

Usage:
    python3 readability_check.py procedure.md
    cat draft.txt | python3 readability_check.py
    python3 readability_check.py policy.txt --json
    python3 readability_check.py policy.txt --max-sentence 20
    python3 readability_check.py --selftest

Exit codes: 0 = success / tests passed, 1 = self-test failure, 2 = bad input.
"""
from __future__ import annotations

import argparse
import json
import re
import sys

DEFAULT_MAX_SENTENCE = 25

# --- word lists ------------------------------------------------------------------

# Complex phrase -> plainer alternative. Longest phrases are matched first.
SUBSTITUTIONS = {
    "at this point in time": "now",
    "at the present time": "now",
    "in the event that": "if",
    "in the event of": "if",
    "due to the fact that": "because",
    "owing to the fact that": "because",
    "in the vicinity of": "near",
    "in close proximity to": "near",
    "provide assistance to": "help",
    "give consideration to": "consider",
    "conduct an assessment of": "assess",
    "make an application": "apply",
    "in accordance with": "under",
    "on a regular basis": "regularly (say how often)",
    "a sufficient number of": "enough",
    "a large proportion of": "most",
    "in a safe manner": "safely",
    "prior to": "before",
    "in advance of": "before",
    "subsequent to": "after",
    "in order to": "to",
    "in the absence of": "without",
    "with regard to": "about",
    "in respect of": "about",
    "ensure that you": "make sure you",
    "terminate employment": "dismiss",
    "participate in": "take part in",
    "at all times": "always",
    "adjacent to": "next to",
    "commence": "start",
    "commencement": "start",
    "cease": "stop",
    "terminate": "end",
    "utilise": "use",
    "utilisation": "use",
    "endeavour": "try",
    "ascertain": "find out",
    "facilitate": "help",
    "implement": "carry out",
    "approximately": "about",
    "additional": "extra",
    "demonstrate": "show",
    "purchase": "buy",
    "obtain": "get",
    "retain": "keep",
    "notify": "tell",
    "assist": "help",
    "shall": "must",
}

# Vague words that usually hide an undecided control -> the question they dodge.
VAGUE = {
    "appropriate": "Which one, exactly? Name the item, class or rating.",
    "suitable": "Suitable by what standard? Name it.",
    "adequate": "Adequate measured how?",
    "as necessary": "Decided by whom, on what basis?",
    "where required": "Required by what, and when?",
    "if practicable": "If it is practicable here, say so. If not, say what happens instead.",
    "where possible": "If it is possible here, say so.",
    "wherever practicable": "Decide it now, in the document.",
    "be careful": "Do what, specifically?",
    "take care": "Do what, specifically?",
    "exercise caution": "Do what, specifically?",
    "regularly": "How often? Give an interval.",
    "periodically": "How often? Give an interval.",
    "from time to time": "How often? Give an interval.",
    "competent person": "Competent in what, evidenced how?",
    "authorised person": "Authorised by whom, recorded where?",
    "relevant ppe": "Which items, to which standard?",
    "correct ppe": "Which items, to which standard?",
    "appropriate ppe": "Which items, to which standard?",
    "safe distance": "How far?",
    "safe manner": "Doing what, specifically?",
    "ensure safety": "This is what the rest of the document is meant to answer.",
    "good practice": "Whose good practice? Cite the document.",
    "as soon as possible": "By when?",
}

CONTRACTIONS = re.compile(
    r"\b(?:don't|doesn't|didn't|can't|won't|shouldn't|couldn't|wouldn't|isn't|aren't|"
    r"wasn't|weren't|hasn't|haven't|hadn't|it's|you're|we're|they're|there's|that's|"
    r"you'll|we'll|they'll|you've|we've|they've|mustn't|needn't)\b",
    re.IGNORECASE,
)

BE_FORMS = r"(?:is|are|was|were|be|been|being|am)"
# Passive candidate: a form of "be" followed (optionally via an adverb) by a past participle.
PASSIVE = re.compile(
    rf"\b{BE_FORMS}\b(?:\s+\w+ly)?\s+(\w+(?:ed|en|own|ought|aid|ade|old|eld))\b",
    re.IGNORECASE,
)
# Common adjectives that end in -ed and are not passives.
PASSIVE_EXCEPTIONS = {
    "red", "bed", "led", "shed", "need", "speed", "feed", "seed", "indeed", "aged",
    "used", "based", "located", "limited", "related", "required",
}

NOMINALISATION = re.compile(r"\b\w{5,}(?:tion|ment|ance|ence|ility|isation|ization)s?\b",
                            re.IGNORECASE)
# Nominalisations that are the normal name for the thing, not bureaucratic padding.
NOMINALISATION_OK = {
    "information", "instruction", "instructions", "equipment", "regulation", "regulations",
    "ventilation", "insulation", "protection", "construction", "maintenance", "distance",
    "substance", "substances", "emergency", "documentation", "certification", "isolation",
    "contamination", "vibration", "radiation", "combustion", "attachment", "compartment",
    "department", "environment", "government", "management", "measurement", "section",
    "position", "condition", "conditions", "direction", "directions", "operation",
    "operations", "inspection", "inspections", "station", "solution", "connection",
    "friction", "function", "reaction", "respiration", "suffocation", "evacuation",
}

ACRONYM = re.compile(r"\b([A-Z]{2,6})\b")
# Acronyms so embedded in NZ/AU work that expansion is noise rather than help.
ACRONYM_ALLOWED = {
    "NZ", "AU", "UK", "US", "PDF", "OK", "AM", "PM", "ID", "TV", "CD", "DVD", "MP3",
}
ALLCAPS_RUN = re.compile(r"\b(?:[A-Z]{2,}[^\w\n]+){3,}[A-Z]{2,}\b")

SENTENCE_SPLIT = re.compile(r"(?<=[.!?])[\s\n]+")
WORD = re.compile(r"[A-Za-z][A-Za-z'-]*")


# --- text preparation ------------------------------------------------------------

def strip_markup(text: str) -> str:
    """Remove fenced code blocks, markdown table rows, headings markers and list bullets.

    Tables and code are not prose and would skew the sentence statistics badly.
    """
    text = re.sub(r"```.*?```", " ", text, flags=re.DOTALL)
    text = re.sub(r"`[^`]*`", " ", text)
    lines = []
    for ln in text.split("\n"):
        stripped = ln.strip()
        if stripped.startswith("|") or re.match(r"^[|\s:-]+$", stripped):
            continue          # markdown table row or separator
        stripped = re.sub(r"^#{1,6}\s*", "", stripped)
        stripped = re.sub(r"^[-*+]\s+", "", stripped)
        stripped = re.sub(r"^\d+[.)]\s+", "", stripped)
        lines.append(stripped)
    return "\n".join(lines)


def sentences(text: str) -> list[str]:
    out = []
    for block in text.split("\n"):
        block = block.strip()
        if not block:
            continue
        for s in SENTENCE_SPLIT.split(block):
            s = s.strip()
            if WORD.search(s):
                out.append(s)
    return out


def words(text: str) -> list[str]:
    return WORD.findall(text)


def syllables(word: str) -> int:
    """Heuristic syllable count. Good enough for a readability estimate, no more."""
    w = word.lower().strip("'-")
    if not w:
        return 0
    if len(w) <= 3:
        return 1
    w = re.sub(r"(?:[^laeiouy]es|[^laeiouy]e)$", "", w)
    w = re.sub(r"^y", "", w)
    count = len(re.findall(r"[aeiouy]{1,2}", w))
    return max(count, 1)


# --- checks ----------------------------------------------------------------------

def find_long_sentences(sents: list[str], limit: int) -> list[dict]:
    out = []
    for i, s in enumerate(sents, 1):
        n = len(words(s))
        if n > limit:
            out.append({"sentence_no": i, "words": n, "text": _clip(s)})
    return sorted(out, key=lambda d: -d["words"])


def find_terms(text: str, table: dict) -> list[dict]:
    """Match the longest phrases first so 'in order to' isn't reported as 'order'."""
    lowered = text.lower()
    claimed = [False] * len(lowered)
    hits = []
    for phrase in sorted(table, key=len, reverse=True):
        for m in re.finditer(rf"\b{re.escape(phrase)}\b", lowered):
            if any(claimed[m.start():m.end()]):
                continue
            for j in range(m.start(), m.end()):
                claimed[j] = True
            hits.append({"found": phrase, "advice": table[phrase], "at": m.start()})
    return sorted(hits, key=lambda d: d["at"])


def find_passive(sents: list[str]) -> list[dict]:
    out = []
    for i, s in enumerate(sents, 1):
        for m in PASSIVE.finditer(s):
            if m.group(1).lower() in PASSIVE_EXCEPTIONS:
                continue
            out.append({"sentence_no": i, "found": m.group(0).strip(), "text": _clip(s)})
    return out


def find_unexplained_acronyms(text: str) -> list[str]:
    """An acronym is explained if it appears in brackets right after words, e.g. '... (PPE)'."""
    explained = set(re.findall(r"\(([A-Z]{2,6})\)", text))
    seen, out = set(), []
    for m in ACRONYM.finditer(text):
        a = m.group(1)
        if a in ACRONYM_ALLOWED or a in explained or a in seen:
            continue
        seen.add(a)
        out.append(a)
    return out


def find_nominalisations(text: str) -> list[str]:
    seen, out = set(), []
    for m in NOMINALISATION.finditer(text):
        w = m.group(0).lower()
        if w in NOMINALISATION_OK or w in seen:
            continue
        seen.add(w)
        out.append(w)
    return out


def _clip(s: str, n: int = 90) -> str:
    s = " ".join(s.split())
    return s if len(s) <= n else s[: n - 1] + "…"


def flesch(word_count: int, sentence_count: int, syllable_count: int) -> dict:
    if not word_count or not sentence_count:
        return {"reading_ease": None, "grade": None, "band": "not enough text"}
    wps = word_count / sentence_count
    spw = syllable_count / word_count
    ease = 206.835 - 1.015 * wps - 84.6 * spw
    grade = 0.39 * wps + 11.8 * spw - 15.59
    if ease >= 70:
        band = "plain - most workers should manage this"
    elif ease >= 60:
        band = "fair - workable, but tighten the long sentences"
    elif ease >= 50:
        band = "hard - rewrite before issuing to a mixed-literacy workforce"
    else:
        band = "very hard - rebuild it"
    return {"reading_ease": round(ease, 1), "grade": round(grade, 1), "band": band}


def analyse(text: str, max_sentence: int = DEFAULT_MAX_SENTENCE) -> dict:
    clean = strip_markup(text)
    sents = sentences(clean)
    ws = words(clean)
    syl = sum(syllables(w) for w in ws)
    long_sents = find_long_sentences(sents, max_sentence)

    return {
        "counts": {
            "words": len(ws),
            "sentences": len(sents),
            "average_sentence_words": round(len(ws) / len(sents), 1) if sents else 0,
            "long_sentences": len(long_sents),
            "long_sentence_pct": round(100 * len(long_sents) / len(sents), 1) if sents else 0,
            "max_sentence_words": max((d["words"] for d in long_sents), default=
                                      max((len(words(s)) for s in sents), default=0)),
        },
        "readability": flesch(len(ws), len(sents), syl),
        "long_sentences": long_sents[:10],
        "vague_words": find_terms(clean, VAGUE),
        "complex_words": find_terms(clean, SUBSTITUTIONS),
        "passive_voice": find_passive(sents)[:15],
        "unexplained_acronyms": find_unexplained_acronyms(clean),
        "contractions": sorted({m.group(0).lower() for m in CONTRACTIONS.finditer(clean)}),
        "shouting_capitals": [_clip(m.group(0), 50) for m in ALLCAPS_RUN.finditer(clean)][:5],
        "nominalisations": find_nominalisations(clean)[:15],
        "settings": {"max_sentence_words": max_sentence},
    }


# --- reporting -------------------------------------------------------------------

def report(r: dict) -> str:
    c, out = r["counts"], []
    out.append("Plain-language check")
    out.append("=" * 20)
    out.append("")
    out.append(f"  Words {c['words']:,}   Sentences {c['sentences']:,}   "
               f"Average sentence {c['average_sentence_words']} words")
    rd = r["readability"]
    if rd["reading_ease"] is not None:
        out.append(f"  Reading ease {rd['reading_ease']}  (approx. school grade {rd['grade']})")
        out.append(f"  -> {rd['band']}")
    out.append("")

    if r["vague_words"]:
        out.append(f"VAGUE WORDS - {len(r['vague_words'])} (fix these first)")
        out.append("  Each usually means a control has not been decided.")
        for h in r["vague_words"][:12]:
            out.append(f"    \"{h['found']}\" -> {h['advice']}")
        if len(r["vague_words"]) > 12:
            out.append(f"    ... and {len(r['vague_words']) - 12} more")
        out.append("")

    if r["long_sentences"]:
        out.append(f"LONG SENTENCES - {c['long_sentences']} of {c['sentences']} "
                   f"({c['long_sentence_pct']}%) over {r['settings']['max_sentence_words']} words")
        for d in r["long_sentences"][:5]:
            out.append(f"    [{d['words']} words] {d['text']}")
        out.append("")

    if r["complex_words"]:
        out.append(f"COMPLEX WORDS - {len(r['complex_words'])}")
        for h in r["complex_words"][:12]:
            out.append(f"    \"{h['found']}\" -> \"{h['advice']}\"")
        if len(r["complex_words"]) > 12:
            out.append(f"    ... and {len(r['complex_words']) - 12} more")
        out.append("")

    if r["passive_voice"]:
        n = len(r["passive_voice"])
        out.append(f"PASSIVE VOICE - {n} candidate{'' if n == 1 else 's'} "
                   "(name who does it)")
        for d in r["passive_voice"][:5]:
            out.append(f"    \"{d['found']}\" in: {d['text']}")
        out.append("")

    if r["unexplained_acronyms"]:
        out.append("UNEXPLAINED ACRONYMS - expand on first use, or remove")
        out.append("    " + ", ".join(r["unexplained_acronyms"][:20]))
        out.append("")

    if r["contractions"]:
        out.append("CONTRACTIONS - write words in full so instructions carry weight")
        out.append("    " + ", ".join(r["contractions"]))
        out.append("")

    if r["shouting_capitals"]:
        out.append("BLOCKS OF CAPITALS - fine in a heading, slower to read in body text")
        for s in r["shouting_capitals"]:
            out.append(f"    {s}")
        out.append("")

    if r["nominalisations"]:
        out.append("NOMINALISATIONS - a verb hiding inside a noun (e.g. 'do an inspection' "
                   "-> 'inspect')")
        out.append("    " + ", ".join(r["nominalisations"]))
        out.append("")

    flagged = (r["vague_words"] or r["long_sentences"] or r["complex_words"]
               or r["unexplained_acronyms"])
    if not flagged:
        out.append("No mechanical flags. That is the easy half - now test it with workers.")
        out.append("")

    out.append("Thresholds here are this tool's conventions, NOT a regulator's - no law sets a")
    out.append("reading level, and no score discharges a duty. Accuracy outranks readability.")
    out.append("The real test is demonstration or thinking-aloud with the workers who use it.")
    return "\n".join(out)


# --- self-test -------------------------------------------------------------------

BAD = (
    "Prior to the commencement of any work activity at height, it is required that all "
    "workers shall utilise appropriate PPE at all times and the work area is to be "
    "inspected regularly by a competent person in order to ascertain that adequate "
    "controls have been implemented in accordance with the relevant procedure. "
    "Don't work at height in the vicinity of the edge. ALL WORKERS MUST COMPLY AT ALL TIMES."
)
GOOD = (
    "Before you work at height, put on your harness and helmet. "
    "Check the edge protection is in place. "
    "If the edge protection is missing, stop work and tell your supervisor."
)


def selftest() -> int:
    failures = 0

    def check(label: str, ok: bool, detail: str = "") -> None:
        nonlocal failures
        print(f"  [{'PASS' if ok else 'FAIL'}] {label}" + (f" - {detail}" if detail else ""))
        if not ok:
            failures += 1

    bad, good = analyse(BAD), analyse(GOOD)

    vague_found = {h["found"] for h in bad["vague_words"]}
    check("vague words detected in the bad sample",
          {"appropriate ppe", "regularly", "competent person", "adequate"} <= vague_found,
          f"found {sorted(vague_found)}")
    check("no vague words in the good sample", not good["vague_words"])

    complex_found = {h["found"] for h in bad["complex_words"]}
    check("complex phrases detected",
          {"prior to", "utilise", "in order to", "ascertain", "in the vicinity of"} <= complex_found,
          f"found {sorted(complex_found)}")
    check("longest-phrase-first matching (no bare 'commence' inside 'commencement')",
          "commencement" in complex_found and "commence" not in complex_found)

    check("long sentence detected in the bad sample", bad["counts"]["long_sentences"] >= 1)
    check("no long sentences in the good sample", good["counts"]["long_sentences"] == 0)

    check("contraction detected", "don't" in bad["contractions"])
    check("no contractions in the good sample", not good["contractions"])
    check("shouting capitals detected", len(bad["shouting_capitals"]) >= 1)
    check("unexplained acronym detected", "PPE" in bad["unexplained_acronyms"])
    check("explained acronym not flagged",
          "PPE" not in analyse("Wear personal protective equipment (PPE). "
                               "Check the PPE before use.")["unexplained_acronyms"])

    check("good sample reads easier than bad",
          good["readability"]["reading_ease"] > bad["readability"]["reading_ease"],
          f"{good['readability']['reading_ease']} vs {bad['readability']['reading_ease']}")

    check("markdown tables excluded from sentence stats",
          analyse("Stop work.\n\n| a | b |\n|---|---|\n| 1 | 2 |\n")["counts"]["sentences"] == 1)
    check("empty input does not crash", analyse("")["counts"]["words"] == 0)
    check("passive voice detected",
          any("inspected" in d["found"] for d in analyse(
              "The area is inspected by the supervisor.")["passive_voice"]))

    print()
    if failures:
        print(f"{failures} failure(s)")
        return 1
    print("All self-tests passed.")
    return 0


def main() -> int:
    p = argparse.ArgumentParser(
        description="Deterministic plain-language linting for health & safety documents.",
        epilog="Not a compliance test. No law sets a reading level, and no score discharges "
               "a duty. Test with the workers who use the document.",
    )
    p.add_argument("path", nargs="?", help="file to check (omit to read stdin)")
    p.add_argument("--json", action="store_true", help="machine-readable output")
    p.add_argument("--max-sentence", type=int, default=DEFAULT_MAX_SENTENCE,
                   help=f"words before a sentence is flagged as long (default {DEFAULT_MAX_SENTENCE})")
    p.add_argument("--selftest", action="store_true", help="run the built-in tests")
    args = p.parse_args()

    if args.selftest:
        return selftest()

    if args.path:
        try:
            with open(args.path, encoding="utf-8") as fh:
                text = fh.read()
        except OSError as e:
            p.error(f"cannot read {args.path}: {e}")
    elif not sys.stdin.isatty():
        text = sys.stdin.read()
    else:
        p.print_help()
        return 0

    if not text.strip():
        p.error("no text to check")
    if args.max_sentence < 5:
        p.error("--max-sentence must be at least 5")

    result = analyse(text, args.max_sentence)
    print(json.dumps(result, indent=2) if args.json else report(result))
    return 0


if __name__ == "__main__":
    sys.exit(main())
