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

`scripts/risk_matrix_scorer.py` implements this scheme deterministically (pre-control and
post-control), and applies the critical-consequence override, so scoring is repeatable rather
than done by eye. Always confirm the matrix in use matches the one the assessment is governed by.
