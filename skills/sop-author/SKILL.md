---
name: sop-author
description: Use this skill to write or review a Standard Operating Procedure (SOP) / safe system of
  work — the repeatable, trainable method for how a task is done safely. Triggers on "SOP", "standard
  operating procedure", "safe operating procedure", "safe system of work", "write a procedure",
  "document the process for X", "procedure document", "work instruction", or "review/update this SOP".
  Produces the structure — purpose & scope, roles, the step-by-step method with hazards and controls
  integrated, competency sign-off, and document control. For a single job's pre-start hazard sheet use
  task-analysis-author; for a critical-risk bow tie use critical-risk-manager. NZ/AU workplace context.
  Not legal advice.
---

# SOP Author (safe systems of work)

## Purpose

Write or review a **Standard Operating Procedure (SOP)** — the documented, repeatable, **trainable**
method for how a task is performed safely and consistently. A good SOP is written **for the person
doing the work**, integrates the relevant hazards and controls, defines the **competency** required,
and is kept current under document control. It is a *standing* document (how the task is always done)
— distinct from a Task Analysis (the hazards of *this* job today) and a bow tie (a critical-risk
analysis).

## When to use

- Documenting how a recurring task should be done safely, as a basis for **training and consistency**.
- Reviewing/updating an existing SOP (refresh the steps, controls, and document control).
- Turning a method that "lives in someone's head" into a repeatable, auditable procedure.

## When NOT to use

- A **single job's** pre-start hazard sheet the crew signs onto → `../task-analysis-author/` (TA/JSA).
- A **critical (fatal) risk** barrier analysis → `../critical-risk-manager/` (bow tie) — the SOP then
  *embeds* the resulting critical controls.
- A pure **legal-duty** question → `../worksafe-nz-specialist/` / `../safework-au-specialist/`.

## Method

**Elicit the real process first.** An SOP invented from assumptions is worse than none. Interview the
people who actually do the task — don't draft from a generic template. If they struggle to describe it
in the abstract, ask them to **walk through the last time they did it**: "what did you do first, then
what?" Concrete recent memory surfaces the real steps, the decision points, and the bits people forget.
Capture the trigger, the tools/plant used, where it branches, where mistakes happen, and what "done
right" looks like — then write. Ask for anything missing rather than guessing.

1. **Define purpose and scope** — what the procedure covers, who it applies to, and any boundaries
   (what it does *not* cover).
2. **Set up document control** — scope, version, issue date, author, reviewer, owner/approver, next
   review date, and a record-of-amendments table. An SOP with no version control rots silently.
3. **Identify roles and responsibilities** — who does what in the procedure (operator, supervisor,
   spotter, etc.) — by role, not by name.
4. **Write the method as numbered steps/sections** — the actual sequence, in **plain language for the
   person doing the work**. Start each step with an **action verb** (*Check, Isolate, Confirm, Don,
   Lift*); one clear instruction per step; say what to do and what "good" looks like. Mark **decision
   points** explicitly (*"If the load exceeds X, stop and …; otherwise continue to step N"*). List any
   **prerequisites** (access, permits, plant checks) before step 1.
5. **Integrate hazards and controls** — for the task's in-scope hazards, weave the **controls** into
   the relevant steps using the hierarchy of controls. For **critical (fatal) risks**, call them out
   explicitly and list the **critical controls** the worker must apply — sourced from the bow tie
   (`../critical-risk-manager/`) and/or the organisation's risk register.
6. **Define competency and sign-off** — what the worker must understand/demonstrate, with a
   competency checklist per section and a trainee/trainer (or worker/supervisor) declaration so
   sign-off records that the person is competent. For critical risks, include a **dedicated sign-off**
   for each critical control.
7. **Set the review cycle** — when the SOP is reviewed (e.g. on change of plant/process/people, after
   an incident, and at a defined maximum interval).

See `references/sop-structure.md` for the full section-by-section structure and good-practice
principles.

## Jurisdiction note

The method is jurisdiction-neutral, but an SOP is one way a PCBU provides the **safe systems of work,
information, training and supervision** it owes (NZ HSWA s 36; AU model WHS s 19). Controls must
reflect the duty to eliminate risk SFAIRP and otherwise minimise it (NZ s 30 / AU s 17). Route duty
questions to `../worksafe-nz-specialist/` / `../safework-au-specialist/`.

## Output format

A structured SOP with, in order: **title** · **document control** (scope/version/dates/author/
reviewer/owner/next review) · **record of amendments** · **purpose & scope** · **roles &
responsibilities** · **numbered procedure** (with hazards/controls integrated and critical risks
called out) · **competency sign-off** per section · **declaration / final sign-off** · **review
cycle**. Produce it as portable, structured Markdown by default.

**Brand-neutral by default.** Do **not** invent or apply any company's house style, colours, logos,
template, or internal system/process names. If the user supplies their own template and brand, apply
that separately (and keep it out of this public, company-agnostic skill).

## Hand-offs

- **Critical-risk controls to embed** → `../critical-risk-manager/` (bow tie + control assurance).
- **A specific job's pre-start hazard sheet** → `../task-analysis-author/` (TA/JSA).
- **Competency/licence requirements** for the task → `../high-risk-work-specialist/`.
- **Duties** → `../worksafe-nz-specialist/` (NZ) / `../safework-au-specialist/` (AU). Route via
  `../hse-advisor/`.

## Disclaimer

This skill produces an SOP **draft — not legal advice and not a verified safe system of work**. A
competent person must validate the method, hazards, controls and competency requirements against the
actual site, plant and people, and keep the SOP current. A written SOP does not by itself make work
safe or discharge any duty holder's obligations — the work must actually be done the way the SOP says,
by competent people, with the controls genuinely in place.
