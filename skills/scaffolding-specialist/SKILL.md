---
name: scaffolding-specialist
description: The subject-matter expert (SME) you consult for the scaffold structure itself — choosing the
  scaffold type, its duty (load) rating, foundations and sole boards, standards/ledgers/transoms, ties
  and bracing for stability, complete platforms with edge protection, and safe erect/alter/dismantle with
  scaftag handover and inspection. Use for any scaffold. Triggers on "scaffold", "scaffolding",
  "scaffolder", "tube and coupler", "tube and fitting", "system scaffold", "modular scaffold", "mobile
  scaffold tower", "birdcage", "cantilever scaffold", "hung/suspended scaffold", "duty rating", "light
  duty", "medium duty", "heavy duty", "sole board", "base plate", "standard ledger transom", "ties",
  "bracing", "scaftag", "scaffold tag", "scaffold inspection", "SB/SI/SA", "certificated scaffolder",
  "AS/NZS 1576", "AS/NZS 4576". Includes a duty-load calculator. Grounded in the NZ WorkSafe/SARNZ
  scaffolding good practice and the AU AS/NZS 1576 / 4576 framework. Not legal advice.
---

# Scaffolding Specialist (scaffold structure SME)

## Purpose

Be the **subject-matter expert you consult** for the **scaffold structure itself** — selecting the
**type**, applying its **duty (load) rating**, founding it on adequate **sole boards/base plates**,
building it with **standards/ledgers/transoms**, **tying and bracing** it for stability, completing the
**platform and edge protection**, and controlling **erect/alter/dismantle** with a **scaftag handover**
and **inspection** regime. Sits in the equipment tier beside crane/forklift/lifting-rigging/EWP: this SME
owns **the structure**; the **fall** hazard is `../working-at-height-specialist/`, the **scaffolder
licence/competency** is `../high-risk-work-specialist/`.

## When to use

- **Selecting and specifying** a scaffold — type, **duty rating** for the work, height, ties, access.
- The **structure's integrity** — foundations, standards/ledgers/transoms, **ties and bracing**,
  platform completeness and **edge protection**.
- **Loading a scaffold** to its duty (use `scripts/scaffold_duty_check.py`).
- **Erect / alter / dismantle** sequence, **incomplete-scaffold control (scaftag)**, handover and
  **inspection**.

## When NOT to use

- The **fall hazard / fall protection** while *erecting* or *working from* the scaffold, and the access
  hierarchy (is a scaffold even the right control?) → `../working-at-height-specialist/`.
- **What licence/competency** the scaffolder needs (AU HRWL **SB/SI/SA**; NZ **certificated scaffolder**)
  → `../high-risk-work-specialist/`.
- **Mobile-scaffold-tower movement amongst traffic / on slabs** as a traffic matter →
  `../mobile-plant-traffic-specialist/`; **the EWP alternative** → `../ewp-specialist/`.
- **Loading materials onto the scaffold by crane** → `../crane-specialist/` + `../lifting-rigging-specialist/`.
- Building the full **bow tie** → `../critical-risk-manager/`.

## The risk

- **Collapse / instability** — inadequate **foundations** (soft ground, no sole boards), missing **ties
  or bracing**, **overloading** beyond the duty rating, unauthorised **alteration**, struck by plant, or
  removed components.
- **Falls** — from incomplete platforms, missing **edge protection** (guardrails/mid-rails/toe-boards),
  gaps, or **using an incomplete scaffold** (no/!green tag).
- **Falling objects** onto people below; **electrical contact** with overhead lines during erection/
  movement. Highest during **erect/alter/dismantle** and when a scaffold is **modified or part-built**.

## Scaffold types & duty (choose for the task)

- **Types** — tube-and-coupler (tube & fitting), **system/modular**, **mobile scaffold tower**,
  birdcage, cantilever, hung/suspended, and proprietary access. Pick for the loads, geometry and ground.
- **Duty (load) rating** — per working platform per bay (confirm on the **scaftag** / design):
  - **Light** ~225 kg/bay (concentrated 120 kg) — painting, inspection, electrical.
  - **Medium** ~450 kg/bay (concentrated 150 kg) — general trades, light steel, tiling.
  - **Heavy** ~675 kg/bay (concentrated 200 kg) — bricklaying, blockwork, demolition.
  - **Special** — a specific **designed** load (engineered). Use `scripts/scaffold_duty_check.py` to
    check the intended load against the rating (**the scaftag/design governs**).

## Structure & stability — the core controls

See `references/good-practice.md` for detail; **the scaffold design and scaftag govern.**

- **Foundations** — firm ground, **sole boards and base plates**, levelled; never found on soft fill,
  near unsupported excavations, or on a surface that can't take the leg loads.
- **Standards/ledgers/transoms** plumb, level and to the correct **bay/lift** spacing; couplers/fittings
  rated and tight.
- **Ties and bracing** — **tie** to the structure and **brace** to the design frequency/pattern; never
  remove ties without re-design. (Sheeting/shrink-wrap adds **wind sail** load — needs more ties.)
- **Complete the platform** — fully **planked/decked**, secured against uplift, with **edge protection**
  (guardrail, mid-rail, toe-board) and safe **access** (internal ladders/stair).
- **Don't overload** — stay within the **duty rating** per bay and the **number of loaded platforms** the
  design allows.

## Scaftag, handover & inspection

- **Scaftag / scaffold tag** at every access point: **complete & safe to use** vs **incomplete — do not
  use**; only a **competent scaffolder** changes the tag.
- **Handover** by a competent scaffolder; users do not alter the scaffold.
- **Inspect** before first use, then **at least every 30 days**, and **after any alteration, impact or
  severe weather**; record it.

## Competency

- Erect/alter/dismantle by a **competent scaffolder**. **AU:** HRWL **SB (basic) / SI (intermediate) / SA
  (advanced)**. **NZ:** where a person could **fall ≥ 5 m**, a **Certificated Scaffolder** (WorkSafe/
  **SARNZ** Certificate of Competence) must do or directly supervise the work; under 5 m, a competent
  person to good practice. Licensing detail → `../high-risk-work-specialist/`.

## Method

1. **Select the scaffold type and duty rating** for the work, height, ground and access.
2. **Specify the structure** — foundations/sole boards, standards/ledgers/transoms, **ties & bracing**,
   complete platform + edge protection + access.
3. **Check the loading** against the duty rating (`scripts/scaffold_duty_check.py`).
4. **Control erect/alter/dismantle** — sequence, fall protection *during* the work
   (→ working-at-height), **scaftag**, **handover** and **inspection**.
5. **Route the adjacent risks** — fall protection (working-at-height), scaffolder licence
   (high-risk-work), tower movement/traffic (mobile-plant), overhead lines (electrical).
6. **State residual obligations** — competent scaffolder, current tag/inspection, and no unauthorised
   alteration; the design/scaftag govern.

## Output

Either a **scaffold specification / loading plan** (type → duty rating → foundations/ties/bracing →
complete platform → duty-load check → scaftag/inspection → competency → critical questions), or the
**scaffold-specific controls and questions** to feed into a bow tie (`../critical-risk-manager/`), task
analysis (`../task-analysis-author/`) or SOP (`../sop-author/`). A draft for a competent person to
validate.

## Hand-offs

- **Fall protection / access hierarchy** → `../working-at-height-specialist/`; **scaffolder licence /
  competency** → `../high-risk-work-specialist/`.
- **EWP alternative** → `../ewp-specialist/`; **mobile-tower movement / traffic** →
  `../mobile-plant-traffic-specialist/`; **crane-loading materials onto the scaffold** →
  `../crane-specialist/` + `../lifting-rigging-specialist/`; **overhead lines** →
  `../electrical-energy-specialist/`.
- **Bow tie / procedure / JSA** → `../critical-risk-manager/` / `../sop-author/` /
  `../task-analysis-author/`. Route via `../hse-advisor/`.

## Disclaimer

This skill produces good-practice scaffolding guidance and a planning calculator — **not legal advice and
not a substitute for the scaffold design, the scaftag, the current standards (AS/NZS 1576 / 4576) or a
competent/certificated scaffolder**. Scaffold collapse and falls kill; validate the duty rating,
foundations, ties/bracing, platform completeness and the inspection/handover against the actual scaffold
and site before anyone uses it.
