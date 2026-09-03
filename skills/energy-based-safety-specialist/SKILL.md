---
name: energy-based-safety-specialist
description: The subject-matter expert (SME) you consult for ENERGY-BASED SAFETY and the CHASNZ
  Energy Wheel — classifying hazards by their energy source, applying the ~1,500 joule
  high-energy threshold that separates "stuff that can kill you" from everything else, and
  testing whether a control is a true DIRECT control or only an alternate one. Use to run an
  energy-based hazard recognition sweep over a task or site, to challenge whether a fatal-risk
  control would still work when a competent person makes a mistake, or to set up HECA
  measurement in place of TRIR. Triggers on "energy wheel", "energy based safety",
  "energy-based hazard recognition", "EBHR", "high energy hazard", "high-energy", "1500
  joules", "STCKY", "stuff that can kill you", "direct control", "alternate control", "HECA",
  "high energy control assessment", "energy based observation", "EBO", "SIF", "serious injury
  and fatality", "SIF prevention", "potential SIF", "PSIF", "beyond TRIR", "safety
  classification and learning", "SCL model", "energy source", "CHASNZ", "Hallowell". Grounded
  in the CHASNZ guide "High Energy Hazards on Construction Sites in New Zealand" (v2.0, Feb
  2024) and the CSRA/EEI research behind it. Not legal advice.
---

# Energy-Based Safety Specialist

## Purpose

Apply the **energy-based safety** lens to NZ/AU work — the discipline of naming hazards by the
**energy** that would do the harm, sorting them by **energy magnitude** rather than by imagined
worst case, and holding controls to the **direct control** test. It answers three questions a
conventional hazard list does not:

1. **Which of these hazards can actually kill someone today?** (the ~1,500 J high-energy line)
2. **Is this control real, or is it a promise?** (targeted, effective, error-tolerant)
3. **How would we measure that at scale without waiting for injuries?** (HECA, not TRIR)

The core claim of the method: **energy magnitude predicts injury severity.** Below ~500 J the
most likely outcome is a first-aid injury; between 500 J and 1,500 J, a medical/lost-time case;
above ~1,500 J a **serious injury or fatality (SIF) becomes the most likely outcome, not the
remote one**. That is why "high energy" is a defensible filter and "worst possible outcome" is
not — a SIF is always *possible*, which makes it useless for prioritising.

## When to use

- Running an **energy-based hazard recognition** sweep over a task, permit, JSA or site walk —
  ten energy categories in turn, so no whole class of killing energy is missed.
- Deciding **whether a hazard is high-energy** — including calculating the energy magnitude when
  no rule of thumb applies (`scripts/energy_calculator.py`).
- **Testing an existing control set**: which controls survive the direct-control test, and which
  are alternate controls quietly carrying a fatal risk on their own.
- Designing or reviewing **HECA / energy-based observation (EBO)** as a leading measure, or
  arguing the case for moving beyond TRIR/LTIFR.
- Reviewing a **bow tie, JSA or SWMS** whose "controls" column is thick with training, signage
  and PPE.
- Classifying an event's **SIF potential** (was a high-energy hazard released, and was a direct
  control present?) rather than grading it by the injury that happened to result.

## When NOT to use

- Building the full threat → top event → consequence structure → `critical-risk-manager`
  (energy-based safety sharpens a bow tie; it does not replace it).
- Deciding the **legal** adequacy of controls, or what SFAIRP requires →
  `../worksafe-nz-specialist/` (NZ) or `../safework-au-specialist/` (AU) via `hse-advisor`.
- Root-causing an event that has already happened → `../incident-investigator/` (Five Whys) or
  `../complex-problem-analyst/` (Fishbone). Use this skill first only to classify the event's
  **energy and control status**, then hand off.
- The controls detail for one specific hazard (how to shore a trench, how to test a confined
  space atmosphere) → the relevant hazard SME. This skill classifies and challenges; the SMEs
  supply the engineering.

## Method

Load `references/energy-wheel.md` for the ten categories and `references/direct-controls.md`
for the control test. In brief:

1. **Scope the observation.** One crew, one task, at a point in time — energy-based safety
   assesses **work as observed**, not work as imagined or as documented. Hypothetical conditions
   are excluded (this is the discipline that stops the list becoming infinite).
2. **Walk the wheel.** Take the ten energy categories in turn — **gravity, mechanical, motion,
   sound, pressure, radiation, temperature, chemical, biological, electrical** — and ask what
   energy of that type is present in this task. The wheel exists because unaided hazard spotting
   is poor; workers typically identify well under half the hazards around them, and the misses
   cluster in whole categories nobody thought to look for.
3. **Classify each energy source as high or low energy.** Use the quick classifiers in
   `references/high-energy-thresholds.md` (a person above ~1.2 m, mobile plant in motion,
   >50 V, steam, fire with a fuel source, an unsupported excavation face ≥ 1.5 m, and so on).
   Where no classifier fits — a dropped tool, a hose under pressure, a hand tool — **calculate**
   with `scripts/energy_calculator.py` rather than guessing. Health hazards are high-energy when
   exposure **exceeds the workplace exposure standard**, not by joules.
4. **State the exposure.** Energy alone is not risk — a person has to be able to contact it.
   Note who is exposed and from whose point of view (a vehicle strike is high energy from the
   point of view of the worker on foot; a crash is assessed from the occupants' point of view).
5. **For each high-energy hazard, find its direct control.** A direct control must pass **all
   three** tests — targeted at that specific energy, effective (mitigating the energy below the
   threshold, or the exposure below the WES) when installed and verified, and **still effective
   when a person makes an unintentional mistake during the work**. One hazard may need more than
   one; one object may present more than one energy (a suspended load carries both gravity and
   lateral motion).
6. **Mark anything else as an alternate control.** Training, PPE, signage, temporary barriers,
   SOPs, permits, supervision, exclusion zones held by discipline alone. These are often
   necessary and are frequently the only thing available — but record them as **exposure**, not
   as coverage. **An alternate control never fills the gap left by a missing direct control.**
7. **Report the gaps.** Every high-energy hazard **without** a direct control is the finding.
   That list, not the hazard count, is the output that changes what happens on site.
8. **Optionally, score it.** Where this is a measurement programme rather than a one-off review,
   compute the HECA score and apply the observation rules in `references/heca-scl.md`.

**Watch for the two standard failure modes.** First, **energy inflation** — classifying
everything as high energy so the filter stops filtering (a 0.5 kg tool dropped 1 m is ~5 J, not
a SIF hazard). Second, **direct-control inflation** — recording a harness, a spotter, or an
"exclusion zone" as a direct control when it depends on someone doing the right thing every
time. The method only earns its keep if both definitions are applied strictly.

**Done when:** every energy category has been considered and either populated or explicitly
ruled out; each identified hazard is classified high or low energy with a stated reason or
calculation; every high-energy hazard has its direct control named and its verification status
recorded, or is flagged as an uncontrolled exposure; and alternate controls are listed
separately and never counted as coverage.

## Jurisdiction note

Energy-based safety is a **method, not a legal standard** — no NZ or AU statute mentions the
1,500 J threshold, direct controls, or HECA. It sits **inside** the existing duty, and does not
displace it.

- **NZ.** The duty is HSWA 2015 — eliminate risk **so far as is reasonably practicable
  (SFAIRP)**, otherwise minimise SFAIRP. The energy wheel is the NZ construction sector's
  articulation of good practice, published by **CHASNZ**, which WorkSafe NZ recognises as the
  industry guidance provider for construction. See `references/nz-gpg.md`.
- **AU.** There is no model WHS Code equivalent. Energy-based safety is used as a **supplement**
  to the model Codes of Practice, whose control expectations still set the compliance baseline.
  Use the wheel to find and pressure-test controls; use the Code to establish what is required.
- **Both.** The direct-control test is **stricter** than the hierarchy of controls, not a
  substitute for it. A control can be high on the hierarchy and still fail the error-tolerance
  test. Run the hierarchy for the legal frame; run the direct-control test for the survival
  frame. Where they disagree, satisfy both.

Treat all thresholds and citations as **verify-pointers**, and confirm the current CHASNZ
edition before relying on it.

## Output format

Produce, in this order:

1. **Header** — task/activity observed, crew, location type, jurisdiction, date, and
   "draft — requires competent-person review".
2. **Energy sweep table** — one row per energy source found, with columns: *Energy category |
   Energy source | Who is exposed | High or low energy (+ reason or calculation) | Direct
   control present? | Alternate controls in place*.
3. **Categories with nothing found** — listed explicitly, so the sweep is visibly complete
   rather than silently partial.
4. **Uncontrolled high-energy exposures** — the headline finding. For each: the energy, the
   exposure, what direct control is missing, and what would qualify as one.
5. **Alternate-control-only lines** — high-energy hazards carried by training/PPE/procedure
   alone, flagged as the risk they are.
6. **HECA score** (only if a measurement programme) — successes, exposures, score, and the
   sample it came from.
7. **Recommendations** — the direct controls to install, in priority order, with who verifies
   each and when.
8. **Disclaimer.**

## Hand-offs

- **Build the full risk story around a high-energy hazard** → `../critical-risk-manager/`.
  Energy-based safety identifies the energy and tests the barriers; the bow tie maps threats,
  consequences and escalation factors. The direct-control test is a sharper filter for
  nominating **critical controls** — see `../critical-risk-manager/references/control-assurance.md`.
- **Engineering detail for a specific energy** → the SME that owns it. Gravity/falls →
  `../working-at-height-specialist/`; mechanical & isolation → `../machinery-safety-specialist/`;
  motion/vehicles → `../mobile-plant-traffic-specialist/`; pressure →
  `../pressure-equipment-specialist/`; temperature, chemical & the WES →
  `../hazardous-substances-specialist/`; electrical → `../electrical-energy-specialist/`;
  gravity in trenches → `../excavation-specialist/`; suspended loads →
  `../lifting-rigging-specialist/` and `../crane-specialist/`.
- **The construction-sector regime** (principal contractor, SWMS/HRCW, site induction) →
  `../construction-specialist/`.
- **Turn the direct controls into a procedure** → `../sop-author/`; **into a task-level JSA** →
  `../task-analysis-author/`.
- **A high-energy hazard was released in a real event** → `../incident-investigator/`.
- **Workload, fatigue, stress and impairment.** These are **not** energy sources and have no
  place on the wheel — but they strongly modify the likelihood of the human error the
  direct-control test assumes. Route them to `../psychosocial-risk-specialist/` and treat them
  as a reason to demand direct controls, not as hazards to score.

## Disclaimer

This skill produces a structured hazard-recognition and control-assessment **draft — not legal
advice, and not a verified control set**. Energy thresholds and classifiers are decision aids
drawn from published research and industry guidance; they are not statutory tests, and no
calculated joule figure determines whether a duty has been met. A competent H&S person must
validate every classification, exposure and control against the actual site, plant, people and
the current law, codes and standards before use.
