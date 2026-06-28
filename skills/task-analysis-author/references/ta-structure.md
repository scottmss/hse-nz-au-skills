# Task Analysis (TA / JSA) structure

The full structure, rating system and a worked example for a Task Analysis. Generic and
company-agnostic — if an organisation or client mandates its own template, matrix or wording,
substitute it. **Not legal advice.**

## What a TA is

A structured document that breaks a work activity into **steps**, identifies the **hazards** in each
step, scores the **initial risk**, documents **controls** by the hierarchy of controls, assigns a
**responsible role**, and rescores the **residual risk**. Workers **sign on** to confirm they
understand the hazards and controls before work begins. It is a **task-level, point-of-work** tool —
distinct from a standing SOP and from a critical-risk bow tie.

## Document structure

1. **Job-context header** — activity/task description; site/location; date; people involved; PPE
   required; emergency response plan (yes/no, and where it is).
2. **Risk-rating key** — the Likelihood and Consequence scales and the risk-band colours, so anyone
   reading it on site can interpret the scores without a separate reference.
3. **Worker sign-on register** — workers print and sign to confirm they've been briefed on, and will
   work to, this TA.
4. **The risk table** — the core: step → hazard → initial risk → control → responsible → residual.
5. **Emergency response** (optional) — scenario → immediate actions → responsible, plus muster point,
   first-aid location and emergency contacts.

## The risk table columns

| # | Task step | Hazard | Conseq | Likelihood | Initial risk | Control method (hierarchy-labelled) | Responsible | Conseq | Likelihood | Residual risk |
|---|---|---|---|---|---|---|---|---|---|---|

- Each **step** can carry several **hazards** (label A, B, C…); each hazard can carry several
  **controls** (one per row). Repeat the step/hazard down the rows it spans.
- **Initial risk** is scored *before* controls (inherent); **residual** *after* controls are fully in
  place. Residual should be lower than initial.

## Rating system (generic 5×5 example)

**Consequence**

| Score | Label | Meaning |
|---|---|---|
| 1 | Insignificant | No injury / negligible |
| 2 | Minor | First aid |
| 3 | Moderate | Medical treatment / lost-time injury |
| 4 | Major | Serious injury / hospitalisation |
| 5 | Catastrophic | Fatality or permanent disability |

**Likelihood**

| Score | Label | Meaning |
|---|---|---|
| 1 | Rare | Only in exceptional circumstances |
| 2 | Unlikely | Could occur but not expected |
| 3 | Possible | Could occur at some time |
| 4 | Likely | Will probably occur |
| 5 | Almost certain | Expected in most circumstances |

**Risk = Likelihood × Consequence**, banded **Low (1–3) / Moderate (4–6) / High (8–12) / Very High
(15–25)** — adjust band cut-offs to the matrix in use. For **repeatable, deterministic** scoring
(and the catastrophic-consequence override), use
`../../critical-risk-manager/scripts/risk_matrix_scorer.py` and
`../../critical-risk-manager/references/critical-risk-definitions.md` rather than scoring by eye.

> Any credible **catastrophic** outcome should be treated as a critical risk regardless of a low
> calculated band — and handled with a bow tie (`../../critical-risk-manager/`), not just a TA row.

## Hierarchy of controls

List controls **highest-order first** and label each with its type:

| Order | Type | Examples |
|---|---|---|
| 1 | **Eliminate** | Remove the hazard / don't do the hazardous step |
| 2 | **Substitute** | A less hazardous method or material |
| 3 | **Isolate** | Barriers, exclusion zones, guarding by separation |
| 4 | **Engineering** | Guards, interlocks, rated equipment, outriggers, load indicators |
| 5 | **Administrative** | Procedures, permits, training, lift plans, checklists, supervision |
| 6 | **PPE** | Last line — protects one person, depends on correct use |

Prefer hard controls (1–4) over soft (5–6). A hazard carried only by administrative controls + PPE is
a weak line — flag it.

## Quality checks before issuing

- Steps are **elicited from the crew who do the work** (not invented), phrased as actions, sequential
  and at a sensible grain; hazard letters sequential.
- Initial risk = Likelihood × Consequence with the correct band label.
- **Residual risk is lower than initial** (controls actually reduce risk).
- Every control has a **labelled type** and a **responsible role**.
- The header is fully populated (no blank fields unless confirmed N/A).
- Any **catastrophic** hazard is escalated to a bow tie, not just a TA row.
- The sign-on register has enough blank rows for the crew.

## Worked example (extract)

**Activity:** Mobile crane lift — set up and lift as directed. **PPE:** hard hat, hi-vis, steel caps,
gloves. **ERP:** Yes.

| # | Step | Hazard | Initial | Control (type) | Responsible | Residual |
|---|---|---|---|---|---|---|
| 1 | Set up crane | A. Crane overturns on soft/uneven ground | 5×3 = VH-15 | **Engineering:** outriggers fully deployed on rated pads; ground assessed | Operator | 5×1 = M-5 |
| 1 | Set up crane | A (cont.) | 5×3 = VH-15 | **Administrative:** set-up to lift plan; exclusion zone established | Supervisor | 5×1 = M-5 |
| 2 | Lift as directed | B. Suspended load strikes a person | 5×3 = VH-15 | **Isolate:** enforced exclusion zone under the load | Dogger | 5×2 = H-10 |
| 2 | Lift as directed | B (cont.) | 5×3 = VH-15 | **Administrative:** licensed dogger directs; tag lines used | Dogger | 5×2 = H-10 |

> Note the **suspended-load** line is a critical (fatal) risk — the TA records the task controls, but
> the full barrier/escalation-factor analysis and control assurance belong in a bow tie
> (`../../critical-risk-manager/`), and the crew's competency in `../../high-risk-work-specialist/`.

## Output

Produce the TA as a **portable Markdown table** by default (header + key + sign-on + risk table). It
can be rendered into a document afterwards, but keep the content **brand-neutral** unless the user
supplies their own template and house style.
