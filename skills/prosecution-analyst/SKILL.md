---
name: prosecution-analyst
description: Use this skill to learn from NZ/AU workplace health & safety prosecution patterns — what
  duty failures get prosecuted, the factors courts weigh, and the preventive lessons — as a learning
  and benchmarking source. Triggers on "prosecution", "enforcement", "what gets prosecuted", "lessons
  from", "case law", "sentencing", "penalties", "culpability", "reparation", "enforceable
  undertaking", "category 1/2/3 offence", "reckless conduct", "industrial manslaughter", "WorkSafe/
  SafeWork prosecution", "duty-holder liability", or benchmarking your controls against real failures.
  Company-agnostic and educational — it reasons about public prosecution patterns and the method of
  learning from them; it does not predict the outcome of any specific case. Not legal advice.
---

# Prosecution Analyst (learning from NZ/AU H&S prosecutions)

## Purpose

Turn NZ/AU workplace H&S **prosecution patterns** into **preventive lessons** — what kinds of duty
failure get prosecuted, the factors courts weigh in culpability and sentencing, and what an
organisation should learn and benchmark against. The value is **systemic learning and benchmarking**,
not assigning blame or predicting a verdict. Grounded in public case law and the HSWA / WHS
enforcement-and-sentencing frameworks.

> **Company-agnostic by design (and scope).** This skill reasons about **public prosecution patterns
> in general terms**. It does **not** reference any single organisation's relevance, and it does
> **not** require, bundle, or expose any proprietary prosecutions dataset — work only from public
> case law and the published frameworks.

## When to use

- Extracting the **systemic lessons** from a class of prosecution (e.g. crane, forklift, working at
  height, machine guarding, contractor management) to strengthen your own controls.
- **Benchmarking** your control set against the failures that typically get prosecuted.
- Understanding the **enforcement and sentencing framework** (offence tiers, culpability, reparation,
  penalties, enforceable undertakings) at a conceptual level.
- Briefing a board/officer on the lessons and risk areas (governance learning).

## When NOT to use

- **Advising on a live or specific case**, predicting an outcome, or assessing one organisation's
  liability → that needs a **competent H&S lawyer**, not this skill.
- The underlying **duty analysis** (who owes what, notifiable events) → `../worksafe-nz-specialist/`
  (NZ) / `../safework-au-specialist/` (AU).
- **Investigating** an actual incident → `../incident-investigator/` / `../complex-problem-analyst/`.

## Method — learning, not blame

1. **Frame the question as a pattern**, not a case: "what do prosecutions in *[activity/hazard]*
   typically turn on, and what's the lesson?" — not "will *X* be convicted?".
2. **Identify the duty failure pattern** — which duty was breached and how (e.g. failure to identify
   a known critical risk, failure to implement a known/available control, inadequate training or
   supervision, plant not maintained, failure to consult/coordinate across PCBUs).
3. **Map the recurring contributing factors** — the systemic conditions that show up again and again
   (see `references/nz-au-prosecution-patterns.md`).
4. **Extract the preventive lesson** — the control, system or governance practice that would have
   broken the pattern. Convert it into a check the organisation can run *now*.
5. **Benchmark** — does our own control set address this failure pattern? Where's our gap?
6. **Frame culpability/sentencing factors** *educationally* — what aggravates and mitigates, and why
   — to motivate prevention, never to estimate a number for a real case.

### Grounding the patterns in real cases (if you have a dataset)

This skill works on general reasoning by default. If you have access to a **prosecutions dataset** —
for example a read-only **MCP server** exposing public NZ/AU enforcement cases — ground the patterns
in it rather than reasoning from memory: search by **industry / legislation / jurisdiction / year**,
retrieve a case's detail and any attached judgment, look at summary statistics, and **cross-reference
the recurring failures against your own highest-residual risks**. Keep using the data as a *learning*
source (patterns and lessons), not as legal advice or case prediction, and stay within whatever the
dataset's licence and access permit. The method is the same with or without a dataset — a dataset
just makes the benchmarking concrete and current.

## The enforcement & sentencing frameworks (conceptual)

Detail and verified penalties/bands are in `references/nz-au-prosecution-patterns.md`. In outline:

- **New Zealand (HSWA 2015):** offence tiers **s 47** (reckless conduct), **s 48** (failure exposing
  to risk of death/serious injury), **s 49** (failure to comply); WorkSafe enforcement tools
  (improvement/prohibition notices, **enforceable undertakings**, prosecution); sentencing via the
  **Stumpmaster** four-step approach (reparation → fine by culpability band → ancillary orders →
  overall proportionality and ability to pay).
- **Australia (model WHS):** **Category 1 (s 31)** reckless/gross negligence, **Category 2 (s 32)**,
  **Category 3 (s 33)**; **industrial manslaughter** as a separate offence in most jurisdictions
  (elements/penalties vary); enforceable undertakings and a range of sentencing orders. **Penalties
  and the IM offence vary by jurisdiction and are periodically increased — verify.**

## Common prosecution patterns (the recurring lessons)

Across NZ/AU H&S prosecutions, the same systemic failures recur — full list in the reference:

- A **known critical risk** was not adequately controlled (the hazard and control were well
  understood in the industry).
- A **known, available, reasonably practicable control** was not implemented (or was removed/bypassed).
- **Inadequate training, competency or supervision** for the task.
- **Plant/machinery** not guarded, isolated or maintained.
- **Prior warnings, near-misses or audit findings ignored** — the event was foreseeable.
- **Failure to consult, cooperate and coordinate** across multiple PCBUs (contracting chains).

The lesson is almost always: the risk was **foreseeable** and a **reasonably practicable control
existed** — which is exactly what `../critical-risk-manager/` and the duty skills are for.

## Jurisdiction note

Penalties, offence structures and sentencing methods **differ between NZ and AU, and between
Australian jurisdictions** (and Victoria runs the OHS Act 2004). Treat section numbers, bands and
penalty figures as **verify-pointers** — they are amended over time. Establish jurisdiction via
`../hse-advisor/` and confirm current figures with the regulator / current case law.

## Output format

- **Pattern brief** — the duty-failure pattern, recurring contributing factors, and the **preventive
  lesson(s)** as actionable checks.
- **Benchmark check** — for a given activity, the failure patterns to test your own controls against.
- **Educational sentencing framing** — the aggravating/mitigating factors and the framework, clearly
  flagged as general and not a prediction.

Every output is **educational and general** — for a specific matter, get legal advice.

## Hand-offs

- **Fix the control the lesson points to** → `../critical-risk-manager/` (bow tie + assurance).
- **The duty itself** → `../worksafe-nz-specialist/` / `../safework-au-specialist/`.
- **Board/officer learning and due diligence** → `../officer-governance-advisor/`.
- **Investigate a real event** → `../incident-investigator/` / `../complex-problem-analyst/`. Route
  via `../hse-advisor/`.

## Disclaimer

This skill produces **general, educational analysis of public prosecution patterns — not legal advice,
not a prediction of any case's outcome, and not an assessment of any organisation's liability**. H&S
prosecution outcomes turn on specific facts and the current law, which change over time. For any live
or specific matter, consult a competent H&S lawyer in the relevant jurisdiction. Use prosecution
lessons to **prevent harm and strengthen controls** — never to assign blame.
