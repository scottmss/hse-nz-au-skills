# CLAUDE.md — NZ/AU Health & Safety Skills Collection

> Working guide for Claude Code / Cowork sessions on this repository.
> Read this first. It defines what we are building, how the repo is structured,
> the conventions every skill must follow, and how the collection is published
> and consumed.

---

## 1. What this project is

This is an open-source collection of **Claude Agent Skills focused on New Zealand and
Australian workplace health & safety (WHS / HSWA)**.

Each skill is a self-contained folder with a `SKILL.md` file that teaches Claude how to
perform a specialist HSE task in a repeatable, jurisdiction-correct way — building bow tie
risk assessments, running incident investigations, drafting safe systems of work, scoring
critical-risk control assurance, and reasoning about NZ/AU duty-holder obligations.

The architecture is modelled on the `ra-qm-team` pattern from the community
`alirezarezvani/claude-skills` library: a **folder-per-specialist-role**, where skills can
reference one another and an **orchestrator skill routes a query to the right specialist**.
That library proved the model for regulated quality/compliance work (ISO 13485, ISO 27001,
GDPR, MDR, FDA). This repo applies the same model to a domain that has **no public
equivalent**: occupational H&S grounded in NZ and Australian law.

### Why this exists (the white space)

The public Claude skills ecosystem is almost entirely software engineering, cybersecurity,
and international GRC compliance. A focused search across GitHub and the skill marketplaces
found **no genuine occupational/workplace HSE skills** grounded in:

- **HSWA 2015 (NZ)** — PCBU duties, officer due-diligence, notifiable events, WorkSafe NZ enforcement
- **WHS Act (AU model law)** — state/territory variations, SafeWork jurisdictions, Comcare
- **High-risk work** — NZ/AU crane, dogging, rigging, scaffolding, EWP licence classes
- **AS/NZS standards** — lifting, working at height, plant, electrical
- **Critical-risk / bow tie methodology** as applied in NZ/AU heavy industry, utilities, and construction
- **NZ/AU prosecution case patterns** as a learning and benchmarking source

This is a genuine gap. The skills in this repo are intended to be the most capable publicly
available occupational-HSE skills in the ecosystem.

---

## 2. What this project is NOT

- **Not legal advice.** Skills produce drafting, structure, and analysis that a competent
  H&S professional must review and validate against the actual site, plant, people, and the
  current text of the law. Every skill must carry this disclaimer.
- **Not a replacement for a qualified HSE practitioner or lawyer.**
- **Not organisation-specific.** This public repo contains **generic, company-agnostic**
  skills only. Anything carrying a specific company's brand, internal process, customer
  names, site detail, or proprietary content stays in a **separate private repo** (see §6).
- **Not a live data product.** Skills are instruction documents. Where a skill references a
  knowledge base (e.g. prosecutions), the data product itself is separate and is not bundled
  into this public repo.

---

## 3. Architecture model (the `ra-qm-team` pattern)

Three structural ideas, copied from the proven model:

1. **Folder-per-role.** Each skill is a specialist (e.g. `critical-risk-manager`,
   `incident-investigator`, `worksafe-nz-specialist`). One job, done well.

2. **Skills reference each other.** A skill's `SKILL.md` may point to sibling skills'
   reference files using relative paths. The orchestrator returns findings and routes
   follow-on work to the right specialist rather than duplicating it.

3. **Progressive disclosure.** Claude scans skill *descriptions* first (~cheap), loads the
   full `SKILL.md` only when a skill applies, and loads bundled `references/` and `scripts/`
   only as needed. This keeps many skills available without flooding the context window.

An **orchestrator skill** (`hse-advisor`) sits on top. It does not do deep work itself; it
identifies the jurisdiction and task and hands off to the correct specialist.

---

## 4. Repository structure

```
hse-nz-au-skills/
├── CLAUDE.md                      ← this file
├── README.md                     ← public-facing intro + install instructions
├── LICENSE                       ← see §11
├── .claude-plugin/
│   └── marketplace.json          ← lets Claude Code add this repo as a marketplace
│
├── skills/
│   │
│   ├── hse-advisor/              ← ORCHESTRATOR (routes to specialists)
│   │   ├── SKILL.md
│   │   └── references/
│   │       ├── hswa-nz-overview.md
│   │       └── whs-au-overview.md
│   │
│   ├── critical-risk-manager/    ← bow tie + critical-risk control assurance
│   │   ├── SKILL.md
│   │   ├── references/
│   │   │   ├── bowtie-methodology.md        (6M method, Aust & Pons 2020)
│   │   │   ├── critical-risk-definitions.md
│   │   │   └── control-assurance.md
│   │   └── scripts/
│   │       └── risk_matrix_scorer.py        (optional)
│   │
│   ├── incident-investigator/    ← Five Whys + structured investigation
│   │   ├── SKILL.md
│   │   └── references/
│   │       └── investigation-methodology.md
│   │
│   ├── complex-problem-analyst/  ← Fishbone / Ishikawa for multi-causal events
│   │   ├── SKILL.md
│   │   └── references/
│   │       └── ishikawa-6m.md
│   │
│   ├── worksafe-nz-specialist/   ← HSWA duties, notifiable events, WorkSafe NZ
│   │   ├── SKILL.md
│   │   └── references/
│   │       ├── hswa-2015-duties.md
│   │       └── notifiable-events.md
│   │
│   ├── safework-au-specialist/   ← WHS Act (model law) + jurisdiction variations
│   │   ├── SKILL.md
│   │   └── references/
│   │       └── whs-act-model-regs.md
│   │
│   ├── high-risk-work-specialist/← cranes, dogging, rigging, scaffolding, EWP
│   │   ├── SKILL.md
│   │   └── references/
│   │       ├── hrwl-classes.md
│   │       └── as-nzs-standards.md
│   │
│   ├── sop-author/               ← safe systems of work / SOP structure
│   │   ├── SKILL.md
│   │   └── references/
│   │       └── sop-structure.md
│   │
│   ├── task-analysis-author/     ← JSA / task analysis (step → hazard → control)
│   │   ├── SKILL.md
│   │   └── references/
│   │       └── ta-structure.md
│   │
│   └── prosecution-analyst/      ← learn from NZ/AU HSE prosecution case patterns
│       ├── SKILL.md              (company-agnostic — see §6)
│       └── references/
│           └── nz-au-prosecution-patterns.md
│
└── scripts/                      ← repo-level tooling (optional)
    └── validate-skills.py        ← lints every SKILL.md before commit
```

The roster above is the **target** state. Ship incrementally — a repo with three solid
skills is more useful than ten thin ones.

---

## 5. Skill authoring conventions

Every skill **must** follow these rules.

### 5.1 Frontmatter

```markdown
---
name: critical-risk-manager
description: Use this skill when building or reviewing a bow tie risk assessment,
  defining a critical risk, assessing control assurance, or scoring residual risk
  for NZ/AU workplace hazards. Triggers on "bow tie", "critical risk", "control
  assurance", "top event", "barrier analysis", "risk matrix". Grounded in HSWA 2015
  (NZ) and the WHS model law (AU).
---
```

- The **description is the most important line in the skill** — it is what Claude scans to
  decide whether to load the skill. State both *what it does* and *when to use it*, with
  explicit trigger phrases.
- `name` must match the folder name, lowercase-hyphenated.

### 5.2 Body structure

Keep `SKILL.md` bodies tight. Push depth into `references/`. A good body has:

- **Purpose** — one or two sentences.
- **When to use / when NOT to use** — explicit.
- **Method** — the step-by-step procedure Claude follows.
- **Jurisdiction note** — which law/standard applies and the default if ambiguous.
- **Output format** — the exact structure of what the skill produces.
- **Hand-offs** — which sibling skill to route to for adjacent work.
- **Disclaimer** — not legal advice; requires competent-person validation.

### 5.3 References and scripts

- `references/*.md` — methodology, legislative summaries, standards detail. Loaded on demand.
- `scripts/*.py` — optional. Prefer **deterministic logic in code** over asking Claude to
  calculate (e.g. risk-matrix scoring, control-coverage counts). Pure-stdlib where possible.

### 5.4 Cross-skill references

Use relative paths, mirroring the `ra-qm-team` convention:

```
../worksafe-nz-specialist/references/notifiable-events.md
```

The orchestrator declares its routing map; specialists declare their hand-offs.

---

## 6. Public vs private separation (CRITICAL)

This repo is **public and company-agnostic**. Two hard rules:

1. **No organisation-specific content.** No company brand, logo, internal process, customer
   names, site addresses, employee names, or proprietary document templates. Org-specific
   skills live in a **separate private repo** and may *depend on* these public skills, never
   the reverse.

2. **Prosecution content stays company-agnostic.** The `prosecution-analyst` skill teaches
   Claude to reason about NZ/AU prosecution *patterns and lessons* in general terms. It must
   not reference any single organisation's relevance, and it must not bundle or expose the
   underlying multi-tenant prosecutions data product. Keep it about the public case law and
   the method of learning from it.

**Sanitisation before every commit:** read the whole skill yourself. A clean automated scan
is not a clean bill of health — grep only catches your own word list. Look for any concrete
name, site, or snippet that was lifted from a real internal project, and genericise it.

---

## 7. Mapping from existing material

Where private/org-specific skills already exist, the public generic skill is the
de-branded distillation of the method:

| Existing private/method asset      | Public generic skill            |
|------------------------------------|---------------------------------|
| Bow tie methodology                | `critical-risk-manager`         |
| Five Whys RCA                      | `incident-investigator`         |
| Complex problem analysis (Fishbone)| `complex-problem-analyst`       |
| Risk register method               | `critical-risk-manager`         |
| SOP authoring method               | `sop-author`                    |
| Task analysis / JSA method         | `task-analysis-author`          |
| Investigation report method        | `incident-investigator`         |
| Prosecutions knowledge (patterns)  | `prosecution-analyst`           |

The org-agnostic methodology skills are essentially publishable as-is. The branded ones need
a generic counterpart authored from the underlying method, not copied from the branded file.

---

## 8. Creating the public GitHub repository

Step-by-step. Run from the directory where you want the repo to live.

### 8.1 Create the repo

Option A — GitHub web UI:
1. New repository → name e.g. `hse-nz-au-skills`.
2. Public. Add a README and a LICENSE (MIT or Apache-2.0 — see §11).
3. Clone it locally.

Option B — GitHub CLI:

```bash
gh repo create hse-nz-au-skills --public --license apache-2.0 \
  --description "NZ/AU workplace health & safety Claude Agent Skills" --clone
cd hse-nz-au-skills
```

### 8.2 Scaffold the structure

```bash
mkdir -p skills scripts .claude-plugin
# create the first skill
mkdir -p skills/critical-risk-manager/references skills/critical-risk-manager/scripts
```

Use the `skill-creator` skill in Claude Code to author each `SKILL.md` from your reference
material rather than writing them by hand — it enforces good frontmatter and structure.

### 8.3 Add the marketplace manifest

Create `.claude-plugin/marketplace.json` so the repo can be added as a Claude Code
marketplace. Minimal form, declaring skills directly (no per-skill plugin.json required):

```json
{
  "name": "hse-nz-au-skills",
  "owner": { "name": "YOUR_GH_USERNAME", "email": "you@example.com" },
  "description": "NZ/AU workplace health & safety Claude Agent Skills",
  "plugins": [
    {
      "name": "hse-core",
      "source": "./",
      "strict": false,
      "skills": [
        "skills/hse-advisor",
        "skills/critical-risk-manager",
        "skills/incident-investigator",
        "skills/complex-problem-analyst",
        "skills/worksafe-nz-specialist",
        "skills/safework-au-specialist",
        "skills/high-risk-work-specialist",
        "skills/sop-author",
        "skills/task-analysis-author",
        "skills/prosecution-analyst"
      ]
    }
  ]
}
```

### 8.4 Write the README

The README is the front door. Include: what it is, the disclaimer, the skill roster with
one-line descriptions, install instructions (§9), and a contribution note.

### 8.5 Commit and push

```bash
git add .
git commit -m "Initial scaffold: hse-advisor + critical-risk-manager"
git push origin main
```

Ship a small, working first version. Add specialists in later commits.

---

## 9. How it is consumed (installation)

Three ways a user gets these skills, in order of convenience:

### As a Claude Code marketplace
```bash
# add this repo as a marketplace
/plugin marketplace add YOUR_GH_USERNAME/hse-nz-au-skills
# install the bundle
/plugin install hse-core@hse-nz-au-skills
```

### By copying a single skill folder
```bash
git clone https://github.com/YOUR_GH_USERNAME/hse-nz-au-skills.git
cp -r hse-nz-au-skills/skills/critical-risk-manager ~/.claude/skills/
```
(`~/.claude/skills/` = user scope, all projects. `.claude/skills/` in a project = project scope.)

### In Claude.ai / Cowork / the API
A `SKILL.md` folder is portable. Upload a skill, or zip a skill folder and add it as a
custom skill via the Claude.ai skills interface or the Skills API. The same files work
across Claude Code, Cowork, and the API.

---

## 10. How it works at runtime

1. User asks something HSE-related ("build me a bow tie for a tandem crane lift").
2. Claude scans skill **descriptions**; `hse-advisor` (orchestrator) and
   `critical-risk-manager` match.
3. The orchestrator identifies jurisdiction + task and routes to `critical-risk-manager`.
4. That skill loads its `SKILL.md`, pulls `references/bowtie-methodology.md`, and (if used)
   runs `scripts/risk_matrix_scorer.py` for deterministic scoring.
5. Output is produced in the skill's defined format, with the disclaimer.
6. For adjacent work (e.g. "is this a notifiable event?") the skill hands off to
   `worksafe-nz-specialist`.

The value of the collection is the **routing + jurisdiction-correctness + method
consistency** — not any single prompt.

---

## 11. Licensing

Pick before first publish:

- **Apache-2.0** — permissive, with an explicit patent grant. Good default for something you
  may later want recognised as the canonical implementation.
- **MIT** — simplest permissive licence; most community skill repos use it.

If any of this methodology has commercial value you intend to capture (e.g. via a paid
product), consider keeping the deepest/most differentiated skills private and publishing a
strong-but-foundational public core. Decide the public/private line deliberately — it is hard
to un-publish.

---

## 12. Security note for consumers

Skills can contain executable scripts and can be a prompt-injection vector. The README should
tell users to review `SKILL.md` and all scripts before enabling a skill, and to treat any
third-party skill as untrusted until audited. This repo should hold itself to that same bar:
no network calls, no destructive operations, no credential handling in any bundled script.

---

## 13. Build workflow checklist

When adding or editing a skill in a session:

- [ ] Read this CLAUDE.md.
- [ ] Use `skill-creator` to scaffold or revise the `SKILL.md`.
- [ ] Write a sharp, trigger-rich `description`.
- [ ] Keep the body lean; push depth into `references/`.
- [ ] Prefer deterministic `scripts/` over asking Claude to calculate.
- [ ] Add jurisdiction note + disclaimer.
- [ ] Declare hand-offs to sibling skills.
- [ ] Sanitise: no org-specific or proprietary content (§6).
- [ ] Run `scripts/validate-skills.py` (once it exists).
- [ ] Update `marketplace.json` and the README roster.
- [ ] Commit small; ship incrementally.
