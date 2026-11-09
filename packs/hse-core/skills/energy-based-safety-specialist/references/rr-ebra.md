# Risk Remaining (RR) and Energy-Based Risk Assessment (EBRA)

How to rate the protection a high-energy hazard actually has, including when no direct control is
feasible, and how to weight that by how long and how many people are exposed. Used at step 8 of
the method in `../SKILL.md`, and whenever work is being **planned** rather than observed.

> **Sources last verified: 2026-11-09.** CSRA (Construction Safety Research Alliance, University
> of Colorado), *Energy-Based Risk Assessment (EBRA)* report (2026) and *Risk Reduction Model*
> v1.5, both at https://www.csra.colorado.edu/projects/energy-based-risk-assessment/. Raheemy,
> Sherratt & Hallowell (2026), *What makes a safety control "enough" for high-energy hazards?*,
> Journal of Safety Research 98, 376–389. Values summarised with attribution, not reproduced.
> **Not legal advice.**

## Three measures, three jobs

| Measure | Question it answers | When | Result |
|---|---|---|---|
| **HECA** | Does each high-energy hazard have a direct control? | Observing work in progress | % of hazards with a direct control (yes/no for each) |
| **RR** | How much protection does this control set give? | Planning, pre-task, or observing | 0–100% risk remaining for each hazard |
| **EBRA** | Where is the remaining risk concentrated once time and headcount count? | Planning and pre-task; comparing work methods | A relative index: the sum across hazards |

**CSRA is explicit that HECA stays the primary monitoring measure.** RR and EBRA add detail where
HECA can only say "exposure"; they do not replace it. Report HECA alongside RR/EBRA whenever you
have both. A hazard with a good RR is still a HECA exposure.

## Step 1: classify the control configuration

### Direct controls come in two kinds

The four direct-control rules are in `direct-controls.md`. RR then asks *how* the control works:

- **DC-E (eliminates).** The exposure is gone: the energy is removed, or nobody can reach it.
  Examples: verified isolation and proving dead; substitution; engineered hard barricades that keep
  everyone out of a lift's drop and swing zone (CSRA's own example).
- **DC-M (mitigates or isolates).** The energy is still there, but the person is protected so a
  SIF is no longer the most likely outcome. Examples: guardrails, machine guards, a trench shield,
  and a properly designed, inspected and connected personal fall-arrest system (CSRA rates this
  DC-M).
- **If unsure, use DC-M.** It is the conservative choice.

### When no direct control is feasible: the three qualifying alternate controls

"Alternate control" (the CHASNZ term) means anything that is not a direct control. CSRA's 2026
work defines which alternate controls earn credit. It calls them *Alternative Controls*; this skill
calls them **qualifying alternate controls**, so they aren't confused with the broader term. There
are three kinds:

| Kind | What it is | CSRA's examples |
|---|---|---|
| **Physical obstacle (PO)** | Something in the way that blocks or slows the path to the energy | Cones with toppers, barrier or danger tape, temporary fencing, stanchions |
| **Dedicated monitoring (DM)** | Continuous attention devoted to that one hazard | A qualified spotter, a flagger, proximity detection, a dedicated alarm, a gas monitor used for that hazard |
| **Visual reminder (VR)** | A visible warning that the hazard is there | Hazard-specific signs, temporary traffic signals, marked boundaries |

**Everything else is a supporting activity**: training, procedures, permits, JSAs, toolbox talks,
experience, general rules, the worker's own situational awareness, and most PPE. These are
needed, but they earn **no** RR credit on their own.

### The five rules for an alternative control system (ACS)

Two qualifying alternate controls make an acceptable ACS only if **all five** hold:

1. **A direct control has been found not feasible** for this specific hazard. Record why.
2. **Two controls, from two different kinds.** Two physical obstacles are not a system: they share
   the same ways of failing.
3. **Each is aimed at this hazard.** Protection a control gives by accident doesn't count.
4. **Everyone who creates or is exposed to the hazard** has verified training specific to the
   hazard and its controls, a safe work plan that covers both, and a quality pre-job brief that
   discusses both.
5. **The controls are in place for the whole time the exposure exists.**

The three pairings are **ACS1 = PO + DM**, **ACS2 = PO + VR** and **ACS3 = VR + DM**.

The research added tests for common safeguards:

- **Spotter.** Watching the hazard is their only job for the whole exposure, they keep in
  continuous contact with the workers involved, and they are not exposed themselves.
- **Flagger.** Their attention is dedicated to that specific hazard.
- **Communication.** Clear, unambiguous, uninterrupted, specific to the hazard, and reaching
  everyone who creates or is exposed to it.
- **Signs.** They tell workers something meaningful about an unusual, hidden or unexpected hazard,
  in language and at a literacy level the crew can understand.

The most common failure is a spotter who has other jobs. That spotter earns nothing.

## Step 2: assign the Risk Remaining

Work down this order (it follows CSRA's Risk Reduction Model flowchart) and stop at the first
match:

| Control configuration | Risk Remaining |
|---|---|
| Direct control that **eliminates** the exposure (DC-E) | ~0% |
| Direct control that **mitigates or isolates** it (DC-M) | 5% |
| **ACS1**: physical obstacle + dedicated monitoring | 20% |
| **ACS2** (PO + VR) or **ACS3** (VR + DM) | 30% |
| A **single** physical obstacle or dedicated monitoring | 45% |
| A **visual reminder only** | 67% |
| **No qualifying control** | 100% |

**Where the numbers come from.** A Delphi panel of 21 safety experts rated each configuration over
two rounds. Agreement had to reach 70% for direct controls, and an average absolute deviation of 10
or less on a 10–90 scale for the ACS values. The single-control values were then derived from the
ACS values by simultaneous equations. They behave like products of independent layers: 45% × 45% ≈
20%, and 45% × 67% ≈ 30%. That is why two controls of the same kind don't make a system.

**These are relative weights, not probabilities.** CSRA says so directly. Never present "20%" as
"a one-in-five chance of a fatality".

### Cases the source doesn't settle (this skill's conventions)

State these as conventions whenever you use them. `../scripts/ebra_calculator.py` applies them and
flags each one:

- **A pairing is present but rule 1, 4 or 5 fails.** It is not an ACS. Score the strongest single
  control present (45% or 67%) and record which rule failed. If a direct control is feasible, the
  finding is the missing direct control, not the score.
- **All three kinds present (PO + DM + VR).** Score ACS1 (20%). CSRA gives no further credit, so
  don't multiply.
- **A direct control is present but deficient** (a missing part, unverified, or not used as
  designed). It is absent. Score whatever qualifying alternate controls remain.
- **Health hazards judged against the workplace exposure standard** (silica, noise, chemicals).
  CSRA frames RR and EBRA entirely around physical energy of 1,500 J or more. Use HECA's yes/no
  for these, and apply RR only with stated reasoning.
- **One object carrying two energies** (a suspended load can fall and swing). Score each hazard
  separately, as CSRA does.

## Step 3: EBRA adds time and headcount

- **Duration (D):** the share of the work period someone is exposed to this hazard. Use only the
  three standard categories so assessments stay comparable: **full shift = 1.0**, **part shift =
  0.5**, **momentary = 0.1**.
- **Workers exposed (W):** the people **directly exposed to this hazard**, not the crew size.
  Count only those inside the exposure conditions. One person can count against several hazards.

```
EBRA  =  Σ over each high-energy hazard ( RR × D × W )
```

Calculate it with `../scripts/ebra_calculator.py`, not by hand. The script also reports HECA and
ranks the largest contributors.

Planned work takes judgement on D and W. CSRA accepts this: EBRA is a structured estimate, not a
measurement. Give the reasoning for each value so someone else can check it.

## Reading the result

- **Lower is less relative risk remaining.** EBRA has no units and is not a probability.
- **The value is in each hazard's contribution, not the total.** Ask which hazard dominates, and
  whether the control (RR), the time (D) or the headcount (W) is driving it. A hazard with the same
  RR as others can dominate because more people are exposed for longer.
- **There are three levers, in this order:**
  1. A stronger control: single → ACS → direct; DC-M → DC-E.
  2. Shorter exposure.
  3. Fewer people exposed.

  Shorter exposure and fewer people **never stand in for a control that's needed**. CSRA says
  this, and so does the duty to eliminate first.
- **A good total doesn't clear anything.** Any hazard with people exposed at 100% (no qualifying
  control) is a stop-work finding, however small its contribution. A low total doesn't show each
  hazard is adequately controlled.
- **Baselines.** Repeated EBRAs of the same task build a typical range, and a day well above it
  is a signal to look again. Only compare EBRAs assessed under the same rules for identifying
  hazards, classifying controls, D and W.

## Worked example (illustrative)

A water-main renewal in a suburban street, over one shift. The plan as first written:

| High-energy hazard | Control configuration | RR | D | W | RR × D × W |
|---|---|---|---|---|---|
| Trench collapse (pipe-layers in a 1.8 m trench) | Trench shield, installed and inspected: DC-M | 5% | 0.5 | 2 | 0.050 |
| Excavator slew striking workers on foot | Cones with toppers + tape around the slew radius, and a spotter whose only job is the slew, in radio contact: ACS1 | 20% | 0.5 | 3 | 0.300 |
| Live traffic striking workers at the trench edge | Cones and signs per the traffic management plan: ACS2 | 30% | 1.0 | 2 | 0.600 |
| Pipe lifted by the excavator (worker guiding it into the trench) | Tag line only: no qualifying control | 100% | 0.1 | 1 | 0.100 |
| **EBRA total** | | | | | **1.050** |

**HECA: 1 of 4 = 25%.** Live traffic is 57% of the total (alternate controls only, all shift).
The pipe lift is only 10% of the total, but it is a **stop-work finding**: someone is under a
suspended load with nothing qualifying.

**Two challenges before scoring the ACS2 line:**
- **Rule 1.** Would a rigid temporary barrier fit the site? If so, cones and signs are not an
  acceptable ACS, and the reasonably practicable duty would likely require the barrier anyway.
- **Rule 4.** Was the traffic hazard actually covered in the pre-job brief?

**The revised plan:**
- A rigid barrier on the live-lane side (DC-M): 0.05 × 1.0 × 2 = 0.100.
- The pipe is landed with nobody in the trench or the drop zone, and the drop zone is
  hard-barricaded (DC-E, W = 0): 0.
- The work is sequenced so only one person works inside the slew radius: 0.20 × 0.5 × 1 = 0.100.

**New total 0.250, HECA 3 of 4 = 75%.** The remaining contributor is the excavator. Engineered
separation (DC-M) is the next lever if the site allows it.

## Guarding the numbers

- **ACS inflation.** Calling any cones-plus-spotter arrangement ACS1 without checking all five
  rules. Check the spotter's other duties, the pre-job brief, and whether a direct control was
  feasible.
- **Shrinking D and W.** Calling exposure "momentary", or counting only the person nearest the
  hazard. W is everyone inside the exposure conditions.
- **"Our score is low" as a reason not to install a direct control.** Rule 1 and the duty to
  eliminate first both point the other way.
- **Comparing EBRAs assessed differently.** If the hazard-identification or classification rules
  differ, the comparison means nothing.
- **Presenting RR as a probability.**

## Jurisdiction

RR and EBRA are a **prioritisation method, not a legal test**. Their values are expert consensus,
not measured injury rates. In NZ (HSWA 2015) and AU (model WHS Act) the duty is unchanged:
eliminate risk so far as is reasonably practicable, otherwise minimise it. Rule 1 (rule out a
direct control first) lines up with that duty. A low EBRA never shows the duty has been met, and
an alternative control system is not a defence where a direct control was reasonably practicable.
CHASNZ's v2.0 guide (February 2024) predates this work; check whether a later edition adopts it.
See `nz-gpg.md`.
