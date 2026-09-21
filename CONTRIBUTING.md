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
description: Build or review a bow tie for a critical (fatal) risk — top event, threats,
  consequences, barriers, escalation factors — then assess critical-control assurance and score
  residual risk on the risk matrix. NZ/AU. Use before starting any bow tie.
---
```

- The **description is the most important line in the skill** — it is what Claude scans to decide
  whether to load it. State *what it does* and *when to use it*, leading with the words a user would
  actually say.
- **Keep it short — aim for ~250 characters, never over 300.** Claude loads *every* installed
  skill's description into context on every turn, inside a fixed budget of roughly 8,000 characters
  shared with all the user's other skills. Go over and Claude keeps the skill names but silently
  drops descriptions, and skills stop triggering. (v1.x descriptions averaged ~900 characters; a
  full install was 5× over budget and users could not see most of the skills.) The validator warns
  above 300 and **fails above 1,024**, the Agent Skills spec maximum — Claude.ai rejects the upload.
- **Put the long trigger list in the orchestrator, not the description.** The `hse-advisor` routing
  map is where the exhaustive keywords belong: it loads on demand and costs nothing against the budget.
- Name the sibling a user is most likely to confuse it with ("For slings use
  lifting-rigging-specialist"). Skip "Not legal advice" here — the body carries the disclaimer.
- `name` must match the folder name, lowercase-hyphenated.
- Watch the YAML: an unquoted description containing a colon-then-space can break loading — the
  validator checks for this. When wrapping the description over several lines, never break straight
  after a hyphen: YAML folds the line break into a space, turning `de-rating` into `de- rating`.

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

Packs install into **separate folders**, so a skill can only reach files in its own pack. Three
forms, each checked by the validator:

| To… | Write | Example |
|---|---|---|
| hand off to another skill (any pack) | its **name** | `` `crane-specialist` `` |
| point at a file in **your own pack** | a relative path | `` `../critical-risk-manager/references/control-assurance.md` `` |
| point at a file in **another pack** | `skill:path` | `` `worksafe-nz-specialist:references/overlapping-duties.md` `` |

- **Hand off by name, never by path.** `` `../crane-specialist/` `` fails validation if the skill is in
  another pack, and breaks silently the day a skill moves. The name always works.
- `skill:path` means *that file inside that skill* — Claude invokes the skill to reach it. Keep these
  rare: if the other pack isn't installed the pointer is a dead end, so say enough inline that the
  reader isn't stranded.
- Inside a `references/` file, remember a relative path starts from that folder
  (`../../other-skill/references/x.md`, or `../scripts/tool.py` for your own skill's script).

The orchestrator (`hse-advisor`) declares its routing map; each specialist declares its own hand-offs.

## 4a. Packs and bundles

The collection installs as **packs** — `hse-core`, `hse-hazards`, `hse-plant` and the `hse-sector-*`
packs — so users load only what they need and stay inside the description budget. Each pack is a
real plugin folder:

```
packs/hse-plant/
├── .claude-plugin/plugin.json      name, version, description, author, dependencies
└── skills/
    ├── crane-specialist/SKILL.md
    └── …
```

**The folder a skill sits in is its pack.** There is no separate list to keep in step: Claude Code
scans the pack's `skills/` folder, and a plugin manager counts what is on disk. (v2.0.0 carved every
pack out of one shared `skills/` folder; each install then held all 48 skills on disk and plugin
managers showed "48 skills" for every pack.) When you add a skill:

1. **Put it in exactly one pack** — `packs/<pack>/skills/<name>/`. Core is for the orchestrator and
   cross-cutting method/law skills; hazards, plant and sectors go in their packs. Start a new
   `hse-sector-*` pack rather than letting one grow past ~6 skills.
2. **Add a routing row** for it in the `hse-advisor` routing map — this is where its full trigger
   vocabulary lives.
3. **Add it to the pack table** in `hse-advisor` ("Packs — when a specialist isn't installed") and to
   the README roster (with its pack) and install table.
4. **Bump the version everywhere together** with `python3 scripts/bump-version.py X.Y.Z`. Installs
   are pinned by version: a pack whose version doesn't change never updates for existing users.

The validator enforces all four, and prints each pack's and bundle's description cost.

**A new pack** needs `packs/<name>/.claude-plugin/plugin.json` (copy a sibling's; keep
`"dependencies": ["hse-core"]` — every specialist hands off into core) and a marketplace entry whose
`source` is `./packs/<name>`. Keep `version` in `plugin.json` only — if the marketplace entry sets one
too, `plugin.json` silently wins — and keep the `description` identical in both.

**Bundles** (`hse-for-construction-industrial`, `hse-everything`, …) give users a one-step install.
Each is a folder under `bundles/` holding only `.claude-plugin/plugin.json` — a `name`, a `version`
and a `dependencies` list of packs — plus a marketplace entry whose `source` is that folder. A bundle
carries no skills, so a new skill needs no bundle change; a new **pack** should be added to the
bundles it belongs in (always to `hse-everything`).

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

- [ ] Sharp `description` — what + when, ~250 characters, never over 300.
- [ ] Body lean; depth pushed into `references/`.
- [ ] Deterministic `scripts/` preferred over asking Claude to calculate.
- [ ] Jurisdiction note + disclaimer present.
- [ ] Hand-offs to sibling skills declared.
- [ ] Region anchors carry verify-pointers + a `Sources last verified` date.
- [ ] Company-agnostic — no proprietary or organisation-specific content.
- [ ] `python3 scripts/validate-skills.py` passes.
- [ ] Hand-offs written as skill names; no `../` path into another pack.
- [ ] If you added a skill: placed in exactly one pack folder, given a routing row and a pack-table
      entry in `hse-advisor`, added to the README roster, and the version bumped with `bump-version.py`.
