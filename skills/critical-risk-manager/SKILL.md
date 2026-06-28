---
name: critical-risk-manager
description: Use this skill when building or reviewing a bow tie risk assessment, defining a
  critical risk, assessing control (barrier) assurance, or scoring residual risk for NZ/AU
  workplace hazards. Triggers on "bow tie", "bowtie", "critical risk", "control assurance",
  "barrier", "top event", "barrier analysis", "threat", "consequence", "risk matrix",
  "residual risk", "escalation factor", "critical control". Builds the structured visual risk
  story for high-energy / fatal-risk hazards — crane lifts, confined space, working at height,
  chemical handling, traffic/mobile plant, electrical, dropped objects. Grounded in HSWA 2015
  (NZ) and the WHS model law (AU). Use the bow tie structure here before starting any bow tie.
---

# Critical Risk Manager

## Purpose

Build and review **bow tie risk assessments** and **critical-risk control assurance** for NZ/AU
workplace hazards — turning a hazard into a clear, defensible risk story: threats → top event →
consequences, with preventive and mitigating controls, escalation factors, and a residual-risk
view. Designed for **critical (potentially fatal) risks**, where the quality and assurance of a
small number of controls matters more than a long generic hazard list.

## When to use

- Building a new bow tie for a hazard or activity.
- Reviewing/critiquing an existing bow tie for completeness and control quality.
- Defining whether something is a **critical risk** and identifying its **critical controls**.
- Scoring residual risk on a matrix, or assessing **control assurance** (are the controls real,
  in place, and verified?).

## When NOT to use

- Routine, low-consequence task hazards better served by a JSA / task analysis → hand off to
  `task-analysis-author`.
- Investigating an event that has already happened → hand off to `incident-investigator`
  (Five Whys) or `complex-problem-analyst` (Fishbone).
- Pure legal-duty questions (is this notifiable? what does the PCBU owe?) → route via
  `hse-advisor` to the jurisdiction specialist.

## Method

Load `references/bowtie-methodology.md` for the full method. In brief:

1. **Name the hazard** — the source of harm with potential energy (e.g. *suspended load*,
   *stored hydraulic energy*, *working at height*). One hazard per bow tie.
2. **Define the top event** — the moment control of that hazard is lost (e.g. *load falls from
   crane*). Not the cause, not the consequence — the release point. See
   `references/critical-risk-definitions.md` for the line between hazard, top event, and
   consequence.
3. **List the threats** (left side) — credible causes that could lead to the top event. Each
   threat is an independent line to the top event.
4. **List the consequences** (right side) — credible outcomes if the top event occurs, including
   the worst credible (usually fatality for a critical risk).
5. **Add preventive controls** — barriers on each *threat line*, between the threat and the top
   event. Apply the **hierarchy of controls** (elimination > substitution > engineering >
   administrative > PPE) and prefer hard controls.
6. **Add mitigating controls** — barriers on each *consequence line*, between the top event and
   the consequence (e.g. exclusion zones, emergency response, trauma care).
7. **Identify critical controls** — the few controls that, if they failed, would most likely
   allow a fatality. Flag these explicitly; they need the highest assurance.
8. **Add escalation factors + their controls** — conditions that defeat or degrade a control
   (e.g. *competency lapse*, *fatigue*, *bypassed interlock*), and the controls that manage them.
9. **Assess control assurance** — for each critical control, is it *in place*, *effective*, and
   *verified*? Load `references/control-assurance.md`.
10. **Score residual risk** — using the matrix in `references/critical-risk-definitions.md`.
    For deterministic, repeatable scoring run `scripts/risk_matrix_scorer.py` rather than scoring
    by eye.

Apply the **hierarchy of controls** throughout and challenge administrative/PPE-only lines — a
critical risk carried only by "be careful" and a hi-vis vest is a red flag. Sweep the **6M
framework** (Machine, Mother Nature, Man, Method, Material, Management — `bowtie-methodology.md`)
across threats, barriers and consequences so no whole class of cause is missed, and pick a
**diagram format A/B/C** up front. Worked starting templates are in `references/examples.md`.

**Done when:** the top event is a genuine loss-of-control; every threat and consequence line has at
least one effective control; critical controls are flagged with their assurance status (in place /
effective / verified) and none introduces a worse new hazard; escalation factors are addressed for
each critical control; residual risk is scored; and gaps/recommendations are listed.

## Jurisdiction note

The bow tie method is identical across NZ and AU; the **legal framing of "adequate" controls
differs**. Both use the *reasonably practicable* (SFAIRP) test, and both require risk to be
**eliminated** SFAIRP and otherwise **minimised** SFAIRP — the legal backbone of the hierarchy of
controls (NZ: HSWA 2015 **s 22** reasonably practicable, **s 30** management of risks; AU model
WHS Act **s 18** and **s 17**; Victoria's OHS Act 2004 differs). The regulations, approved codes
and standards that define *good practice* differ by jurisdiction (and by Australian state —
Victoria especially). Treat these section numbers as verify-pointers, not quotes. Establish
jurisdiction via `hse-advisor` first, and state which standards/codes you are treating as good
practice. Default to **NZ / HSWA 2015** only when context clearly implies it; otherwise ask.

## Output format

Produce, in this order:

1. **Header** — hazard, top event, activity/context, jurisdiction, date, "draft — requires
   competent-person review".
2. **Bow tie table** — Threats → Preventive controls → **Top event** → Mitigating controls →
   Consequences. (The table is the source of truth; a **Mermaid diagram** can follow —
   `references/mermaid-template.md`.)
3. **Critical controls list** — each flagged control, why it's critical, and its assurance
   status (in place / effective / verified — or the gap).
4. **Escalation factors** — factor → which control it threatens → escalation-factor control.
5. **Residual risk** — pre-control and post-control rating from the matrix, with the
   justification and any assumptions.
6. **Gaps & recommendations** — missing controls, weak (admin/PPE-only) lines, unverified
   critical controls.
7. **Disclaimer.**

## Hand-offs

- **Notifiable event** surfaced by a consequence → `worksafe-nz-specialist` (NZ) or
  `safework-au-specialist` (AU), via `hse-advisor`.
- **High-risk-work licensing / plant competency** (crane, rigging, EWP, scaffold) →
  `high-risk-work-specialist`.
- **Turn controls into a procedure** → `sop-author`; **into a task-level JSA** →
  `task-analysis-author`.
- **A critical control failed in a real event** → `incident-investigator`.

## Disclaimer

This skill produces a structured risk assessment **draft — not legal advice and not a verified
control set**. A competent H&S person must validate every threat, consequence, and control
against the actual site, plant, people, and the current law and standards before use. Bow tie
completeness does not by itself discharge any duty holder's obligations.
