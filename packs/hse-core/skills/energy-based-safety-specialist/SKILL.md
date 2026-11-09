---
name: energy-based-safety-specialist
description: Energy-based safety and the CHASNZ Energy Wheel — sweep a task for energy sources,
  classify hazards against the ~1,500 J high-energy (STCKY/SIF) threshold, test direct
  controls, score HECA, and rate risk remaining (CSRA RR/EBRA) when planning work.
---

# Energy-Based Safety Specialist

## Purpose

Apply the **energy-based safety** lens to NZ/AU work — the discipline of naming hazards by the
**energy** that would do the harm, sorting them by **energy magnitude** rather than by imagined
worst case, and holding controls to the **direct control** test. It answers four questions a
conventional hazard list does not:

1. **Which of these hazards can actually kill someone today?** (the ~1,500 J high-energy line)
2. **Is this control real, or is it a promise?** (targeted, effective, error-tolerant)
3. **How would we measure that at scale without waiting for injuries?** (HECA, not TRIR)
4. **Where there is no direct control, how much risk is left, and what should change first?**
   (CSRA's Risk Remaining and Energy-Based Risk Assessment, RR/EBRA)

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
- **Planning work or comparing work methods before work starts.** Rate the risk remaining for each
  high-energy hazard (direct control, alternative control system, single control, or nothing),
  then weight it by exposure time and headcount (`references/rr-ebra.md`,
  `scripts/ebra_calculator.py`).
- Reviewing a **bow tie, JSA or SWMS** whose "controls" column is thick with training, signage
  and PPE.
- Classifying an event's **SIF potential** (was a high-energy hazard released, and was a direct
  control present?) rather than grading it by the injury that happened to result.

## When NOT to use

- Building the full threat → top event → consequence structure → `critical-risk-manager`
  (energy-based safety sharpens a bow tie; it does not replace it).
- Deciding the **legal** adequacy of controls, or what SFAIRP requires →
  `worksafe-nz-specialist` (NZ) or `safework-au-specialist` (AU) via `hse-advisor`.
- Root-causing an event that has already happened → `incident-investigator` (Five Whys) or
  `complex-problem-analyst` (Fishbone). Use this skill first only to classify the event's
  **energy and control status**, then hand off.
- The controls detail for one specific hazard (how to shore a trench, how to test a confined
  space atmosphere) → the relevant hazard SME. This skill classifies and challenges; the SMEs
  supply the engineering.

## Method

Load `references/energy-wheel.md` for the ten categories and `references/direct-controls.md`
for the control test. In brief:

1. **Scope it and pick the mode.** One crew, one task, at a point in time. When **observing**
   work in progress, assess **work as observed**, not work as imagined or as documented, and leave
   hypothetical conditions out. That discipline stops the list becoming infinite. When
   **planning** (a work method, SWMS or pre-task brief before the work starts), assess the hazards
   and controls the plan anticipates, and use RR/EBRA at step 8.
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
4. **State the exposure.** Energy alone is not risk: a person has to be able to contact it.
   Note who is exposed, from whose point of view, how many people, and for how long (full shift,
   part shift or momentary). A vehicle strike is high energy from the point of view of the worker
   on foot; a crash is assessed from the occupants' point of view.
5. **For each high-energy hazard, find its direct control.** A direct control must pass **all
   four** rules in `references/direct-controls.md`:
   - targeted at that specific energy;
   - effective, so a SIF is no longer the most likely outcome;
   - installed, verified and used properly (if it isn't, it is absent);
   - **still effective when a person makes an unrelated mistake during the work**.

   Say whether it **eliminates** the exposure (DC-E) or **mitigates or isolates** it (DC-M). One
   hazard may need more than one direct control. One object may present more than one energy: a
   suspended load carries both gravity and lateral motion.
6. **Where there is no direct control, record why, then sort what's left.** Only three kinds of
   alternate control earn credit in CSRA's model: **physical obstacle, dedicated monitoring and
   visual reminder**. Two of different kinds that meet the five rules in `references/rr-ebra.md`
   form an **alternative control system**. Training, procedures, permits, briefings and most PPE
   are supporting activities: needed, but not controls on their own. **No alternate control
   equals a direct control.** HECA records the hazard as an exposure regardless, and RR gives
   partial credit only.
7. **Report the gaps.** Every high-energy hazard **without** a direct control is the finding.
   That list, not the hazard count, is the output that changes what happens on site.
8. **Score it where the job calls for it.**
   - **Observation programme:** compute HECA and apply the observation rules in
     `references/heca-scl.md`.
   - **Planning, or ranking a set of exposures:** give each hazard its Risk Remaining and compute
     the EBRA total (`references/rr-ebra.md`). Run `scripts/ebra_calculator.py` rather than
     calculating by hand.

   Report HECA alongside RR/EBRA when you have both, because CSRA keeps HECA as the primary
   monitoring measure.

**Watch for the three standard failure modes.**
- **Energy inflation:** classifying everything as high energy so the filter stops filtering. A
  0.5 kg tool dropped 1 m is ~5 J, not a SIF hazard.
- **Direct-control inflation:** recording a spotter, a permit or a taped "exclusion zone" as a
  direct control when it depends on someone doing the right thing every time.
- **Alternative-control-system inflation:** calling any cones-plus-spotter arrangement an
  alternative control system without checking the five rules. A spotter with other duties is the
  usual failure.

The method only earns its keep if all three definitions are applied strictly.

**Done when:**
- every energy category has been considered and either populated or explicitly ruled out;
- each identified hazard is classified high or low energy with a stated reason or calculation;
- every high-energy hazard has its direct control named (DC-E or DC-M) and its verification
  status recorded, or is flagged as an uncontrolled exposure;
- alternate controls are listed separately and never counted as coverage;
- where RR/EBRA was used, each hazard has its control configuration, RR, duration and headcount
  recorded, and the script computed the total.

## Jurisdiction note

Energy-based safety is a **method, not a legal standard**. No NZ or AU statute mentions the
1,500 J threshold, direct controls, HECA or EBRA. It sits **inside** the existing duty and does
not displace it. Risk Remaining values are expert-consensus weights, not legal or statistical
measures, and a low EBRA total never shows that a duty has been met.

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
2. **Energy sweep table**: one row per energy source found, with these columns:
   - Energy category
   - Energy source
   - Who is exposed (how many, how long)
   - High or low energy (with the reason or calculation)
   - Direct control (DC-E, DC-M or none)
   - Alternate controls in place (PO, DM, VR or supporting)
3. **Categories with nothing found**, listed explicitly so the sweep is visibly complete rather
   than silently partial.
4. **Uncontrolled high-energy exposures**: the headline finding. For each, give the energy, the
   exposure, what direct control is missing, and what would qualify as one. Lead with any hazard
   that has people exposed and no qualifying control at all.
5. **Alternate-control-only lines**: high-energy hazards carried by an alternative control
   system, a single control or supporting activities alone, flagged as the risk they are.
6. **Scores**, only what the mode calls for:
   - HECA (observation programme): successes, exposures, the score, and the sample it came from;
   - RR and EBRA (planning): each hazard's RR, D, W and contribution, the total, and the largest
     contributors.
7. **Recommendations**: the direct controls to install, in priority order (largest EBRA
   contributors and any 100% lines first), with who verifies each and when. Where no direct
   control is feasible, give the next step up the RR ladder and any cut in exposure time or
   headcount.
8. **Disclaimer.**

## Hand-offs

- **Build the full risk story around a high-energy hazard** → `critical-risk-manager`.
  Energy-based safety identifies the energy and tests the barriers; the bow tie maps threats,
  consequences and escalation factors. The direct-control test is a sharper filter for
  nominating **critical controls**; see `../critical-risk-manager/references/control-assurance.md`.
  For a high-energy hazard with no feasible direct control, give the RR rating alongside the
  bow tie's matrix score, because it separates an alternative control system from a sign on a
  fence in a way a 5×5 score cannot.
- **Engineering detail for a specific energy** → the SME that owns it. Gravity/falls →
  `working-at-height-specialist`; mechanical & isolation → `machinery-safety-specialist`;
  motion/vehicles → `mobile-plant-traffic-specialist`; pressure →
  `pressure-equipment-specialist`; temperature, chemical & the WES →
  `hazardous-substances-specialist`; electrical → `electrical-energy-specialist`;
  gravity in trenches → `excavation-specialist`; suspended loads →
  `lifting-rigging-specialist` and `crane-specialist`.
- **The construction-sector regime** (principal contractor, SWMS/HRCW, site induction) →
  `construction-specialist`.
- **Turn the direct controls into a procedure** → `sop-author`; **into a task-level JSA** →
  `task-analysis-author`.
- **A high-energy hazard was released in a real event** → `incident-investigator`.
- **Workload, fatigue, stress and impairment.** These are **not** energy sources and have no
  place on the wheel — but they strongly modify the likelihood of the human error the
  direct-control test assumes. Route them to `psychosocial-risk-specialist` and treat them
  as a reason to demand direct controls, not as hazards to score.

## Disclaimer

This skill produces a structured hazard-recognition and control-assessment **draft — not legal
advice, and not a verified control set**. Energy thresholds and classifiers are decision aids
drawn from published research and industry guidance; they are not statutory tests, and no
calculated joule figure determines whether a duty has been met. A competent H&S person must
validate every classification, exposure and control against the actual site, plant, people and
the current law, codes and standards before use.
