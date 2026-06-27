# Bow tie methodology

The full method for building a bow tie risk assessment, as applied to NZ/AU critical (fatal)
workplace risks. The bow tie is a single-hazard, single-top-event diagram that makes the risk
story legible: how a hazard can be released, what stops it, what happens if it is, and what
limits the harm. Method aligns with the barrier-based bow tie approach widely used in heavy
industry, utilities and construction (e.g. the structured approach described by Aust & Pons,
*Bowtie Methodology for Risk Analysis*, 2020).

## Anatomy of a bow tie

```
 THREATS        preventive controls      TOP EVENT      mitigating controls     CONSEQUENCES
 (causes)   →  [C] [C] [C]          →   (loss of    →   [C] [C] [C]         →   (outcomes)
                                          control)
                    ↑                                        ↑
              escalation factor                       escalation factor
              + its control                           + its control
```

- **Hazard** — the source of harm / stored energy. Sits behind the whole diagram. One per bow tie.
- **Top event** — the single point where control of the hazard is lost. The knot of the bow tie.
- **Threats** — the left side. Independent credible causes that could each lead to the top event.
- **Consequences** — the right side. Credible outcomes if the top event occurs.
- **Preventive (proactive) controls** — barriers on each threat line, *before* the top event.
- **Mitigating (reactive/recovery) controls** — barriers on each consequence line, *after* the
  top event.
- **Escalation factors** — conditions that defeat or weaken a specific control.
- **Escalation factor controls** — barriers that manage an escalation factor.

## Step-by-step

### 1. Name the hazard
State the hazard as a source of energy or harm, not as an activity. "Suspended load",
"stored hydraulic pressure", "gravity / working at height", "uncontrolled traffic interaction",
"electrical energy", "respirable crystalline silica". One hazard per bow tie — if you have two
energies, build two bow ties.

### 2. Define the top event
The top event is the moment of **loss of control** of that hazard — released, but harm not yet
done. Tests:
- It is caused by the threats and causes the consequences (it sits in the middle).
- It is realistic and specific: "load falls from crane", "person falls from height", "vehicle
  enters work zone", "uncontrolled release of stored pressure".
- It is **not** the hazard ("suspended load") and **not** the consequence ("fatality").

A common failure is choosing a top event too early (a threat) or too late (a consequence). See
`critical-risk-definitions.md`.

### 3. Identify threats (left side)
List every **credible** way the top event could occur. Each is an independent pathway. Examples
for "load falls from crane": rigging failure, overload, mechanical/structural failure, operator
error, ground failure/outrigger collapse, two-blocking, contact with services.
- Keep threats as direct causes of the top event, not root causes (root causes belong to
  investigation methods, not the bow tie).
- Aim for completeness of *credible* threats, not an exhaustive list of the implausible.

### 4. Identify consequences (right side)
List the credible outcomes if the top event occurs. For a critical risk, include the **worst
credible consequence** (usually a fatality or permanent disability). Other consequences may
include serious injury, property/plant damage, environmental release, business disruption.
Separate distinct outcomes onto separate lines — each gets its own mitigating controls.

### 5. Add preventive controls (threat lines)
On each threat line, place the barriers that stop that threat reaching the top event. Apply the
**hierarchy of controls** top-down:

1. **Elimination** — remove the hazard (don't lift it; design out the work at height).
2. **Substitution** — a less hazardous alternative.
3. **Engineering / isolation** — guards, interlocks, exclusion by physical means, rated
   equipment, load-moment indicators, fall-arrest anchors.
4. **Administrative** — procedures, permits, competency, exclusion zones by signage, supervision.
5. **PPE** — last line, protects one person, fails quietly.

Prefer **hard** controls (elimination/engineering) over **soft** ones (administrative/PPE). A
critical-risk threat line carried only by administrative + PPE controls is weak — flag it.

### 6. Add mitigating controls (consequence lines)
On each consequence line, place barriers that reduce the severity if the top event has occurred:
exclusion zones / no-go areas under loads, emergency response and rescue plans, first aid /
trauma care, emergency shutdown, spill response, alarms and evacuation.

### 7. Identify critical controls
A **critical control** is one whose failure (alone or with one other failure) would most likely
result in a fatality. There are usually only a handful per bow tie. Flag them explicitly — they
carry the risk and demand the highest assurance. (See `critical-risk-definitions.md` for the
test, and `control-assurance.md` for verifying them.)

### 8. Add escalation factors and their controls
For important controls — especially critical ones — ask "what would defeat this control?" Each
answer is an **escalation factor**: competency lapse, fatigue, interlock bypassed/defeated,
inspection overdue, complacency, weather, poor communication. Add the control that manages the
escalation factor (refresher training, fatigue management, bypass governance, inspection regime).
Escalation factors are where many real failures live — do not skip them on critical controls.

### 9. Quality checks before you finish
- Is the top event a genuine loss-of-control, not a cause or an outcome?
- Is each threat independent and credible? Each consequence distinct?
- Does every threat line have at least one **effective** preventive control? Every consequence
  line at least one mitigating control?
- Are critical controls flagged, and is at least one a **hard** control where reasonably
  practicable?
- Have escalation factors been considered for each critical control?
- Are any lines carried only by "be careful" (administrative) + PPE? Challenge them.
- Have you avoided double-counting one control as if it were several?

## Common pitfalls

- **Top event chosen as a threat or a consequence.** The most frequent error.
- **Generic control soup.** Twenty weak controls do not equal one good one; name real,
  verifiable barriers.
- **Administrative/PPE reliance on a fatal risk.** A defensibility and assurance problem.
- **Controls with no owner or no verification** — looks complete on paper, fails in reality.
- **Confusing the bow tie with an investigation** — the bow tie is prospective (could happen);
  Five Whys / Fishbone are retrospective (did happen).
