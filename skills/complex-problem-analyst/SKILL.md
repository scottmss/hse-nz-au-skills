---
name: complex-problem-analyst
description: Use this skill for a complex, recurring or multi-causal workplace problem that simple
  fixes haven't solved — to run a Fishbone (Ishikawa) analysis that maps all contributing factor
  categories at once. Triggers on "why does this keep happening", "we can't figure out why", "it's
  not just one thing", "recurring issue", "systemic", "fishbone", "Ishikawa", "contributing
  factors", "post-mortem", "post-incident review", or any request to diagnose a failure with several
  converging causes rather than a single chain. Use this when the problem involves people, process,
  equipment and environment interacting. Pairs with incident-investigator (Five Whys) for depth.
  NZ/AU workplace context. Not legal advice.
---

# Complex Problem Analyst (Fishbone / Ishikawa)

## Purpose

Diagnose a **multi-causal** workplace problem by mapping all contributing factor *categories* at once
— rather than following a single causal thread. The Fishbone (Ishikawa) diagram puts the **problem
(effect)** at the fish head and the **cause categories** as bones; each bone carries several
contributing factors. Mapping them together reveals **intersections** — the combinations of factors
that actually produce failures.

## When to use

- A problem that **keeps coming back** despite obvious fixes.
- A failure that clearly involves **several factors at once** (people + process + equipment +
  environment).
- Post-incident reviews / post-mortems for events with no single cause.
- Recurring quality or operational breakdowns spanning multiple teams or systems.

## When NOT to use

- A largely **single-thread** event (one thing led to the next) → `../incident-investigator/`
  (Five Whys) drills it faster. Common pattern: **Fishbone first to find the categories, then Five
  Whys to drill the 1–3 most significant.**
- **Prospective** risk (could happen) → `../critical-risk-manager/` (bow tie).
- Legal-duty questions → route via `../hse-advisor/`.

## The 6M cause categories (default)

Sweep all six so no class of cause is missed (adapt labels to context):

| Category | Also called | Look for |
|---|---|---|
| **People** | Man, human factors | Skills, training, fatigue, judgement, communication, supervision |
| **Process** | Method | Procedures, steps, standards, decision rules, SOPs |
| **Equipment** | Machine | Tools, vehicles, machinery, technology, maintenance state |
| **Environment** | Mother Nature, milieu | Weather, lighting, noise, layout, time pressure, culture |
| **Materials** | | Inputs, parts, substances, data/information quality |
| **Measurement** | Management | Inspection, verification, feedback loops, monitoring (or, in ops/H&S, organisational and oversight factors) |

Drop categories that genuinely don't apply; add domain-specific ones if needed. Alternative label
sets and the full method are in `references/ishikawa-6m.md`.

## Method

1. **Define the problem (fish head)** — a precise, factual effect statement: what happened, when and
   where, and the measurable impact. No blame. (A vague statement yields a vague analysis.)
2. **Brainstorm across ALL categories at once** — for each bone ask "how might factors here have
   contributed?". Breadth before depth; don't chase one bone to its end first. Capture short phrases;
   don't evaluate yet.
3. **Build the diagram** — represent it as a portable ASCII/Markdown tree (see below;
   `references/ishikawa-6m.md` for the format).
4. **Identify the significant factors** — separate **root causes** (fixing them prevents recurrence)
   from **contributing factors**, and find **compounding intersections** (where two or more bones had
   to align). Factors appearing across multiple bones are often systemic.
5. **Corrective actions by category** — a table (factor · category · action · owner · timeline).
   Prioritise actions that address **multiple bones** at once.
6. **State gaps and unknowns** — what's unavailable, unconfirmed, or needs more investigation.

## Portable diagram format (default)

```
PROBLEM: [effect statement]

PEOPLE
  ├─ [contributing factor]
  └─ [contributing factor]
PROCESS
  ├─ [contributing factor]
  └─ [contributing factor]
EQUIPMENT
  └─ [contributing factor]
ENVIRONMENT
  └─ [contributing factor]
MEASUREMENT
  └─ [contributing factor]
```

Works everywhere and is easy to edit. (A Mermaid alternative is in `references/ishikawa-6m.md`.)

## Integration with Five Whys

The Fishbone tells you **where** to look; Five Whys tells you **how deep** to go on a specific cause.
Use them together: Fishbone → pick the 1–3 most significant root causes → apply Five Whys to each
(`../incident-investigator/`). Don't Five-Whys every bone — that loses the multi-causal advantage.

## Jurisdiction note

The method is jurisdiction-neutral. If the underlying event may be a **notifiable event/incident**,
the notify/preserve duties are time-critical — hand off (NZ: `../worksafe-nz-specialist/`; AU:
`../safework-au-specialist/`). Investigate to learn, not to blame.

## Output format

1. **Problem statement** (1–2 sentences). 2. **Fishbone diagram** (ASCII default). 3. **Key findings**
— root causes, contributing factors, intersections. 4. **Corrective actions table** (factor ·
category · action · owner · timeline). 5. **Gaps and unknowns.** Scale rigour to severity.

## Hand-offs

- **Drill a specific cause** → `../incident-investigator/` (Five Whys).
- **A critical control failed** → `../critical-risk-manager/`.
- **Notifiable event** → `../worksafe-nz-specialist/` (NZ) / `../safework-au-specialist/` (AU).
- **Board/officer learning** → `../officer-governance-advisor/`. Route via `../hse-advisor/`.

## Disclaimer

This skill produces analysis and structure — **not legal advice and not a determination of fault**.
Findings must be validated by a competent person against the evidence, and any legal/notification
obligation confirmed against the current Act and regulator guidance. Frame causes as systemic, not
personal.
