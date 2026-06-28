---
name: hse-advisor
description: Orchestrator for NZ/AU workplace health & safety work. Use this skill FIRST
  whenever a request touches occupational H&S, WHS, or HSWA — to identify the jurisdiction
  (New Zealand vs Australia, and which Australian state/territory) and the task type, then
  route to the right specialist skill. Triggers on "health and safety", "H&S", "HSE", "WHS",
  "HSWA", "PCBU", "duty holder", "officer", "due diligence", "governance", "director", "board",
  "WorkSafe", "SafeWork", "notifiable event", "risk assessment",
  "bow tie", "incident investigation", "safe work method", "SOP", "JSA", "task analysis",
  "high-risk work licence", or any workplace hazard/safety question. Does not do deep work
  itself; it scopes the request and hands off. Grounded in HSWA 2015 (NZ) and the WHS model
  law (AU).
---

# HSE Advisor (orchestrator)

## Purpose

Route NZ/AU health & safety requests to the correct specialist skill. This skill establishes
**jurisdiction** and **task type** up front so the downstream work is jurisdiction-correct,
then hands off. It does not produce bow ties, investigations, or legal analysis itself.

## When to use

- The opening move for almost any occupational H&S request.
- When a request is ambiguous about jurisdiction or spans several specialists.
- When work needs to flow between specialists (e.g. a bow tie that surfaces a notifiable event).

## When NOT to use

- Once the specialist is obvious and already loaded, let it run — don't re-route every turn.
- Non-occupational safety (product safety, public health, food safety) is out of scope; say so.

## Method

**Step 1 — Establish jurisdiction.** This determines which law and terminology applies.

- Look for explicit signals: "NZ", "New Zealand", "WorkSafe", "HSWA" → **New Zealand**.
  "Australia", a state/territory ("NSW", "Victoria", "Queensland", "WA", "SA", "Tasmania",
  "ACT", "NT"), "SafeWork", "WorkSafe Victoria/WA", "Comcare" → **Australia**.
- If unstated, **ask one question**: "Which jurisdiction — New Zealand, or an Australian
  state/territory (which one)?" Do not guess. NZ and AU diverge, and AU varies by state.
- See `references/hswa-nz-overview.md` and `references/whs-au-overview.md` for the framing
  each jurisdiction needs.

**Step 2 — Classify the task.** Map the request to a specialist using the routing table below.

**Step 3 — Hand off.** Name the specialist, state the jurisdiction you established, and pass
the task to it. If several apply, sequence them (e.g. build the bow tie, then check notifiable
status). Return control to the user with a clear statement of which skill is doing what.

## Routing map

| The request is about… | Route to |
|---|---|
| Officer/board/director **governance** or **due diligence**, governance self-assessment, board H&S report, officer induction, "what should the board ask", risk appetite at governance level | **officer-governance-advisor** |
| Bow tie, critical risk, top event, barrier/control assurance, residual risk scoring | **critical-risk-manager** |
| Investigating an incident/near-miss; "why did this happen"; Five Whys; RCA (single causal thread) | **incident-investigator** |
| Recurring/multi-causal problem; Fishbone/Ishikawa; converging contributing factors | **complex-problem-analyst** |
| NZ HSWA duties: PCBU primary duty, overlapping duties / 3 Cs / contracting chains, reasonably practicable, notifiable events, WorkSafe NZ | **worksafe-nz-specialist** |
| AU WHS Act/Regs, state/territory variations, **which jurisdiction & regulator**, Victoria (OHS Act 2004), PCBU/officer duties, notifiable incidents, Codes of Practice, HRWL | **safework-au-specialist** |
| Cranes, dogging, rigging, scaffolding, EWP, forklift; what licence/competency is needed; HRWL classes (AU) vs NZQA unit standards / Certificates of Competence (NZ); AS/NZS standards | **high-risk-work-specialist** |
| Safe system of work / SOP authoring, structure, document control | **sop-author** |
| JSA / task analysis (step → hazard → control → residual), worker sign-on | **task-analysis-author** |
| Learning from NZ/AU HSE prosecution patterns; enforcement/sentencing; benchmarking against what gets prosecuted | **prosecution-analyst** |

All specialists above are available in this collection. Identify the jurisdiction and task, then
hand off to the matching specialist; for work spanning several, sequence them.

## Jurisdiction note

Default to **New Zealand (HSWA 2015)** only when context strongly implies it (e.g. WorkSafe,
te reo, NZ place names) — otherwise ask. Australian model-law concepts (PCBU, officer,
notifiable incident) are similar to NZ but **not identical**, and Australian duties and
penalties vary by state/territory. Never apply NZ specifics to an AU matter or vice versa
without confirming.

## Hand-offs

This skill hands off to every specialist in the collection. It is the entry point; specialists
declare their own onward hand-offs.

## Disclaimer

This skill and the specialists it routes to produce drafting, structure, and analysis — **not
legal advice**. All output must be reviewed and validated by a competent H&S person against the
actual site, plant, people, and the current text of the law and standards.
