# HECA — measuring safety without waiting for injuries

**High-Energy Control Assessments (HECA)** turn the energy wheel from a hazard-spotting aid into a
**leading measure**. Used at step 8 of the method in `../SKILL.md`, and whenever the question is
"how do we measure this at scale?" or "why shouldn't we use TRIR/LTIFR?".

> **Sources last verified: 2026-09-03.** After Erkal & Hallowell, *Moving Beyond TRIR — Measuring
> and Monitoring Safety Performance With High-Energy Control Assessments*, Professional Safety
> 68(05) 2023, and the EEI **Safety Classification and Learning (SCL) Model** (2020). Verify-pointers
> — summarised, not reproduced. **Not legal advice.**

## The problem it solves

Recordable-injury rates have fallen for decades while **SIF rates have plateaued**. The
accumulating evidence is that SIFs have *different causes* from minor injuries — so driving down
cuts and sprains does not drive down fatalities. Worse, injury rates are:

- **lagging** — you learn by hurting someone;
- **rare** — a single business unit never accumulates enough SIF data to see a pattern;
- **perverse** — they reward under-reporting and punish honest reporting.

HECA measures the thing that actually prevents fatalities: **the presence of adequate controls on
life-threatening hazards during normal work.** Its founding idea is that *safety is the presence of
safeguards*, not the absence of incidents.

## The measurement

Three steps, during an **energy-based observation (EBO)** of real work in progress:

1. Identify every **high-energy hazard** the crew faces (`high-energy-thresholds.md`).
2. For each, mark whether a **direct control** is present (`direct-controls.md`).
3. Compute the score.

```
                        Success
HECA  =  ─────────────────────────────────────
              Success  +  Exposure
```

- **Success** — a high-energy hazard *with* a corresponding direct control.
- **Exposure** — a high-energy hazard *without* one.

The score is **the percentage of life-threatening hazards that are properly controlled**. It is
computed per crew, per task, at a point in time.

**If no high-energy hazards were observed, do not compute a score.** Recording it as zero is the
most common corruption of the metric — an absence of high energy is not a failure, and a zero will
pollute every aggregate it enters.

## The observation rules

These exist to make scores comparable between observers, crews and companies. Applied loosely, the
number means nothing.

1. HECA is based on **observation of active work** — not on paperwork review or incident
   classification.
2. **One measurement = one crew, one task, one working day.** Multiple crews or tasks require
   multiple measurements.
3. If a crew performs more than one task in the period, score **each task separately**.
4. Two or more crews working **in proximity on the same task** are grouped as **one** measurement.
5. Two hazards sharing the **same energy source and the same direct control** are combined into one
   entry.
6. A direct control with a **deficiency or a coverage gap** is recorded as **exposure**. No partial
   credit.
7. Score **work as observed** — never hypothetical, anticipated or speculated conditions.
8. **One object may carry more than one high-energy hazard** (a suspended load = gravity + lateral
   motion).
9. Observers must make **reasonable efforts to verify** that direct controls are installed and used
   properly — looking is not the same as verifying.
10. The definitions of *high energy* and *direct control* must be applied **strictly**. Drift in
    either definition destroys comparability.

**Equipment-specific rules.** Two or more reasonably similar machines on the same task count as one
entry. Where equipment forms part of a direct control, make a reasonable effort to confirm it is
maintained. Consider the equipment/environment interaction (plant tracking near workers on foot)
and whether it is operating **within its engineered limits** (lift capacity, boom limits, ground
stability). **The internal integrity of electrical, engine and hydraulic systems is out of scope** —
most safety observers cannot assess it, so ask the people who maintain it rather than assuming.

## Record more than the number

The score alone is nearly useless for learning. For each observation, record:

- which high-energy hazards were present;
- which had direct controls, and which did not;
- **why** a control was absent — never installed, unavailable, available but not used, installed
  but deficient;
- what the observer **did about the exposure at the time**.

That "why" field is where the systemic finding lives. Ten exposures because the control does not
exist is a procurement and design problem; ten because it was available and unused is a
supervision, planning or production-pressure problem. The score cannot tell them apart.

## Sampling — how much is enough

Not every crew on every day. HECA is a **sampling** method: a representative subset supports
conclusions about the whole organisation.

A workable estimate of the *population* (the number of assessment opportunities in a month):

```
HECA opportunities per month  ≈  field worker-hours per month  ÷  (200 hours × 3 workers per crew)
```

So a business unit with 300,000 field worker-hours in a month has roughly **500** opportunities.
From that population, apply standard sample-size formulas at your chosen confidence level (with a
typical 5% standard error) to get the number of observations needed.

**Sample representatively, not conveniently.** A sample skewed toward the accessible, the tidy and
the well-run yard produces a flattering number that is simply wrong. Pick sites and crews
deliberately across work type, geography, contractor and shift.

**Do not pool data across contractors with inconsistent collection practices** — an aggregate built
from differently-applied definitions is not a measurement.

## Guarding the metric

Any safety number becomes a target and then stops measuring. HECA's specific vulnerabilities:

- **Definition drift** — quietly widening "direct control" until scores rise. This is the main one.
- **Selection bias** — observing the easy work.
- **Zero-hazard padding** — recording observations with no high-energy hazards to inflate averages.
- **Score-chasing** — treating HECA as a KPI to hit rather than a picture to learn from. The
  research is explicit that manipulation-resistance is still an open problem.

The defence is the same in every case: publish the **exposures and their reasons**, not just the
percentage, and audit a sample of observations against the strict definitions.

## The SCL model — classifying events by energy, not by outcome

The **Safety Classification and Learning (SCL) model** is the companion idea on the *incident* side.
Instead of grading an event by the injury that happened to result, it classifies by **whether
high energy was present and whether a direct control was there**:

- **Success** — a high-energy incident did *not* occur **because a direct control was present**.
  Explicitly worth recording and learning from. Conventional systems record nothing here.
- **Exposure** — high energy was present **with no direct control**. A near-miss in the only sense
  that matters, whether or not anyone was hurt.
- **SIF / potential SIF (PSIF)** — an actual serious injury or fatality, or an event that could
  most likely have been one.

The practical consequence: **a cut finger sustained while a high-energy hazard sat uncontrolled is
a SIF-potential event, and a fatality-free day on an uncontrolled site is not a success.** Outcome
severity and energy severity are different axes, and only the second one predicts the next
fatality. This is the discipline to import into event classification and into board reporting —
see `../../officer-governance-advisor/` for how leading indicators should reach an officer, and
`../../incident-investigator/` once an event needs root-causing.

## Standing this up

A realistic sequence for an organisation adopting it:

1. **Train observers on the two definitions** — high energy and direct control — and calibrate them
   against each other on the same real task until they agree. Uncalibrated observers produce
   incomparable data.
2. **Run EBOs without scoring** for a period. Let people find that their exclusion zones and
   spotters are alternate controls before any number is attached to it.
3. **Publish the exposure list, not the score,** for the first cycle.
4. **Fix the direct controls** that repeatedly turn out to be missing — usually a small number of
   recurring engineering and procurement decisions.
5. **Then start scoring and sampling**, with the guards above.

Adopting the score before the definitions are calibrated produces a confident number describing
nothing.
