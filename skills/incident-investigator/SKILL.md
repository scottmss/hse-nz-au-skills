---
name: incident-investigator
description: Use this skill to investigate a workplace incident, near-miss or failure with a
  structured Five Whys root cause analysis (RCA). Triggers on "five whys", "5 whys", "root cause",
  "RCA", "why did this happen", "incident investigation", "near-miss investigation", "what caused",
  "investigate this incident", "post-incident", or any request to systematically work out why an
  event occurred and how to stop it recurring. Single-thread causal method — for a multi-causal
  problem with several converging factors, use complex-problem-analyst (Fishbone) instead, or first.
  Retrospective (an event that happened); for prospective risk use critical-risk-manager. NZ/AU
  workplace context. Not legal advice.
---

# Incident Investigator (Five Whys RCA)

## Purpose

Investigate a workplace incident, near-miss or failure by asking **"Why?"** repeatedly — using each
answer as the input to the next question — until fixing the answer would prevent recurrence. Produces
a clear problem statement, a validated causal chain, root cause(s), and corrective actions with
owners and dates. Five Whys is a **single-thread** method: it drills one causal line deep.

## When to use

- A specific incident, near-miss, injury, property-damage event or failure needs investigating.
- You want to get past the symptom to the **systemic** cause and stop recurrence.
- The event is largely **one causal chain** (one thing led to the next).

## When NOT to use

- A **multi-causal** event where several factors converged (people + process + equipment +
  environment all at once) → use `../complex-problem-analyst/` (Fishbone), which maps all factor
  categories at once. A common pattern: Fishbone first to find the categories, then Five Whys to
  drill the 1–3 most significant.
- **Prospective** risk (could happen, not did) → `../critical-risk-manager/` (bow tie).
- Pure legal-duty questions (is this notifiable? who owed what?) → route via `../hse-advisor/`.

## Method

### 1. Write the problem statement
One specific, factual sentence — **what · where · when · who (roles)**, observable, no blame.
- ✅ "Mobile crane sling parted during a tandem lift at the yard, 14 March, load dropped ~2 m, no
  injury."
- ❌ "There was a problem with the crane."

### 2. Build the why-chain
Ask "Why did *[the problem]* happen?", then "Why did *[that answer]* happen?", and so on. Record each
answer; it becomes the next question. Typically **3–5 whys**; go further if needed.

**Validation test at every step:** *"If we fixed this, would the problem still happen?"*
- **Yes** → it's a contributing factor; keep asking.
- **No** → you've reached a root cause.

**Facilitation rules:**
- **Never stop at "human error"** — ask *why* the error was possible (what system allowed it).
- **No blame** — focus on systems, processes and conditions, not individuals.
- **Be specific** — push past trivially simple answers.
- **Include people with direct operational knowledge** of how the work is really done.
- Treat **time/schedule pressure** as a system/management cause, not an excuse — ask why pressure was
  allowed to override the safety step.

### 3. Identify root cause(s)
For each candidate root cause: *"If this were eliminated, would the incident have been prevented?"*
If yes → confirmed root cause. **Multiple root causes are valid.** A single chain can branch.

### 4. Corrective actions
For each root cause specify: **What** (specific action) · **Who** (named person/role) · **When**
(date) · **How effectiveness will be verified**. Prefer **hard** controls over more procedure/training
where reasonably practicable (see `../critical-risk-manager/`).

### 5. Capture what's still unknown
Be honest about gaps: information not available, lines needing further investigation, suspected-but-
unconfirmed factors.

See `references/investigation-methodology.md` for the full guide and a worked example.

## Jurisdiction note

The method is jurisdiction-neutral, but the **obligations around an event are not**. If the incident
may be a **notifiable event/incident**, the duties to notify and preserve the site are time-critical
— hand off immediately (NZ: `../worksafe-nz-specialist/`; AU: `../safework-au-specialist/`). Do not
let an investigation delay notification or disturb the scene.

## Output format

A structured investigation produces:
1. **Incident details** — date, location, investigator, problem statement.
2. **Cause chain** — the why-chain as a table or list (each step → answer).
3. **Root cause(s)** — clearly stated and validated.
4. **Corrective actions** — table: action · owner · due date · verification.
5. **Summary** — 2–3 sentences for management/governance reporting.
6. **Gaps & unknowns.**

A colour-coded ASCII/Markdown chain (symptom → … → root cause) is a good portable visual.

## Hand-offs

- **Multi-causal event** → `../complex-problem-analyst/` (Fishbone) — run it first or alongside.
- **A critical control failed** → `../critical-risk-manager/` to rebuild/assure the control set.
- **Notifiable event** → `../worksafe-nz-specialist/` (NZ) / `../safework-au-specialist/` (AU).
- **Board/officer learning from the event** → `../officer-governance-advisor/` (learning, not blame).
- Route jurisdiction/cross-skill work via `../hse-advisor/`.

## Disclaimer

This skill produces investigation structure and analysis — **not legal advice and not a determination
of fault or liability**. Findings must be validated by a competent person against the evidence, and
any legal or notification obligation confirmed against the current Act and regulator guidance.
Investigate to **learn and prevent recurrence**, not to apportion blame.
