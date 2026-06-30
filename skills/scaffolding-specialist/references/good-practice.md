# Scaffolding — good practice, structure & competency

Detailed good-practice controls, duty ratings, structural set-up, scaftag/inspection and competency for
scaffolding. Generic and company-agnostic, distilled from the NZ WorkSafe/SARNZ scaffolding good practice
and the Australian AS/NZS 1576 / 4576 framework. **Not legal advice**; standards and guidance change —
treat references as verify-pointers and confirm the current edition. **The scaffold design and the
scaftag govern.**

> This SME owns **the structure**. The **fall** hazard / access hierarchy → `../../working-at-height-specialist/`;
> the **scaffolder licence** → `../../high-risk-work-specialist/`; the **EWP alternative** →
> `../../ewp-specialist/`.

## Choose the scaffold type

| Type | Use | Watch |
|---|---|---|
| **Tube-and-coupler (tube & fitting)** | Flexible, irregular structures | Workmanship-dependent; coupler torque; competence-critical |
| **System / modular** | Fast, repeatable, common access | Use compatible components; don't mix systems |
| **Mobile scaffold tower** | Light, movable access | Outriggers/stabilisers; **never move occupied**; height-to-base ratio; firm/level floor |
| **Birdcage** | Full-area access under a ceiling | Ties/bracing; access; loaded-platform count |
| **Cantilever / hung / suspended** | No ground / over voids | **Engineered design**; special duty; anchorage |

## Duty (load) rating

Per **working platform per bay** — confirm on the **scaftag** / design:

| Duty | Allowable / bay | Concentrated | Typical work |
|---|---|---|---|
| **Light** | ~225 kg | ~120 kg | painting, inspection, electrical |
| **Medium** | ~450 kg | ~150 kg | general trades, light steel framing, tiling |
| **Heavy** | ~675 kg | ~200 kg | bricklaying, blockwork, demolition |
| **Special** | designed | designed | engineered to a specific load only |

Use `../scripts/scaffold_duty_check.py` to check the intended **per-bay load** (people + materials) and a
**concentrated load** against the rating (it treats person mass as a flagged assumption and never invents
the rating — **the scaftag/design governs**). Also limit the **number of bays/platforms loaded at once**
to what the design allows.

## Structure & stability — the core of scaffold safety

- **Foundations** — firm ground; **sole boards** to spread the load and **base plates** (adjustable
  jacks levelled); never found on soft fill, unconsolidated ground, fragile surfaces, or **within the
  zone of influence of an unsupported excavation**. Suspended slabs need the leg loads checked.
- **Frame** — **standards** plumb, **ledgers** level, **transoms** at the correct spacing; correct
  **bay length and lift height**; rated **couplers/fittings** tightened; no missing or substituted parts.
- **Ties & bracing** — **tie** the scaffold to the building/structure to the **design pattern/frequency**
  and **brace** (façade/ledger/plan bracing) for rigidity. **Never remove a tie** without re-design.
  **Sheeting / shrink-wrap / banners** dramatically increase **wind (sail) load** — they require **more
  ties** and a design check.
- **Complete the platform** — fully **planked/decked**, boards secured against **uplift**, no gaps for
  tools/feet; **edge protection** (guardrail ~900–1100 mm, mid-rail, **toe-board**) on open sides; safe
  **access** (internal ladder/stair access bay).
- **Don't overload** — keep within the **duty rating** and the loaded-platform count; land and distribute
  materials, don't pile them.

## Scaftag, handover & inspection

- **Scaftag at each access point** — **complete & safe to use** vs **incomplete — do not use** (and the
  **duty** marked). Only a **competent scaffolder** alters the scaffold or changes the tag. Users **must
  not** modify a scaffold (remove ties/boards/guardrails).
- **Handover** by the competent scaffolder after erection/alteration.
- **Inspect** before first use, then **at least every 30 days**, and **after any alteration, impact,
  modification or severe weather event**; record the inspection and who did it.

## Competency

- Erect/alter/dismantle by a **competent scaffolder**. **AU:** HRWL **SB (basic) / SI (intermediate) / SA
  (advanced)** by scaffold type/complexity. **NZ:** where a person could **fall 5 m or more**, the work
  must be done or **directly supervised by a Certificated Scaffolder** (WorkSafe / **SARNZ** Certificate
  of Competence, underpinned by the NZ Certificate in Scaffolding); under 5 m, a competent person to good
  practice. **NZ:** erecting/dismantling a scaffold from which a person could fall ≥ 5 m is **notifiable
  work** (24 h notice). See `../../high-risk-work-specialist/` and `../../working-at-height-specialist/`.

## Critical questions to consider

- Is the **scaffold type and duty rating** right for the work, height, ground and access?
- Are the **foundations** adequate (sole boards/base plates, firm ground, clear of excavations)?
- Are **ties and bracing** to the design — and have **sheeting/wind loads** been allowed for?
- Is the **platform complete** (fully decked, edge protection, safe access), with no gaps?
- Is the **loading within the duty rating** and the loaded-platform count (→ duty calculator)?
- Is there a **current scaftag** and **handover**, and has it been **inspected** (first use / 30-day /
  post-alteration)?
- Is the **scaffolder competent/certificated** for the height and type — and is the work **notifiable**?

## Authoritative sources

- **WorkSafe NZ — Scaffolding in New Zealand** and the **SARNZ** (Scaffolding, Access & Rigging NZ) Best
  Practice Guidelines: https://www.worksafe.govt.nz/topic-and-industry/working-at-height/scaffolding-in-new-zealand/
- **AS/NZS 1576** (scaffolding — general requirements/design) and **AS/NZS 4576** (guidelines for
  scaffolding, incl. scaffolder training/certification) — copyright; cite and apply, confirm the current
  edition.
- **Safe Work Australia — Scaffolds and scaffolding work** guidance; AU HRWL scaffolding classes via
  `../../high-risk-work-specialist/`.
