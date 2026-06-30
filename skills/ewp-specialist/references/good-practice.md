# EWP / MEWP — good practice, stability & competency

Detailed good-practice controls, stability set-up, crush/entrapment prevention and competency for mobile
elevating work platforms. Generic and company-agnostic, distilled from WorkSafe NZ MEWP good practice and
the Australian AS 1418.10 / AS 2550.10 framework. **Not legal advice**; standards and guidance change —
treat references as verify-pointers and confirm the current edition. **The data plate and manufacturer's
manual govern.**

> This SME owns **the machine**. The **fall** hazard from the platform → `../../working-at-height-specialist/`;
> the **operator licence** → `../../high-risk-work-specialist/`; **siting amongst traffic** →
> `../../mobile-plant-traffic-specialist/`; **overhead lines** → `../../electrical-energy-specialist/`.

## Choose the right EWP for the task

| Type | Strength | Watch |
|---|---|---|
| **Scissor lift** | Vertical reach, larger platform/capacity | Limited slope; firm level ground; tip-over if overloaded/extended on a grade |
| **Boom — telescopic / articulating (knuckle)** | Height **and** outreach; up-and-over | Capacity/stability fall with outreach; **ejection/catapult**; harness/restraint normally required |
| **Vertical / mast (personnel) lift** | Compact, indoor, low level | Low height; stability if moved extended |
| **Trailer / truck-mounted, spider/tracked** | Outrigger-stabilised reach | **Ground bearing** under pads is critical; set-up discipline |

## Platform load (data plate)

- The data plate gives a **rated platform capacity (kg)** and a **max number of persons** (and often a
  **max manual force**). The load — **occupants + tools + materials** — must stay within **both**.
- Use `../scripts/ewp_load_check.py` to sum the load and check it (it never reports above the data-plate
  rating; **person mass is an assumption you supply, not chart data**).
- **Manual force** (pulling/pushing from the platform) and **wind on sail area** (sheets, panels) add to
  the destabilising load — keep within the manufacturer's limits.

## Stability & set-up — the core of EWP safety

- **Firm, level ground.** Assess the surface; use **spreader pads** under outriggers; level the machine
  per the manual. Keep clear of **edges, voids, penetrations, service trenches, basements and soft fill**.
- **Ground bearing.** Outrigger/wheel point loads can be high; compare the **pad pressure** (the script
  estimates it from the per-leg load and pad area) with the **allowable ground bearing** for the surface
  (competent/geotechnical advice for suspended slabs, fill, or near excavations).
- **Slope / grade.** Operate only on slopes the machine is **rated** for; chassis level within limits.
- **Wind.** Obey the **manufacturer's wind-speed limit** — boom EWPs are wind-sensitive, and **sail area**
  (sheet materials, signage) effectively lowers the safe wind speed. Stop and lower in rising wind.
- **Dynamic loads / travelling elevated.** No sudden control inputs; travel elevated **only** where the
  machine permits and the path is firm, level and clear.

## Crush / entrapment — the signature MEWP killer

- An operator can be **pinned between the platform/controls and a fixed structure** (overhead steelwork,
  beams, eaves, doorways). **Sustained involuntary operation** of the controls (e.g. a slumped operator
  holding the joystick) can keep driving into the structure.
- Controls: **plan the route** to avoid overhead crush points and brief the operator on them; position the
  machine to keep the body clear of pinch points; **secondary guarding / anti-entrapment** devices
  (pressure-sensing bars, shrouds, cut-outs) **reduce** the risk but **must not be solely relied on** and
  must not introduce new hazards; consider proximity to structures in the work plan.

## Emergency lowering & rescue

- A **rescue plan is mandatory** before elevating: a **trained ground person**, the **emergency-lowering**
  controls **known and tested**, and a way to recover a **stranded or entrapped** operator **quickly**
  (not reliant on emergency-services response). Rehearse it.

## Inspection & maintenance

- **Pre-start each shift** — function and **emergency-lowering** tests, tyres/tracks, outriggers, fluids,
  controls, guards/rails, decals; a current **log book**.
- **Periodic and major inspection per AS 2550.10** — keep the records (AS 2550.10 §6.6). Maintenance and
  inspection by a **competent person** with access to **AS 2550.10** and **AS/NZS 1418.10**.

## Competency

- **Trained, competent and machine-familiarised** operators. **AU:** a **boom-type EWP with a boom length
  ≥ 11 m** needs **HRWL class WP**; below that and for scissor/vertical lifts, employer-verified
  competency. **NZ:** a recognised **EWP operator certificate** (NZ has **no HRWL**). Licensing/competency
  detail → `../../high-risk-work-specialist/`.

## Critical questions to consider

- Is the **EWP type** right for the height, outreach, ground and environment?
- Is the **platform load** within **both** the rated capacity **and** the max persons (data plate)?
- Is the **ground firm and level**, with ground-bearing assessed and outriggers/pads set?
- Are the **slope and wind** limits known and obeyed (incl. sail area)?
- Is **crush/entrapment** planned out (route, position, secondary guarding) — not just relied on guarding?
- Is there a **tested emergency-lowering / rescue plan** with a trained ground person?
- Is the operator **competent and the machine in-date** (pre-start, AS 2550.10 inspection)?
- Are **overhead lines** and **traffic** handled (→ electrical-energy / mobile-plant-traffic)?

## Authoritative sources

- **WorkSafe NZ — Mobile elevating work platforms** (and the Best Practice Guidelines — MEWPs):
  https://www.worksafe.govt.nz/topic-and-industry/working-at-height/mobile-elevating-work-platforms-2/
- **AS/NZS 1418.10** (design of MEWPs) and **AS 2550.10** (safe use of MEWPs) — copyright; cite and apply,
  confirm the current edition. Industry good practice (e.g. EWPA) on secondary guarding/entrapment.
