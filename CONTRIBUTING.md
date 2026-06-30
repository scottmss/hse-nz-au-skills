# Contributing to the NZ/AU HSE Skills collection

Thanks for helping improve this collection. It is a set of **Claude Agent Skills** for New Zealand and
Australian workplace health & safety. Each skill is a self-contained folder with a `SKILL.md` that
teaches Claude to perform one specialist HSE task in a repeatable, jurisdiction-correct way.

This guide covers the authoring conventions every skill must follow. Please read it before opening a PR.

## Ground rules

- **Not legal advice.** Skills produce drafting, structure and analysis that a competent H&S
  professional must validate against the actual site, plant, people and the current text of the law.
  **Every skill must carry this disclaimer.**
- **Keep it company-agnostic.** No company brand, logo, internal process, customer names, site
  addresses, employee names, or proprietary document templates. Contributions must be generic and
  grounded in publicly available law and regulator guidance. Read the whole skill yourself before you
  commit — an automated scan only catches your own word list.
- **One skill, one job.** Folder-per-role: each skill is a specialist (e.g. `critical-risk-manager`,
  `confined-space-specialist`) that does one thing well.
- **Run the validator.** `python3 scripts/validate-skills.py` must pass before you commit.

## 1. Frontmatter

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

- The **description is the most important line in the skill** — it is what Claude scans to decide
  whether to load it. State both *what it does* and *when to use it*, with explicit trigger phrases.
- `name` must match the folder name, lowercase-hyphenated.
- Watch the YAML: an unquoted description containing a colon-then-space can break loading — the
  validator checks for this.

## 2. Body structure

Keep `SKILL.md` bodies tight. Push depth into `references/`. A good body has:

- **Purpose** — one or two sentences.
- **When to use / when NOT to use** — explicit.
- **Method** — the step-by-step procedure Claude follows.
- **Jurisdiction note** — which law/standard applies and the default if ambiguous.
- **Output format** — the exact structure of what the skill produces.
- **Hand-offs** — which sibling skill to route to for adjacent work.
- **Disclaimer** — not legal advice; requires competent-person validation.

## 3. References and scripts

- `references/*.md` — methodology, legislative summaries, standards detail. Loaded on demand, so keep
  the `SKILL.md` lean and let depth live here.
- `scripts/*.py` — optional. Prefer **deterministic logic in code** over asking Claude to calculate
  (e.g. risk-matrix scoring, control-coverage counts). Pure-stdlib where possible. No network calls, no
  destructive operations, no credential handling in any bundled script.

## 4. Cross-skill references

Use relative paths so specialists can point at each other's reference files:

```
../worksafe-nz-specialist/references/notifiable-events.md
```

The orchestrator (`hse-advisor`) declares its routing map; each specialist declares its own hand-offs.

## 5. Region-anchor references (GPG / ACOP / Code grounding)

Hazard and activity specialists keep their **method jurisdiction-neutral** and push the
**region-specific regulatory grounding** into a dedicated anchor file per jurisdiction. This is the
pattern that makes a skill defensibly NZ- *and* AU-correct rather than skewed to one.

- **Split:** `references/good-practice.md` holds the jurisdiction-neutral controls/method (hierarchy of
  controls, critical questions). `references/nz-gpg.md` (and, where the AU side needs its own depth,
  `references/au-cop.md`) hold the region anchor — *what the regulator actually points duty-holders to*.
- **Name the real documents, not a generic gesture.** "WorkSafe working-at-height guidance" is too
  vague; cite the **Best Practice Guidelines for Working at Height in New Zealand**, the **Working on
  roofs GPG**, etc., with their URLs. See `working-at-height-specialist/references/nz-gpg.md` for the
  pattern.
- **Capture the jurisdiction-specific *principle*, not just the document** — e.g. NZ has **no minimum
  height** (the "three-metre rule" is a myth); the 5 m figure is only a notification/competency
  threshold. These framing facts are what a generic controls list misses.
- **Verify-pointer discipline.** Every cited GPG/Code/standard is a **verify-pointer** — summarise and
  link, **never wholesale-copy**. NZ GPGs/ACOPs and AU model Codes are free to reference with
  attribution; **AS/NZS standards are copyright** — cite and apply, don't reproduce.
- **Stamp a `Sources last verified: YYYY-MM-DD` line** in each anchor file, and verify NZ legislative
  facts against the regulator before asserting them.
- Apply this to any skill where one jurisdiction is thinly grounded.

## 6. Security note

Skills can contain executable scripts and can be a prompt-injection vector. Treat any third-party skill
as untrusted until you have reviewed its `SKILL.md` and all scripts. This repo holds itself to that
bar: no network calls, no destructive operations, no credential handling in any bundled script.

## 7. Before you open a PR — checklist

- [ ] Sharp, trigger-rich `description`.
- [ ] Body lean; depth pushed into `references/`.
- [ ] Deterministic `scripts/` preferred over asking Claude to calculate.
- [ ] Jurisdiction note + disclaimer present.
- [ ] Hand-offs to sibling skills declared.
- [ ] Region anchors carry verify-pointers + a `Sources last verified` date.
- [ ] Company-agnostic — no proprietary or organisation-specific content.
- [ ] `python3 scripts/validate-skills.py` passes.
- [ ] `marketplace.json` and the README roster updated if you added a skill.
