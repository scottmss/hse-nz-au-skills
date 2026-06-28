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
| **sop-author** | Writes or reviews a **Standard Operating Procedure** / safe system of work — purpose & scope, roles, the step-by-step method with hazards and controls integrated, competency sign-off, and document control. |
| **task-analysis-author** | Builds a **Task Analysis (TA) / JSA** for a specific job — steps → hazards → initial risk → controls (hierarchy) → responsible → residual risk, with a worker sign-on. Reuses the critical-risk matrix and scorer. |
| **prosecution-analyst** | Turns **NZ/AU H&S prosecution patterns** into preventive lessons and benchmarks — the enforcement/sentencing frameworks (HSWA ss 47–49 + Stumpmaster; model WHS Category 1–3 + industrial manslaughter) and the recurring duty-failure patterns. Company-agnostic and educational; not a prediction of any case. |
| **psychosocial-risk-specialist** | Identify, assess and control **psychosocial risk** (work-design hazards that cause psychological harm) — the hazard taxonomy, source-first controls, and the NZ/AU split (AU model WHS Regs 55A–55D + Code; NZ via the general duties, since "health" includes mental health). |

> **Status.** Twelve skills built — an orchestrator plus eleven specialists spanning critical-risk,
> psychosocial risk, governance, NZ/AU duties, high-risk work, investigation, procedures, and
> prosecution learning. Contributions and refinements welcome (see below).

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
# install the bundle
/plugin install hse-core@hse-nz-au-skills
```

### By copying a single skill folder

```bash
git clone https://github.com/scottmss/hse-nz-au-skills.git
cp -r hse-nz-au-skills/skills/critical-risk-manager ~/.claude/skills/
```

`~/.claude/skills/` installs at user scope (all projects). A `.claude/skills/` folder inside a
project installs at project scope.

### In Claude.ai / Cowork / the API

A `SKILL.md` folder is portable. Upload a skill — or zip a skill folder and add it as a custom
skill via the Claude.ai skills interface or the Skills API. The same files work across Claude
Code, Cowork, and the API.

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
