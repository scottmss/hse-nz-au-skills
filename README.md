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

> **Roadmap.** Further specialists are planned — `high-risk-work-specialist`, `sop-author`,
> `task-analysis-author`, and `prosecution-analyst`. The collection ships incrementally;
> a small set of solid skills beats a large set of thin ones.

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

---

## Licence

[Apache-2.0](LICENSE).
