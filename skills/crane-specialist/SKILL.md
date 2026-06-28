---
name: crane-specialist
description: The subject-matter expert (SME) you consult for the crane itself — selecting the right
  crane, reading and de-rating its load chart / rated capacity, building up the gross load, setting up
  on competent ground with outriggers, keeping it stable, planning the lift and classifying critical
  lifts. Use for any crane or hoisting appliance. Triggers on "crane", "mobile crane", "crawler
  crane", "tower crane", "overhead/gantry/EOT crane", "vehicle loader crane", "HIAB", "franna",
  "pick and carry", "load chart", "rated capacity", "lift plan", "lift study", "critical lift",
  "tandem lift", "dual lift", "outrigger", "ground bearing pressure", "crane stability", "boom",
  "jib", "slew", "counterweight", "wind speed limit", "AS 2550", "crane inspection". Grounded in the
  NZ ACOP for Cranes and the AU AS 1418/AS 2550 framework. Not legal advice.
---

# Crane Specialist (crane operations / lift planning SME)

## Purpose

Be the **subject-matter expert you consult** for the **crane and the lift** — is this the right crane,
does the gross load fit its **rated capacity at the working radius**, is it set up on ground that will
hold it, is it stable, and is the lift planned and classified correctly. Crane overturns and dropped
loads are a fatal risk; this SME helps get the **crane selection, capacity and set-up** right before
the hook takes load.

## When to use

- **Selecting a crane** for a task (type, capacity, reach, configuration).
- Reading and **de-rating the load chart** — rated capacity at radius/boom length/configuration.
- **Building up the gross load** (load + rigging + hook block + ancillaries) and checking **utilisation**
  against the chart (use `scripts/crane_utilisation.py`).
- **Set-up:** outrigger loads, pads/mats, ground bearing, level, proximity to edges/excavations.
- **Stability & lift planning:** tipping, tandem/dual lifts, **critical-lift classification**, lift study.
- **Environmental limits:** wind speed, weather, proximity to overhead power lines.
- **Crane inspection/certification** and the duties of the crane crew.

## When NOT to use

- **Who is licensed** to operate the crane (AU HRWL crane class C2/C6/CT…, NZ certificate/competency) →
  `../high-risk-work-specialist/`.
- The **slinging / rigging gear and load de-rating** (slings, shackles, sling angle, dogging) →
  `../lifting-rigging-specialist/`.
- **Positioning the crane amongst site traffic / pedestrians** → `../mobile-plant-traffic-specialist/`.
- **Overhead-line approach distances / electrical isolation** detail → `../electrical-energy-specialist/`.
- Building the full **bow tie / lift risk study** → `../critical-risk-manager/` (this SME supplies the
  crane controls and questions that go into it).

## The risk

A **crane overturn, structural overload, dropped load, or contact with power lines** — from the wrong
crane, exceeding the rated capacity at the actual radius, soft or uneven ground under the outriggers,
loss of stability, wind, or an unplanned/uncoordinated lift.

## Critical controls — apply the hierarchy

Work top-down (detail in `references/good-practice.md`):

1. **Eliminate / reduce** — avoid or reduce the lift (prefabricate, mechanical handling, fewer/smaller
   lifts, lift in better conditions); never lift over people or live plant where avoidable.
2. **Engineering — right crane, right capacity, right set-up:**
   - **Select the crane** for the heaviest/farthest pick in the worst configuration, with margin.
   - **Stay within the rated capacity** at the *actual* radius and configuration — never exceed the
     load chart; account for over-side vs over-front and outriggers vs on-rubber.
   - **Found it properly** — outrigger pads/mats sized so ground bearing pressure stays within the
     ground's safe capacity; level; clear of excavations, slopes and voids; cribbing where needed.
3. **Plan the lift & classify it:**
   - Build the **gross load** (load + rigging + hook block + jib/aux deductions) and keep **utilisation**
     within limits; treat high-utilisation, tandem/dual, blind, over-structure or over-public lifts as
     **critical lifts** needing a documented lift study and a lift supervisor.
   - Define **wind limits**, exclusion zones, the signalling/communications plan and crew roles.
4. **Administrative** — competent crew, pre-lift brief, permits, "proceed without stopping once
   committed", stop-work authority for anyone.
5. **PPE & detection** — the crane's own RCI/LMI and anti-two-block, anemometer, hi-vis, comms.

## Crane crew & competency

Competency is part of the control set — confirm before the lift. The crane crew typically includes a
**crane operator**, a **dogger/rigger** (slinging and directing — see `../lifting-rigging-specialist/`)
and, for complex lifts, a **lift supervisor**. AU operation requires the relevant **HRWL crane class**;
NZ uses competency/certificates. Determine the exact requirement in `../high-risk-work-specialist/`.

## Jurisdiction note

**NZ:** WorkSafe's **Approved Code of Practice for Cranes** is the primary good-practice anchor —
note it predates HSWA 2015 (not yet updated to the current Act) and is being progressively reviewed;
it **remains published as good practice**. Confirm current status via `../hse-advisor/`. **AU:** crane
**design** is **AS 1418** and **safe use** is the **AS 2550** series (.1 general, .4 tower, .5 mobile &
vehicle-loading), supported by the **Code of Practice for Safe Use of Mobile Cranes** and
state/territory guidance (e.g. tower cranes). AS/NZS standards are **copyright — cited as
verify-pointers, not reproduced**; confirm the current edition.

## Output

Either a **crane/lift plan** (crane selection → rated capacity at radius → gross load & utilisation →
ground & outrigger set-up → stability/critical-lift classification → wind/exclusion/comms → crew &
competency → critical questions), or the **crane-specific controls and questions** to feed into a bow
tie (`../critical-risk-manager/`), task analysis (`../task-analysis-author/`) or SOP (`../sop-author/`).
A draft for a competent crane person / lift planner to validate against the actual crane chart and site.

## Hand-offs

- **Licence / competency to operate** → `../high-risk-work-specialist/`.
- **Slinging / rigging gear & sling de-rating** → `../lifting-rigging-specialist/`.
- **Crane siting amongst traffic/pedestrians** → `../mobile-plant-traffic-specialist/`.
- **Overhead power lines / electrical isolation** → `../electrical-energy-specialist/`.
- **Bow tie / critical-lift study** → `../critical-risk-manager/`.
- **Procedure / JSA** → `../sop-author/` / `../task-analysis-author/`.
- **Notifiable event / duties** (overturn, dropped load, dangerous occurrence) →
  `../worksafe-nz-specialist/` (NZ) / `../safework-au-specialist/` (AU). Route via `../hse-advisor/`.

## Disclaimer

This skill produces good-practice crane and lift-planning guidance — **not legal advice, not
engineering certification, and not a substitute for a competent crane person or the actual crane load
chart**, which governs. Rated capacities, ground bearing, stability and lift classification must be
confirmed by a competent person against the specific crane, configuration, ground and conditions before
any lift proceeds.
