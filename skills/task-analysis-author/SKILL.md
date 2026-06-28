---
name: task-analysis-author
description: Use this skill to create a Task Analysis (TA) / Job Safety Analysis (JSA) for a specific
  work activity — breaking the job into steps, identifying the hazards in each step, scoring the risk,
  applying controls by the hierarchy of controls, and rescoring residual risk, with a worker sign-on.
  Triggers on "task analysis", "TA", "JSA", "job safety analysis", "JHA", "step-by-step hazard
  analysis", "document the hazards for this job", "we need a TA before we start", or "what are the
  risks and controls for this task". Task/step level (the hazards of doing a job today); for a
  critical-risk bow tie use critical-risk-manager, and for a full procedure use sop-author. NZ/AU
  workplace context. Not legal advice.
---

# Task Analysis Author (TA / JSA)

## Purpose

Produce a **Task Analysis (TA)** — also called a Job Safety Analysis (JSA) or Job Hazard Analysis
(JHA) — for a specific work activity: break the activity into **steps**, identify the **hazards** in
each step, score the **initial risk**, apply **controls** using the hierarchy of controls, assign a
**responsible role**, and rescore the **residual risk**. Workers **sign on** to confirm they
understand the hazards and controls before the work begins. A TA is a **task-level, point-of-work**
document — practical and specific to the job in front of the crew.

## When to use

- Documenting the hazards and controls for a **specific job/activity** before it starts.
- A pre-start / pre-task hazard assessment the crew signs onto.
- Breaking a job into steps to find where the harm could occur and how to control it.

## When NOT to use

- A **critical (potentially fatal) risk** that needs a barrier/escalation-factor analysis →
  `../critical-risk-manager/` (bow tie). A TA can *reference* the bow tie's critical controls.
- A **standing procedure** for how a task is always done → `../sop-author/` (an SOP). A TA is for
  *this* job; an SOP is the repeatable method.
- Investigating an event that happened → `../incident-investigator/` / `../complex-problem-analyst/`.

## Method

1. **Capture the job context** — the activity, location/site, date, who's involved, the PPE required,
   and whether an emergency response plan applies. **Interview the crew who'll do the work** rather
   than inventing steps; ask for anything missing rather than guessing. If they struggle to describe
   the job in the abstract, ask them to **walk through the last time they did it** — concrete recent
   memory surfaces the real steps and the easy-to-miss hazards.
2. **Break the activity into steps** — the natural sequence (e.g. *mobilise → set up → carry out →
   pack down*), each phrased as an **action** (*Mobilise, Set up, Lift, Pack down*). Keep steps at a
   sensible grain — not one giant step, not fifty tiny ones.
3. **Identify hazards per step** — for each step, list the credible hazards (label them A, B, C…).
   Focus on what can cause harm. A 6M sweep (Machine / Mother Nature / Man / Method / Material /
   Management — see `../critical-risk-manager/references/bowtie-methodology.md`) helps avoid blind
   spots.
4. **Score the initial risk** — Likelihood × Consequence on a 5×5 matrix (the *inherent* risk before
   controls). Use the generic matrix and the **deterministic scorer** in
   `../critical-risk-manager/` (`references/critical-risk-definitions.md` +
   `scripts/risk_matrix_scorer.py`) so scoring is repeatable, not by eye.
5. **Apply controls (hierarchy of controls)** — for each hazard, list the controls **highest-order
   first**: Eliminate → Substitute → Isolate → Engineering → Administrative → PPE. Label each control
   with its type. Prefer hard controls; challenge admin/PPE-only lines.
6. **Assign a responsible role** — who ensures each control is in place and working (a role, not a
   name).
7. **Score the residual risk** — Likelihood × Consequence *after* the controls. Residual should be
   lower than initial; if it isn't, the controls aren't doing enough.
8. **Add the worker sign-on** — a register for workers to confirm they've been briefed on, and will
   work to, the TA before starting.

See `references/ta-structure.md` for the full structure, the rating system, and a worked example.

**Done when:** every step has its credible hazards; each hazard has an initial score, hierarchy-
labelled controls with a responsible role, and a residual score lower than the initial; any
catastrophic hazard is escalated to a bow tie; the header is complete; and the sign-on register is
present.

## Jurisdiction note

The method is jurisdiction-neutral. The **legal backbone** is the duty to eliminate risk *so far as
is reasonably practicable* and otherwise minimise it via the hierarchy of controls (NZ: HSWA s 30/
s 22; AU: model WHS s 17/s 18 — see `../worksafe-nz-specialist/` / `../safework-au-specialist/`). The
**5×5 matrix is a generic example** — if the organisation or client mandates a specific matrix,
substitute it. State which matrix you used.

## Output format

A TA table, in this column order:

| # | Task step | Hazard | Initial risk (L×C) | Control (hierarchy-labelled) | Responsible | Residual risk (L×C) |

Plus: a **job-context header** (activity, site, date, PPE, ERP yes/no), a **risk-rating key**, and a
**worker sign-on register**. Produce it as a portable Markdown table by default; it can be rendered to
a document afterwards. **Do not invent a house style or brand** — keep it generic unless the user
supplies their own template.

## Hand-offs

- **Critical risk in the task** → `../critical-risk-manager/` (build/assure the bow tie; reference its
  critical controls in the TA).
- **High-risk-work competency** (crane, rigging, scaffold, EWP) → `../high-risk-work-specialist/`.
- **Turn a repeated task into a standing procedure** → `../sop-author/`.
- **Underlying duties** → `../worksafe-nz-specialist/` (NZ) / `../safework-au-specialist/` (AU).
  Route via `../hse-advisor/`.

## Disclaimer

This skill produces a task-level risk assessment **draft — not legal advice and not a verified safe
system of work**. A competent person must validate every step, hazard, control and score against the
actual site, plant and people before the work proceeds, and confirm the controls are genuinely in
place. A signed TA does not by itself make the work safe or discharge any duty holder's obligations.
