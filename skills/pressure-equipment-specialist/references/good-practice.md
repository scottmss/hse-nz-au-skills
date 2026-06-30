# Pressure equipment — good practice, integrity & competency

Detailed good-practice controls, the hazard-level/registration regime, integrity management, inspection
and competency for fired and unfired pressure equipment. Generic and company-agnostic, distilled from the
NZ PECPR framework + AS 4343 / AS/NZS 1200 / AS/NZS 3788 and the Australian plant-registration & HRWL
framework. **Not legal advice**; standards and regulations change — treat references as verify-pointers
and confirm the current edition. **The equipment design, the standards and a competent person / inspection
body govern.**

> This SME owns **the equipment and its integrity**. The **contents** → `../../hazardous-substances-specialist/`;
> **vessel entry** → `../../confined-space-specialist/`; **guarding/LOTO** → `../../machinery-safety-specialist/`;
> the **operator licence** → `../../high-risk-work-specialist/`.

## What counts as pressure equipment

- **Fired:** **boilers** (steam/hot-water), fired heaters.
- **Unfired:** **pressure vessels**, **air receivers**, **autoclaves**, heat exchangers, **pressure
  piping**, and **gas cylinders** (as equipment). Steam and **compressed-air** systems tie them together.

## The catastrophic hazard

A pressure rupture releases **stored energy** as **blast and shrapnel** that travel well beyond the
equipment — a **steam (boiler) explosion**, a **BLEVE** of liquefied gas, or a vessel/cylinder burst.
Two failure routes dominate: **the protective barrier (relief) fails** so the equipment over-pressures,
or **integrity fails** (corrosion/creep/fatigue/low water/bad repair). Control **both**.

## Hazard level, design verification & registration

The classifying step is the **hazard level (AS 4343, A highest → E lowest)**, from the **pV product**
(design pressure × volume) and a content factor (Fc = 0.1 vacuum, 1 liquid, **10 gas**), with harmfulness
and special factors. Use `../scripts/pressure_hazard_level.py` to compute pV and the Fc-weighted figure —
**it never assigns the A–E level; AS 4343 and a competent person govern.** A worked example: a ~1250 L
**gas** air-receiver at 800 kPa gives pV ≈ 1000 MPa·L → about **Hazard Level B**, which triggers design +
plant registration in AU.

- **NZ — PECPR.** Higher-hazard pressure equipment needs **design verification** under the **HSE (Pressure
  Equipment, Cranes, and Passenger Ropeways) Regulations 1999**, performed by **accredited bodies** that
  keep **their own registers** — NZ has **no central plant register** (see `../../machinery-safety-specialist/`).
- **AU — plant registration.** Specified pressure equipment needs both **design registration** and
  **item/plant registration** with the **state/territory WHS regulator** (Victoria's OHS Act differs).
  The hazard level sets whether registration applies — confirm the threshold.

## Pressure relief — the primary barrier

- **Safety/relief valves and devices** correctly **sized** for the worst-case over-pressure source, **set**
  to the right pressure, and **sealed** — and **never isolated, gagged, painted-over, over-adjusted or
  removed**. A vessel can be **multiply protected** (e.g. a fire case).
- **Test and maintain** relief devices on schedule; keep records; re-verify after any change of duty.

## Integrity management

- **Design and construction** to **AS/NZS 1200** (and the relevant vessel/boiler/piping standards);
  correct **materials** and **welding/repair** by competent persons (no unapproved repairs).
- **Degradation** — manage **corrosion and erosion** (corrosion allowance, coatings, monitoring),
  **creep** in hot boiler/HT components, and **fatigue/cyclic** cracking; protect against **over-pressure**
  and **thermal shock**.
- **Boilers** — **water level** and quality are life-critical: **low water → overheating → explosion**;
  maintain level controls, low-water trips, feedwater and water treatment, and competent attendance.

## In-service inspection

- Periodic **external and internal inspection** and **pressure tests** by a **competent person /
  inspection body** to **AS/NZS 3788**, at a **cadence set by the hazard level and service** (corrosive,
  cyclic, hot service shorten it). Keep the **certificate and records**; act on findings before return to
  service.

## Isolation & stored energy for maintenance

Before any work on or entry into pressure equipment: **depressurise, isolate (positive isolation/blanks),
drain/vent, and prove zero energy** — then coordinate **lockout/tagout** (`../../machinery-safety-specialist/`)
and, for internal work, **confined-space entry** (`../../confined-space-specialist/`). Beware **trapped
pressure**, residual heat and stored process energy.

## Gas cylinders (as equipment)

Store **secured and upright**, ventilated, away from heat/ignition; **valve protection** fitted;
**segregate** oxidisers from fuels; inspect and keep within **test date**. The **contents** (flammable/
toxic/inert, DG class) route to `../../hazardous-substances-specialist/`.

## Competency

- **Operators** competent for the equipment. **AU:** **HRWL** — **boiler operation (BB basic / BS standard
  / BA advanced)**, **turbine operation (TO)**, **reciprocating steam engine (ES)**. **NZ:** boiler/
  pressure-equipment **certificates of competence** and PECPR roles. **Inspection** by a competent
  person / accredited inspection body. Licensing detail → `../../high-risk-work-specialist/`.

## Critical questions to consider

- What's the **hazard level** (AS 4343, pV × Fc), and is **design verification/registration** current
  (NZ PECPR / AU registration)?
- Is the **pressure relief** sized/set/sealed, maintained, and **not isolated or gagged**?
- Is **integrity** managed (corrosion/creep/fatigue; **boiler water level/treatment**; over-pressure)?
- Is **in-service inspection** current (AS/NZS 3788), with records and findings actioned?
- For maintenance/entry: **depressurised, isolated, zero-energy proven**, with LOTO and confined-space
  routed?
- Are **operators competent/licensed** (boiler/turbine), and **gas cylinders** stored and in-test?

## Authoritative sources

- **NZ — PECPR** (HSE (Pressure Equipment, Cranes, and Passenger Ropeways) Regulations 1999) and **WorkSafe
  NZ** pressure-equipment guidance: https://www.worksafe.govt.nz/
- **AU — state/territory WHS regulators** for pressure-equipment **design & item registration** and HRWL
  boiler/turbine operation.
- **Standards (copyright — cite and apply):** **AS 4343** (hazard levels), **AS/NZS 1200** (pressure
  equipment), **AS/NZS 3788** (in-service inspection), and the relevant boiler/vessel/piping standards.
  Confirm current editions before relying on any requirement.
