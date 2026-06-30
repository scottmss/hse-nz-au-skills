---
name: ewp-specialist
description: The subject-matter expert (SME) you consult for the elevating work platform itself —
  selecting the right EWP/MEWP type, reading the data plate (rated platform capacity and max persons),
  setting up on firm level ground within slope and wind limits, keeping it stable, and preventing the
  signature MEWP killer (crush/entrapment between the platform and a structure). Use for any mobile
  elevating work platform. Triggers on "EWP", "MEWP", "elevating work platform", "mobile elevating work
  platform", "boom lift", "cherry picker", "knuckle boom", "articulating boom", "telescopic boom",
  "scissor lift", "vertical lift", "travel tower", "spider lift", "trailer-mounted EWP", "truck-mounted
  EWP", "platform capacity", "outriggers", "secondary guarding", "entrapment", "WP class", "AS 2550.10",
  "AS 1418.10". Includes a platform-load / ground-bearing calculator. Grounded in the NZ WorkSafe MEWP
  good practice and the AU AS 1418.10 / AS 2550.10 framework. Not legal advice.
---

# EWP Specialist (elevating work platform SME)

## Purpose

Be the **subject-matter expert you consult** for the **EWP/MEWP itself** — selecting the right type,
reading the **data plate** (rated platform capacity and max persons), **setting up on firm, level ground**
within **slope and wind limits**, keeping it **stable**, and preventing the signature MEWP killer —
**crush/entrapment between the platform and a structure**. Sits beside the lifting cluster: this SME owns
**the machine**; the **fall** hazard from the platform is `../working-at-height-specialist/`, the
**operator licence/competency** is `../high-risk-work-specialist/`, and **siting amongst traffic** is
`../mobile-plant-traffic-specialist/`.

## When to use

- **Selecting and setting up** an EWP/MEWP for a task — type choice, ground, stability, reach/height.
- Reading and applying the **data plate** — **rated platform capacity** and **max persons**; planning
  the platform load (use `scripts/ewp_load_check.py`).
- **Stability** — ground bearing, slopes/grades, **wind limits**, outriggers/levelling, kerbs/voids.
- **Crush/entrapment** prevention and **emergency lowering / rescue** of a stranded platform.

## When NOT to use

- The **fall hazard from the platform** (harness/restraint in boom EWPs, edge/anchor selection, the
  hierarchy of access) → `../working-at-height-specialist/`.
- **What licence/competency** the operator needs (AU HRWL **WP** for boom ≥ 11 m; NZ EWP operator
  certificate) → `../high-risk-work-specialist/`.
- **Siting amongst site traffic / ground crew / pedestrians** → `../mobile-plant-traffic-specialist/`.
- **Overhead-line approach distances / electrocution** detail → `../electrical-energy-specialist/`.
- Building the full **bow tie** → `../critical-risk-manager/`.

## The risk

- **Overturn / instability** — soft or sloping ground, voids/penetrations, **wind**, overloading,
  dynamic loads (sudden movements), travelling elevated.
- **Crush / entrapment** — the operator pinned **between the platform/controls and a fixed structure**
  (overhead steelwork, beams, eaves) — a leading MEWP fatality. **Sustained involuntary operation** of
  the controls can keep driving the platform into the structure.
- **Falls from the platform**, **ejection** (catapult from a boom), **contact with overhead lines**, and
  **mechanical failure**. Highest during set-up, travelling elevated, and working in confined overhead
  spaces.

## EWP types (choose for the task)

- **Scissor lift** — vertical only; good platform area/capacity; firm level ground (limited slope).
- **Boom — telescopic / articulating (knuckle)** — height *and* outreach; up-and-over access; capacity
  and stability fall as outreach increases; harness/restraint normally required.
- **Vertical / mast (personnel) lift** — compact, low height, indoor.
- **Trailer / truck-mounted, spider/tracked** — outrigger-stabilised; ground bearing under pads is
  critical.

## Stability & set-up — the core controls

See `references/good-practice.md` for detail; **the data plate and manufacturer's manual govern.**

- **Platform load** — keep occupants + tools + materials within the **rated platform capacity** *and* the
  **max persons**; check with `scripts/ewp_load_check.py` (it never exceeds the data-plate rating).
- **Ground** — **firm and level**; assess **ground-bearing** (pads/wheels vs allowable bearing —
  the script estimates pad pressure); spreader pads under outriggers; keep clear of **edges, voids,
  penetrations, trenches and basements**.
- **Slope/grade** — only on slopes the machine is **rated** for; level with outriggers where fitted.
- **Wind** — obey the **manufacturer's wind-speed limit** (boom EWPs especially; account for sail area of
  sheets/panels).
- **Dynamic / travel** — travel elevated only where the machine allows and the route is firm/level/clear;
  no sudden inputs.

## Crush/entrapment & rescue

- **Plan the route** to avoid overhead crush points; brief the operator on where they could be **pinned**.
- **Secondary guarding / anti-entrapment** devices reduce the risk but **must not be solely relied on**
  and must not introduce new hazards.
- A **rescue plan** is mandatory: trained ground person, **emergency-lowering** controls known and
  tested, and a way to recover a stranded or entrapped operator quickly.

## Inspection & competency

- **Pre-start** each shift (function/emergency-lowering tests, tyres/outriggers, fluids, controls,
  guarding); a current **log book**; periodic and **major inspection** per **AS 2550.10** (records kept).
- **Trained, competent, familiarised** operators for the specific machine; **AU:** boom EWP ≥ 11 m boom
  = **HRWL class WP**; **NZ:** recognised **EWP operator certificate** (no HRWL) →
  `../high-risk-work-specialist/`.

## Method

1. **Select the EWP type** for the height, outreach, ground and environment.
2. **Read the data plate** — rated platform capacity and max persons — and **check the platform load**
   (`scripts/ewp_load_check.py`).
3. **Set up for stability** — firm/level ground, ground-bearing, slope and **wind** limits, outriggers.
4. **Control crush/entrapment** — route planning, secondary guarding, and a **rescue/emergency-lowering**
   plan.
5. **Route the adjacent risks** — fall protection (working-at-height), licence (high-risk-work), traffic
   (mobile-plant), overhead lines (electrical).
6. **State residual obligations** — pre-start, competent operator, and the data plate/manual govern.

## Output

Either an **EWP set-up / selection plan** (type → data-plate load check → ground & stability → wind/slope
→ crush-entrapment & rescue → competency → critical questions), or the **EWP-specific controls and
questions** to feed into a bow tie (`../critical-risk-manager/`), task analysis
(`../task-analysis-author/`) or SOP (`../sop-author/`). A draft for a competent person to validate.

## Hand-offs

- **Fall protection from the platform** → `../working-at-height-specialist/`; **operator licence /
  competency** → `../high-risk-work-specialist/`.
- **Siting amongst traffic / ground crew** → `../mobile-plant-traffic-specialist/`; **overhead lines /
  electrocution** → `../electrical-energy-specialist/`.
- **Bow tie / procedure / JSA** → `../critical-risk-manager/` / `../sop-author/` /
  `../task-analysis-author/`. Route via `../hse-advisor/`.

## Disclaimer

This skill produces good-practice EWP guidance and a planning calculator — **not legal advice and not a
substitute for the EWP data plate, the manufacturer's manual, the current standards (AS 1418.10 / AS
2550.10) or a competent person**. Overturn and crush/entrapment kill quickly; validate the platform
load, ground/stability, wind/slope limits and the rescue plan against the actual machine, site and people
before use.
