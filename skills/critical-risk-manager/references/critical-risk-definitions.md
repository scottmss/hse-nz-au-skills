# Critical-risk definitions and the risk matrix

Definitions and the scoring scheme used by `critical-risk-manager`. Terminology aligns with
common NZ/AU critical-risk practice. The matrix below is a **generic example** — many
organisations and regulators use their own; always confirm which matrix applies and substitute it.

## Core definitions

- **Hazard** — a source of potential harm (an energy or substance): suspended load, gravity,
  electricity, pressure, a toxic substance, a moving vehicle.
- **Risk** — the combination of the likelihood of harm and its severity if the hazard is realised.
- **Critical risk** — a hazard with the realistic potential to cause **death or permanent
  disabling injury**. Critical risks are managed by the assurance of a few **critical controls**,
  not by long generic hazard registers. (Often called *material risks*, *fatal risks*, or
  *Significant/Material Unwanted Events* depending on the organisation.)
- **Top event** — the point at which control of the hazard is lost (released, but harm not yet
  realised). Sits between threats and consequences.
- **Threat** — a credible cause that could lead to the top event.
- **Consequence** — a credible outcome if the top event occurs.
- **Control / barrier** — a measure that prevents a threat reaching the top event (preventive)
  or reduces a consequence after it (mitigating).
- **Critical control** — a control whose failure would, alone or with one other failure, most
  likely result in a fatality or permanent disabling injury. The "few that really matter".
- **Escalation factor** — a condition that defeats or degrades a control.
- **Hierarchy of controls** — Elimination > Substitution > Engineering/Isolation >
  Administrative > PPE. Higher = more reliable (less dependent on human behaviour).

## Distinguishing hazard / top event / consequence (worked examples)

| Hazard | Threat (cause) | Top event (loss of control) | Consequence (outcome) |
|---|---|---|---|
| Suspended load (crane) | Rigging failure | Load falls from crane | Person struck and killed |
| Gravity / height | Unprotected edge | Person falls from height | Fatal fall injury |
| Mobile plant | Operator can't see pedestrian | Vehicle strikes pedestrian | Fatal crush injury |
| Stored pressure | Corroded vessel | Uncontrolled release of pressure | Fatal blast/projectile injury |
| Electricity | Contact with live conductor | Electric shock / arc flash | Electrocution / severe burns |

If you can put a control *before* it that prevents loss of control, it's a threat side; if the
control *reduces harm after* it, it's a consequence side. The top event is the hinge.

## Critical-control test

Flag a control as **critical** if **all** of these hold:
1. It addresses a critical (fatal/permanent-disability) risk.
2. Its failure would significantly increase the likelihood or severity of that outcome.
3. It is the **last reliable line** or a uniquely load-bearing barrier on that pathway.

Aim for the *few* that genuinely carry the risk, not every control. If everything is "critical",
nothing is.

## Common critical-risk categories

Most NZ/AU heavy-industry, utilities and construction organisations define a set of **critical (fatal)
risks** — the handful of energies/exposures that can kill or permanently disable. The categories below
recur across the sector; use them as a **checklist to make sure you've identified your critical
risks**, then build a bow tie for each that applies. (This is a generic industry taxonomy — confirm
and adapt the set to your own operations.)

| Category | The harm |
|---|---|
| **Driving / vehicles** | Collision or loss of control (cars, trucks, mobile plant) → `../../mobile-plant-traffic-specialist/` |
| **Working at height** | Fall from height, dropped object, suspension trauma → `../../working-at-height-specialist/` |
| **Rotating plant & major machinery** | Contact with rotating tools/plant or large machinery → `../../machinery-safety-specialist/` |
| **Hazardous substances / harmful contaminants** | Exposure to hazardous substances, fumes, dust (incl. asbestos), contaminated water → `../../hazardous-substances-specialist/` |
| **Stored / released energy** | Electrical shock, arc flash, crushing, burns; uncontrolled release of pressure/stored energy |
| **Ground disturbance / excavation** | Collapse or engulfment; contact with underground services → `../../excavation-specialist/` |
| **Confined space** | Unsafe/toxic atmosphere — asphyxiation, engulfment, inability to rescue → `../../confined-space-specialist/` |
| **Water** | Drowning or hypothermia working in, on or above water |
| **Psychosocial** | Work-design hazards causing psychological harm → `../../psychosocial-risk-specialist/` |
| **Violence & aggression** | Violence, assault or significant injury to workers or the public |

## Baseline controls for any critical risk

Many controls are hazard-specific, but a set of **general controls applies to *every* critical risk**
— the foundation that the hazard-specific (bow tie) controls sit on. Check these are in place
alongside the specific barriers:

- **Planning** — the work (and its critical risks) is planned before it starts, with the people doing
  it and the relevant **subject-matter expert(s) (SMEs)** consulted. In this collection the SMEs are
  the sibling specialists — e.g. `../../high-risk-work-specialist/` (plant/competency),
  `../../psychosocial-risk-specialist/` (psychosocial), `../../worksafe-nz-specialist/` /
  `../../safework-au-specialist/` (duties). Route via `../../hse-advisor/`.
- **Risk assessment, scaled to the risk** — escalating from a quick pre-task check, to a JSA / task
  analysis (`../../task-analysis-author/`), to a full safe-work-method statement for critical-risk
  work.
- **Consultation** — everyone affected understands the risks and controls (and the public/neighbours
  where relevant).
- **Competency** — everyone holds the required, current competency for the task
  (`../../high-risk-work-specialist/`).
- **Fatigue, and drugs & alcohol** — managed so people are fit for the task.
- **A current risk register** — hazards, risks and controls recorded and shared.
- **Reporting** — events, near-misses and hazards reported so they reach decision-makers and are
  actioned.
- **Stop-work authority** — every worker has the right (and is expected) to stop or refuse work that
  poses an imminent risk to health or safety. This is a control in its own right.

A bow tie covers the **hazard-specific** barriers; these baseline controls are the standing
foundation. A critical-risk assessment should confirm **both**.

## Example 5×5 risk matrix (generic — substitute your own)

**Likelihood**

| Level | Descriptor | Rough guide |
|---|---|---|
| 5 | Almost certain | Expected to occur in most circumstances |
| 4 | Likely | Will probably occur |
| 3 | Possible | Could occur at some time |
| 2 | Unlikely | Could occur but not expected |
| 1 | Rare | Only in exceptional circumstances |

**Consequence (severity)**

| Level | Descriptor | Safety outcome |
|---|---|---|
| 5 | Catastrophic | Fatality / permanent disabling injury |
| 4 | Major | Serious injury, hospitalisation, long-term harm |
| 3 | Moderate | Medical treatment / lost-time injury |
| 2 | Minor | First aid injury |
| 1 | Insignificant | No / negligible injury |

**Risk score = Likelihood × Consequence**

| Score | Band | Typical response |
|---|---|---|
| 17–25 | Extreme | Stop / do not proceed without elimination or major control redesign and senior sign-off |
| 10–16 | High | Critical controls must be in place, verified, and signed off before work |
| 5–9 | Medium | Manage with documented controls and monitoring |
| 1–4 | Low | Manage by routine procedures |

> **Any credible fatal consequence is treated as critical** regardless of a low calculated
> likelihood — a "rare × catastrophic = 5" must not be waved through as merely *medium*. Score
> the matrix, but let the catastrophic consequence drive the assurance regime.

`../scripts/risk_matrix_scorer.py` implements this scheme deterministically (pre-control and
post-control), and applies the critical-consequence override, so scoring is repeatable rather
than done by eye. Always confirm the matrix in use matches the one the assessment is governed by.
