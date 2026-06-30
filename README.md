# HSE NZ/AU Skills

**Claude Agent Skills for New Zealand & Australian workplace health & safety.**

An open-source collection of [Claude Agent Skills](https://docs.anthropic.com/en/docs/claude-code/skills)
that teach Claude to perform specialist occupational health & safety (HSE) tasks the way an
experienced NZ/AU H&S practitioner would — building bow tie risk assessments, running incident
investigations, scoring critical-risk control assurance, and reasoning about duty-holder
obligations under **HSWA 2015 (NZ)** and the **WHS model law (AU)**.

The public Claude skills ecosystem is almost entirely software engineering, security, and
international GRC compliance. This collection fills a genuine gap: capable, jurisdiction-correct
**occupational** H&S skills grounded in NZ and Australian law and AS/NZS standards.

---

## ⚠️ Disclaimer — read this first

These skills produce **drafting, structure, and analysis — not legal advice.**

- They are **not** a substitute for a qualified HSE practitioner or a lawyer.
- Every output must be **reviewed and validated by a competent person** against the actual
  site, plant, people, and the *current text of the law and standards*, which change over time.
- They are **generic and company-agnostic**. They contain no organisation-specific process,
  template, or proprietary content.

Use them to work faster and more consistently — not to replace professional judgement.

---

## Skills in this collection

| Skill | What it does |
|-------|--------------|
| **hse-advisor** | Orchestrator. Identifies the jurisdiction (NZ vs AU) and task, then routes to the right specialist. |
| **critical-risk-manager** | Builds and reviews bow tie risk assessments, defines critical risks, and scores control assurance and residual risk. |
| **officer-governance-advisor** | Officer/board H&S governance and due diligence (HSWA s 44): governance self-assessment, board reporting, officer induction, director questions, and the link to enterprise risk. Grounded in the IoD/WorkSafe NZ governance guide. |
| **worksafe-nz-specialist** | NZ HSWA 2015 duties: who holds which duty, the primary duty of care, reasonably practicable, the four steps to managing risk, **notifiable events** (what to notify, preserve, record), and in-depth **overlapping duties** — shared workplaces, contracting chains, and the "3 Cs". |
| **safework-au-specialist** | Australian WHS law: establishes **which jurisdiction and regulator** apply (model WHS states + Commonwealth, and **Victoria's separate OHS Act 2004**), then the PCBU primary duty, officer due diligence, overlapping duties (s 46), notifiable incidents, Codes of Practice, and high-risk work licensing. |
| **incident-investigator** | Structured **Five Whys** root cause analysis for a workplace incident or near-miss — problem statement, validated why-chain, root causes, and corrective actions with owners and verification. |
| **complex-problem-analyst** | **Fishbone (Ishikawa)** analysis for recurring, multi-causal problems — maps all contributing factor categories (6M) at once, finds the intersections, and pairs with Five Whys for depth. |
| **high-risk-work-specialist** | What licence or competency a high-risk task needs and who may do it — **AU HRWL classes** (cranes, dogging, rigging, scaffolding, EWP, forklift) vs **NZ competency** (NZQA unit standards, Certificates of Competence, Approved Codes), plus the governing AS/NZS standards. |
| **lifting-rigging-specialist** | The SME for the **rigging/dogging method** — estimating the load and its centre of gravity, selecting and **de-rating slings for the sling angle**, choosing lifting gear (shackles, eyebolts, beams), and running the lift (exclusion zone, signals, tag lines). Includes a sling-WLL calculator. Grounded in the NZ ACOP for Load-lifting Rigging + AS standards. |
| **crane-specialist** | The SME for the **crane and the lift** — crane selection, reading and de-rating the **load chart / rated capacity**, gross-load build-up and **utilisation / critical-lift classification**, ground & outrigger set-up, stability, lift planning, and wind/inspection limits. Includes a crane-utilisation calculator. Grounded in the NZ ACOP for Cranes + AS 1418/AS 2550. |
| **forklift-specialist** | The SME for the **forklift itself** — rated capacity and **load-centre / lift-height de-rating**, the stability triangle & tip-over, attachments, grades & loading docks, pedestrian separation, pre-start, ROPS/seatbelt, and refuelling/charging. Includes a load-centre capacity calculator. Grounded in the NZ forklift ACOP + AS 2359. |
| **sop-author** | Writes or reviews a **Standard Operating Procedure** / safe system of work — purpose & scope, roles, the step-by-step method with hazards and controls integrated, competency sign-off, and document control. |
| **task-analysis-author** | Builds a **Task Analysis (TA) / JSA** for a specific job — steps → hazards → initial risk → controls (hierarchy) → responsible → residual risk, with a worker sign-on. Reuses the critical-risk matrix and scorer. |
| **prosecution-analyst** | Turns **NZ/AU H&S prosecution patterns** into preventive lessons and benchmarks — the enforcement/sentencing frameworks (HSWA ss 47–49 + Stumpmaster; model WHS Category 1–3 + industrial manslaughter) and the recurring duty-failure patterns. Company-agnostic and educational; not a prediction of any case. |
| **psychosocial-risk-specialist** | Identify, assess and control **psychosocial risk** (work-design hazards that cause psychological harm) — the hazard taxonomy, source-first controls, and the NZ/AU split (AU model WHS Regs 55A–55D + Code; NZ via the general duties, since "health" includes mental health). |
| **working-at-height-specialist** | The SME for **working at height / preventing falls** — good-practice controls (eliminate → passive → restraint/arrest), dropped objects, rescue, and the qualifications + NZ/AU guidance (WorkSafe GPG; AU falls Code; AS/NZS 1891). |
| **excavation-specialist** | The SME for **excavation, trenching & ground disturbance** — locating/isolating underground services, collapse prevention (batter/bench/shore), exclusion zones, rescue, and the qualifications + NZ/AU guidance (WorkSafe GPG; AU Excavation Code; AS 5488). |
| **confined-space-specialist** | The SME for **confined space entry** — atmosphere (isolate, purge, test, ventilate), entry permit, standby, non-entry rescue, and the qualifications + NZ/AU guidance (WorkSafe; AU Confined spaces Code; AS/NZS 2865). |
| **machinery-safety-specialist** | The SME for **machinery & plant safety** — guarding (fixed/interlocked), emergency stops, and **isolation/lockout-tagout (LOTO)**, plus qualifications + NZ/AU guidance (WorkSafe Safe use of machinery; AU plant Code; AS/NZS 4024). |
| **mobile-plant-traffic-specialist** | The SME for **vehicles, mobile plant & workplace traffic** — separating pedestrians and vehicles, reversing/blind-spot controls, traffic management plans, plus competency (WorkSafe site-traffic GPG; NZGTTM; AU traffic guide). |
| **hazardous-substances-specialist** | The SME for **hazardous substances/chemicals & asbestos** — inventory/SDS/GHS, eliminate/substitute/ventilate/contain, plus the NZ/AU regs (HSW Hazardous Substances 2017 & Asbestos 2016; AU chemicals & asbestos Codes). |
| **electrical-energy-specialist** | The SME for **electrical safety & stored/released energy** — de-energise/isolate/prove-dead, arc flash, overhead-line approach distances (NZECP 34), hot work and pressure release, plus competency (WorkSafe Energy Safety; AU electrical Code; AS/NZS 4836). |
| **electricity-supply-specialist** | The SME for the **electricity supply industry (ESI) sector** — the generation, transmission & distribution workforce whose core business *is* the network. Owns the **work-control / permit / access-authority system (SM-EI)**, switching & earthing, **live-line** work, substations & cable jointing, and generation (**hydro & dam safety**, **geothermal & H₂S**, wind, solar/BESS); routes the electrical hazard to electrical-energy-specialist and the rest to their SMEs. Grounded in the NZ ESI stack (SM-EI, NZECP 34/35, Electricity (Safety) Regs 2010) + StayLive. |
| **water-safety-specialist** | The SME for **working in/on/above water** — prevent the fall in, lifejackets, safety observer, water rescue, conditions monitoring, and diving (AS 4758; AS/NZS 2299; Maritime NZ). |
| **horticulture-specialist** | The SME for **horticulture** — orchards, vineyards, kiwifruit, packhouses & coolstores. Owns orchard **MEWPs near overhead lines**, spray-drift, packhouse machinery, **controlled-atmosphere coolstores as confined spaces**, and the **seasonal/RSE workforce**; routes specific hazards to the relevant SME. Grounded in WorkSafe NZ horticulture/MEWP/overhead-line guidance + AU state guidance. |
| **construction-specialist** | The SME for the **construction project regime & construction-specific activities** — principal contractor / **SWMS / high-risk construction work**, site induction & coordination, **temporary works** (formwork/falsework/propping), demolition, and **precast/tilt-up concrete erection** (AS 3850 bracing, lifting inserts, the signed brace plan); routes the physical hazards to the relevant SME. Grounded in NZ HSWA/WorkSafe + AU WHS construction regime + AS 3850. |
| **stevedoring-specialist** | The SME for **stevedoring & port cargo-handling** — loading/unloading ships, container terminals and the wharf (a sector with a serious-injury rate many times the average). Owns the **plant–pedestrian interface** (straddle carriers, reach stackers, quay cranes), lashing-at-height, and the ship interface (holds as confined spaces, over-water); routes the lift, falls and traffic to their SMEs. Grounded in the AU *Managing risks in stevedoring* Code + NZ WorkSafe port-sector / Maritime NZ. |
| **manufacturing-specialist** | The SME for **manufacturing & processing** — the factory production system and its catastrophic risks (**process safety / major hazard facilities**, **combustible dust & explosion**) and chronic risks (**occupational noise**, **hazardous manual tasks**); routes machine guarding/LOTO and chemicals to their SMEs. Grounded in NZ HSW (Major Hazard Facilities) Regs 2016 + AU WHS MHF / noise / manual-task Codes. |
| **transport-logistics-specialist** | The SME for **road transport, trucking & logistics** — the heavy-vehicle supply-chain regime (**Chain of Responsibility / HVNL** in AU; HSWA upstream duties + NZTA work-time in NZ), **driver fatigue & work-time**, **loading/unloading**, and **load restraint**; routes the physical hazards to the relevant SME. Grounded in the AU HVNL/CoR regime + NZ HSWA / Land Transport rules. |
| **forestry-specialist** | The SME for **forestry & harvesting** — owns the deadly core tasks (**tree felling**, **breaking out / cable logging**, the cutover and landing), foregrounds **mechanisation / winch-assist to get people off the slope**, and covers competency and remote rescue; routes generic hazards to the relevant SME. Grounded in WorkSafe NZ's 2025 forestry ACOP + Safetree + AU Safe Work Australia / state harvesting Codes. |
| **agriculture-specialist** | The SME for **farm & agriculture safety** — the sector's fatal risks with **farm vehicles & quad bikes** as the flagship (CPD/OPD rollover protection, helmets, no-passengers, side-by-side choice), plus livestock, working alone, and child/visitor safety; routes specific hazards to the relevant SME. Grounded in WorkSafe NZ Safer Farms + the AU ACCC quad standard. |
| **violence-aggression-specialist** | The SME for **work-related violence & aggression** — design out the opportunity, lone/in-home worker controls, de-escalation, duress/security, and post-incident support (WorkSafe Violence at work; AU violence guidance). Partners psychosocial-risk-specialist. |
| **mining-quarrying-specialist** | The SME for **mining, quarrying & extractives** (surface & underground) — the sector's **separate safety regime** (NZ HSW Mining/Quarrying Regs 2016; AU **state-by-state** — Qld RSHQ Acts, NSW Mines & Petroleum Sites, WA WHS (Mines) Regs), statutory roles & **certificates of competence**, and the **principal hazards** (ground/strata failure, inrush, gas/ventilation, blasting, haul trucks, dust/black lung, tailings, mines rescue); routes generic hazards to their SMEs. |
| **fishing-aquaculture-specialist** | The SME for **commercial fishing & aquaculture** (one of the highest-fatality sectors) — the **co-regulated** maritime + WHS regime (NZ **Maritime NZ** as one regulator for vessel *and* people via MOSS; AU **AMSA** for the vessel + **state WHS** for the people), and the on-water fatal risks (**man overboard/PFDs**, vessel stability/capsize, deck-machinery entanglement, crossing the bar, emergency preparedness, fatigue) plus marine-farm diving & workboats; routes generic hazards to their SMEs. |
| **maritime-ports-specialist** | The SME for **non-fishing seafaring & port/harbour marine operations** — cargo ships, ferries, passenger vessels, tugs, workboats, and the marine side of ports (**mooring/line-handling & snap-back**, pilotage, towage, bunkering, the ship-shore interface, enclosed spaces on ships). Owns the regime (NZ **Maritime NZ**, incl. the 13 major ports on land from 1 Jul 2024; AU **AMSA + Seacare + state WHS**; SOLAS/ISM/STCW); routes cargo handling → stevedoring, fishing → fishing-aquaculture, and generic hazards to their SMEs. |

| **healthcare-specialist** | The SME for **worker** health & safety in **healthcare, aged & disability care** (the largest-employing, convergence sector — *not* patient/clinical safety) — hospitals, rest homes/aged residential care, disability & home/community care, ambulance, mental health. Owns **person/patient handling** (no-lift, hoists, slide sheets) and the sector view; routes occupational violence (dementia), psychosocial/shift work, sharps/biological exposure and cytotoxics to their SMEs. Grounded in WorkSafe NZ's HCSA approach + ACC moving-and-handling guidance and the AU model WHS framework. |
| **waste-recycling-specialist** | The SME for **waste management & recycling** (one of the highest fatality-rate sectors) — kerbside collection, transfer stations, MRFs/sorting, landfills, composting, hazardous/clinical waste. Owns the sector view, the two killers (**struck-by mobile plant** + **machinery crush** — compactors/balers/shredders), and the **unknown/mixed-waste** problem including **lithium-ion battery fires**; routes traffic, machinery, chemical/biological, confined-space and CoR hazards to their SMEs. Grounded in WorkSafe NZ + WasteMINZ guidance and the AU state-WHS waste codes. |
| **oil-gas-specialist** | The SME for the **oil & gas / petroleum** sector (upstream, offshore, gas processing) — a major-accident-hazard sector on a **safety-case** regime. Owns the safety-case/Major-Accident-Event discipline, **well control/blowout** (BOP), **loss of containment → fire/explosion**, **H2S**, and offshore escape/evacuation/helicopter/SIMOPS; routes the general process-safety/MHF method to manufacturing and the generic hazards to their SMEs. Defining regime split — NZ **WorkSafe High Hazards Unit** (Petroleum E&E Regs 2016) vs AU **NOPSEMA** offshore (OPGGS Act, outside the model WHS) and state regulators onshore. |

> **Status.** Thirty-eight skills built — an orchestrator plus thirty-seven specialists spanning critical-risk,
> psychosocial risk, governance, NZ/AU duties, high-risk work, investigation, procedures and prosecution
> learning, plus a full tier of **hazard subject-matter experts** covering the recurring fatal risks:
> working at height, excavation, confined space, machinery/plant, vehicles & traffic, lifting & rigging,
> cranes & lift planning, forklifts, hazardous substances & asbestos, electrical & stored energy, water, violence & aggression, farm/agriculture, horticulture, forestry, construction, transport & logistics, manufacturing, stevedoring, mining & quarrying, commercial fishing & aquaculture, maritime & ports, healthcare & aged care, waste & recycling, oil & gas, and the electricity supply industry — each grounded in
> the relevant GPGs/Codes. Contributions and refinements welcome (see below).

### Pairs with a risk register

These skills are **tool-agnostic** and produce portable Markdown — the bow ties, task analyses,
control-assurance views, and reviews they generate are drafts you keep current somewhere. They pair
naturally with a **structured, shareable risk register** (a tool that stores risks, controls and
reviews against a configurable likelihood × consequence matrix, and shares them with the right
people). Use the skills as the *reasoning and drafting* layer; record and maintain the output in
whatever register your organisation uses. Where a skill can reach a dataset over MCP — for example a
read-only prosecutions case database — it can ground its analysis in real data (see
`prosecution-analyst`).

---

## Install

### As a Claude Code marketplace (recommended)

```bash
# add this repo as a marketplace
/plugin marketplace add scottmss/hse-nz-au-skills
# install the bundle (all skills at once)
/plugin install hse-core@hse-nz-au-skills
```

### Download a bundle (no git required)

Prebuilt zips are attached to each [GitHub Release](https://github.com/scottmss/hse-nz-au-skills/releases):

- **`hse-nz-au-skills.zip`** — the whole collection in one download.
- **`<skill-name>.zip`** — one zip per skill (the skill folder at the root), for when you only want a few.

Unzip a skill folder into `~/.claude/skills/` (Claude Code), or upload it in Claude.ai (below).

### By copying a single skill folder

```bash
git clone https://github.com/scottmss/hse-nz-au-skills.git
cp -r hse-nz-au-skills/skills/critical-risk-manager ~/.claude/skills/
```

`~/.claude/skills/` installs at user scope (all projects). A `.claude/skills/` folder inside a
project installs at project scope.

### In Claude.ai / Cowork / the API

A `SKILL.md` folder is portable. In **Claude.ai**, add each skill under **Settings → Capabilities →
Skills** by uploading its **`<skill-name>.zip`** (from a Release, or build them yourself — below).
Claude.ai adds skills one at a time, so upload the specific skills you want (e.g. `hse-advisor` plus
`critical-risk-manager`). The same files work across Claude Code, Cowork, and the API/Agent SDK.

### Building the bundles yourself

```bash
git clone https://github.com/scottmss/hse-nz-au-skills.git
cd hse-nz-au-skills
python3 scripts/bundle.py   # writes per-skill zips + hse-nz-au-skills.zip to dist/
```

`scripts/bundle.py` is pure-stdlib (no dependencies) and is what produces the Release artifacts.

---

## Security note

Skills can contain executable scripts and are a potential prompt-injection vector. **Review
`SKILL.md` and every script in a skill before enabling it**, and treat any third-party skill as
untrusted until you have audited it. This repo holds itself to that bar: no network calls, no
destructive operations, and no credential handling in any bundled script. Every script in the
repo — the bundled skill calculators (risk-matrix scorer, sling-WLL, crane-utilisation,
forklift-capacity) and the repo tooling (`validate-skills.py`, `bundle.py`) — is pure-stdlib and offline.

---

## Contributing

Contributions are welcome. Please:

- Keep everything **company-agnostic** — no brand, site, customer, or proprietary content.
- Follow the authoring conventions in [`CONTRIBUTING.md`](CONTRIBUTING.md): sharp trigger-rich
  `description`, lean `SKILL.md` body, depth pushed into `references/`, deterministic logic in
  `scripts/` over asking Claude to calculate, a jurisdiction note, declared hand-offs, and the
  disclaimer.
- Remember these skills inform safety-critical work. Accuracy against the current law and
  standards matters more than breadth.
- **Validate before you submit:** run `python3 scripts/validate-skills.py` (frontmatter,
  cross-reference paths, no stray `(planned)` tags, disclaimer, `marketplace.json` consistency).
  CI runs it, plus the `risk_matrix_scorer` self-test, on every push and pull request.

---

## Licence

[Apache-2.0](LICENSE).
