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
| **water-safety-specialist** | The SME for **working in/on/above water** — prevent the fall in, lifejackets, safety observer, water rescue, conditions monitoring, and diving (AS 4758; AS/NZS 2299; Maritime NZ). |
| **violence-aggression-specialist** | The SME for **work-related violence & aggression** — design out the opportunity, lone/in-home worker controls, de-escalation, duress/security, and post-incident support (WorkSafe Violence at work; AU violence guidance). Partners psychosocial-risk-specialist. |

> **Status.** Twenty-four skills built — an orchestrator plus twenty-three specialists spanning critical-risk,
> psychosocial risk, governance, NZ/AU duties, high-risk work, investigation, procedures and prosecution
> learning, plus a full tier of **hazard subject-matter experts** covering the recurring fatal risks:
> working at height, excavation, confined space, machinery/plant, vehicles & traffic, lifting & rigging,
> cranes & lift planning, forklifts, hazardous substances & asbestos, electrical & stored energy, water, and violence & aggression — each grounded in
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
destructive operations, and no credential handling in any bundled script. The only script today,
`risk_matrix_scorer.py`, is pure-stdlib and offline.

---

## Contributing

Contributions are welcome. Please:

- Keep everything **company-agnostic** — no brand, site, customer, or proprietary content.
- Follow the authoring conventions in [`CLAUDE.md`](CLAUDE.md) (§5): sharp trigger-rich
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
