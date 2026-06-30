---
name: pressure-equipment-specialist
description: The subject-matter expert (SME) you consult for the pressure equipment itself — fired and
  unfired — boilers, pressure vessels, pressure piping, air receivers, autoclaves, steam and
  compressed-air systems, and gas cylinders as equipment. Use for the catastrophic-rupture / stored-
  energy hazard, pressure relief, the hazard-level classification, design verification/registration,
  in-service inspection, and operator competency. Triggers on "pressure equipment", "pressure vessel",
  "boiler", "air receiver", "compressed air receiver", "autoclave", "pressure piping", "steam system",
  "steam boiler", "gas cylinder", "LPG cylinder", "safety valve", "pressure relief", "relief valve",
  "PRV", "hazard level", "design verification", "pressure equipment inspection", "plant registration",
  "AS 4343", "AS/NZS 1200", "AS 3788", "PECPR", "boiler operator", "turbine operation". Includes a
  pV / hazard-level calculator. Grounded in NZ PECPR + AS 4343 / AS/NZS 1200 / 3788 and the AU plant-
  registration & HRWL boiler/turbine framework. Not legal advice.
---

# Pressure Equipment Specialist (boilers, vessels & pressure systems SME)

## Purpose

Be the **subject-matter expert you consult** for **pressure equipment itself** — **fired** (boilers) and
**unfired** (pressure vessels, pressure piping, air receivers, autoclaves, heat exchangers) pressure
equipment, **steam and compressed-air systems**, and **gas cylinders** as equipment. Sits in the
equipment tier beside crane/forklift/EWP/scaffolding: this SME owns **the equipment and its integrity**
— the **catastrophic-rupture / stored-energy** hazard, **pressure relief**, the **hazard-level
classification**, **design verification/registration**, **in-service inspection**, and **operator
competency**. The contents, general guarding, vessel entry and operator licence route to their SMEs.

## When to use

- Specifying, operating, maintaining or inspecting **pressure equipment** — boilers, **pressure
  vessels**, **air receivers**, autoclaves, pressure piping, steam systems, gas cylinders.
- The **catastrophic-rupture** hazard and **pressure-relief** protection (safety/relief valves).
- The **hazard-level classification** (AS 4343) and what **design verification / registration /
  inspection** it triggers (use `scripts/pressure_hazard_level.py`).
- **In-service inspection** cadence and **operator competency** (boiler/turbine).

## When NOT to use

- The **contents** of the equipment — flammable/toxic gas, LPG, dangerous-goods storage, SDS →
  `../hazardous-substances-specialist/`.
- **Entry into a vessel/boiler** as a confined space → `../confined-space-specialist/`.
- **General machine guarding / isolation & lockout-tagout** of plant → `../machinery-safety-specialist/`;
  generic **stored-energy / high-pressure-fluid release** as a hazard class → `../electrical-energy-specialist/`.
- **What licence the operator needs** (AU HRWL boiler **BB/BS/BA**, turbine **TO**, reciprocating steam
  engine **ES**; NZ certificates) → `../high-risk-work-specialist/`.
- The **process** the equipment serves (petroleum/geothermal/manufacturing process safety) →
  `../oil-gas-specialist/` / `../geothermal-specialist/` / `../manufacturing-specialist/`.
- Building the full **bow tie** → `../critical-risk-manager/`.

## The risk

- **Catastrophic rupture / explosion** — sudden release of **stored energy**: a **steam (boiler)
  explosion**, a **BLEVE** of liquefied gas, or a vessel/cylinder burst — producing **blast and
  shrapnel** that kill well beyond the equipment. The defining pressure-equipment hazard.
- **Loss of the protective barrier** — a **safety/relief valve** wrong-sized, wrongly set, **isolated,
  painted-up, gagged or removed**, so the equipment can over-pressure.
- **Loss of integrity** — corrosion, erosion, **creep** (hot boilers), fatigue/cyclic cracking, **low
  water** in a boiler (overheating → explosion), wrong material/repair, and over-pressure.
- Highest at **commissioning, abnormal operation, and maintenance/isolation**, and where equipment is
  **un-registered / un-inspected / out-of-date**.

## Hazard level, design verification & registration

The work that classifies pressure equipment is the **hazard level** (AS 4343, levels **A** highest to
**E** lowest), from the **pV product** (design pressure × volume) and a content factor:

- Use `scripts/pressure_hazard_level.py` to compute **pV** and the Fc-weighted figure (Fc = 0.1 vacuum,
  1 liquid, 10 gas). The hazard level then drives **design verification/registration** and **inspection**
  — **AS 4343 and a competent person govern** the actual level (it never assigns A–E itself).
- **NZ:** higher-hazard pressure equipment needs **design verification** under **PECPR** (the HSE
  (Pressure Equipment, Cranes, and Passenger Ropeways) Regulations 1999), by **accredited bodies** that
  keep their **own registers** (NZ has **no central plant register** → `../machinery-safety-specialist/`).
- **AU:** specified pressure equipment needs **design registration** *and* **item/plant registration**
  with the **state WHS regulator** (Victoria differs). Confirm the threshold for the hazard level.

## Core controls (owned here)

See `references/good-practice.md` for detail; **the design, the standards and a competent person govern.**

- **Pressure relief** — correctly **sized, set and sealed** safety/relief valves and devices; **never
  isolated, gagged or over-set**; tested/maintained on schedule. The primary barrier against rupture.
- **Integrity management** — design and material to **AS/NZS 1200**; corrosion/erosion/creep/fatigue
  management; **boiler water level and treatment**; over-pressure protection; competent **repairs**.
- **Hazard level & registration** — classify (AS 4343), obtain **design verification/registration**, and
  keep it current.
- **In-service inspection** — periodic external/internal inspection and pressure tests by a **competent
  person / inspection body** per **AS/NZS 3788**, at a cadence set by hazard level/service; keep the
  **certificate/records**.
- **Isolation & stored energy for maintenance** — **depressurise, isolate, drain/vent and prove zero
  energy** before any work; coordinate with **LOTO** (`../machinery-safety-specialist/`) and
  **confined-space** entry (`../confined-space-specialist/`).
- **Gas cylinders** — secure, upright, ventilated storage; valve protection; segregation (oxidiser/fuel);
  the **contents** route to `../hazardous-substances-specialist/`.

## Method

1. **Identify the equipment** (boiler / vessel / piping / air receiver / autoclave / cylinder) and its
   **service**.
2. **Classify the hazard level** (AS 4343) and check **design verification/registration** is current
   (`scripts/pressure_hazard_level.py`).
3. **Verify the protective barrier** — pressure relief sized/set/sealed and maintained.
4. **Check integrity & inspection** — corrosion/creep/fatigue/boiler water; current **in-service
   inspection** (AS/NZS 3788).
5. **Control maintenance** — depressurise/isolate/prove-zero-energy; route LOTO, confined space, contents.
6. **Confirm operator competency** (boiler/turbine licence) → `../high-risk-work-specialist/`.
7. **State residual obligations** — the design/standards/competent person govern; registration and
   inspection must be current.

## Jurisdiction note

**NZ:** **HSWA 2015** + the **HSE (Pressure Equipment, Cranes, and Passenger Ropeways) Regulations 1999
(PECPR)** — **design verification** and **in-service inspection** by accredited bodies; **AS 4343**
(hazard levels), **AS/NZS 1200** (pressure equipment), **AS/NZS 3788** (in-service inspection). NZ has
**no central plant register** (→ `../machinery-safety-specialist/`). **AU:** the **WHS Regulations** plant
provisions — **design registration** and **item/plant registration** of specified pressure equipment with
the **state WHS regulator** (Victoria's OHS Act differs), the same **AS 4343 / AS/NZS 1200 / 3788**
standards, plus **HRWL** for **boiler operation (BB/BS/BA)**, **turbine operation (TO)** and
**reciprocating steam engine (ES)** → `../high-risk-work-specialist/`. Standards are **copyright** — cite
and apply, confirm the current edition via `../hse-advisor/`.

## Output

Either a **pressure-equipment plan** (equipment → hazard level & registration → pressure relief →
integrity & inspection → maintenance isolation → operator competency → critical questions), or the
**pressure-equipment controls and questions** to feed into a bow tie (`../critical-risk-manager/`), task
analysis (`../task-analysis-author/`) or SOP (`../sop-author/`). A draft for a competent person to validate.

## Hand-offs

- **Contents / gas / DG storage** → `../hazardous-substances-specialist/`; **vessel/boiler entry** →
  `../confined-space-specialist/`; **guarding / LOTO / stored energy** → `../machinery-safety-specialist/`
  / `../electrical-energy-specialist/`.
- **Operator licence (boiler/turbine)** → `../high-risk-work-specialist/`; **the process served** →
  `../oil-gas-specialist/` / `../geothermal-specialist/` / `../manufacturing-specialist/`.
- **Duties / notifiable events** → `../worksafe-nz-specialist/` / `../safework-au-specialist/`; **bow tie /
  procedure / JSA** → `../critical-risk-manager/` / `../sop-author/` / `../task-analysis-author/`. Route
  via `../hse-advisor/`.

## Disclaimer

This skill produces good-practice pressure-equipment guidance and a planning calculator — **not legal
advice and not a substitute for the equipment design, the standards (AS 4343 / AS/NZS 1200 / 3788), the
jurisdiction's regulations (NZ PECPR / AU plant registration) or a competent person / inspection body**.
A pressure rupture or boiler explosion releases stored energy that kills well beyond the equipment;
validate the hazard level, pressure relief, integrity, inspection currency and isolation against the
actual equipment before relying on them.
