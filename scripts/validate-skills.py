#!/usr/bin/env python3
"""validate-skills.py — lint every SKILL.md before commit.

Repo-level linter for the hse-nz-au-skills collection. Checks each skill's
frontmatter and body, that cross-references resolve, that no stray "(planned)"
tags remain, and that the packs, bundles, marketplace.json, the hse-advisor
orchestrator and the README all agree with the skills on disk.

Layout it enforces:

    packs/<pack>/.claude-plugin/plugin.json     one installable plugin per pack
    packs/<pack>/skills/<skill>/SKILL.md        a skill lives in exactly one pack
    bundles/<name>/.claude-plugin/plugin.json   no skills — only `dependencies` on packs
    .claude-plugin/marketplace.json             one entry per pack and per bundle

Pure standard library. No network, no writes. Run from anywhere:

    python3 scripts/validate-skills.py

Exit codes: 0 = all checks passed, 1 = one or more errors.
"""
from __future__ import annotations

import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PACKS_DIR = os.path.join(ROOT, "packs")
BUNDLES_DIR = os.path.join(ROOT, "bundles")
MARKETPLACE = os.path.join(ROOT, ".claude-plugin", "marketplace.json")
ROOT_PLUGIN_MANIFEST = os.path.join(ROOT, ".claude-plugin", "plugin.json")
LEGACY_SKILLS_DIR = os.path.join(ROOT, "skills")
PACK_PREFIX = "./packs/"
# A bundle is a plugin with no skills of its own — only `dependencies` on packs — so
# one install pulls in a curated set. Each lives in its own folder under bundles/.
BUNDLE_PREFIX = "./bundles/"
# Every specialist hands off into this pack (the orchestrator, the NZ/AU law skills,
# critical risk...), so every other pack depends on it.
CORE_PACK = "hse-core"
ORCHESTRATOR = "hse-advisor"

# Agent Skills spec (agentskills.io/specification): description is 1-1024 chars.
# Claude Code tolerates more (it caps each listing entry at 1,536), but claude.ai /
# Claude Desktop skill upload and the API reject anything over 1024.
DESC_MAX_CHARS = 1024
# Claude Code lists every skill's description in context on every turn, within a
# budget of 1% of the context window (~8,000 chars at 200k). Over budget it keeps
# the skill names but drops descriptions, least-invoked first — on a fresh install
# that means most skills show with no description and stop triggering.
LISTING_BUDGET_CHARS = 8000
# A pack should leave room for the user's other packs and skills.
PACK_BUDGET_CHARS = LISTING_BUDGET_CHARS // 2
# Soft per-skill target. Descriptions stay short because the trigger vocabulary
# lives in the orchestrator's routing map, which loads on demand and costs nothing.
DESC_TARGET_CHARS = 300

NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
# A backtick code-span whose entire content looks like an internal relative path.
PATH_RE = re.compile(r"^(?:\.\.?/|references/|scripts/)[\w./-]+$")
# A pointer at a file inside ANOTHER skill: `worksafe-nz-specialist:references/x.md`.
# Packs install into separate folders, so a ../ path cannot cross from one pack to
# another — this form names the skill and lets it resolve wherever that skill lives.
SKILL_FILE_RE = re.compile(r"^([a-z0-9]+(?:-[a-z0-9]+)*):((?:references|scripts)/[\w./-]+|SKILL\.md)$")
# A backtick span that is shaped like one of our skill names.
SKILL_NAME_SHAPE_RE = re.compile(
    r"^[a-z0-9]+(?:-[a-z0-9]+)*-(?:specialist|advisor|author|analyst|manager|investigator|reviewer)$")
BACKTICK_RE = re.compile(r"`([^`]+)`")

errors: list[str] = []
warnings: list[str] = []
desc_lengths: dict[str, int] = {}
skills: dict[str, tuple[str, str]] = {}   # skill name -> (pack name, skill dir)
packs: dict[str, list[str]] = {}          # pack name -> skill names (from the folders)
bundles: dict[str, list[str]] = {}        # bundle name -> pack names it installs


def err(where: str, msg: str) -> None:
    errors.append(f"  [FAIL] {where}: {msg}")


def warn(where: str, msg: str) -> None:
    warnings.append(f"  [warn] {where}: {msg}")


def subdirs(path: str) -> list[str]:
    if not os.path.isdir(path):
        return []
    return sorted(d for d in os.listdir(path)
                  if os.path.isdir(os.path.join(path, d)) and not d.startswith("."))


def load_json(path: str, where: str):
    try:
        with open(path, encoding="utf-8") as fh:
            return json.load(fh)
    except FileNotFoundError:
        err(where, f"missing {os.path.relpath(path, ROOT)}")
    except json.JSONDecodeError as e:
        err(where, f"{os.path.relpath(path, ROOT)} is invalid JSON: {e}")
    return None


# --------------------------------------------------------------------------- skills

def split_frontmatter(text: str):
    """Return (frontmatter_str, body_str) or (None, text) if no frontmatter."""
    if not text.startswith("---"):
        return None, text
    parts = text.split("\n")
    if parts[0].strip() != "---":
        return None, text
    for i in range(1, len(parts)):
        if parts[i].strip() == "---":
            return "\n".join(parts[1:i]), "\n".join(parts[i + 1:])
    return None, text


def frontmatter_value(fm: str, key: str):
    """Minimal YAML scalar lookup for a top-level `key:` (handles quotes)."""
    m = re.search(rf"(?m)^{re.escape(key)}:\s*(.*)$", fm)
    if not m:
        return None
    val = m.group(1).strip()
    if (val.startswith('"') and val.endswith('"')) or (val.startswith("'") and val.endswith("'")):
        val = val[1:-1]
    return val


def has_key(fm: str, key: str) -> bool:
    return re.search(rf"(?m)^{re.escape(key)}:", fm) is not None


def description_text(fm: str) -> str:
    """The description as a YAML loader would see it: continuation lines folded to
    single spaces, block-scalar indicator and surrounding quotes removed. Used for
    length checks, where `frontmatter_value` (first line only) under-counts."""
    m = re.search(r"(?ms)^description:[ \t]*(.*?)(?=^\S[^:\n]*:|\Z)", fm)
    if not m:
        return ""
    lines = [ln.strip() for ln in m.group(1).strip().split("\n")]
    if lines and re.match(r"^[>|][+-]?\d*$", lines[0]):
        lines = lines[1:]
    val = " ".join(ln for ln in lines if ln)
    if len(val) >= 2 and val[0] in "\"'" and val[-1] == val[0]:
        val = val[1:-1]
    return val


def check_cross_refs(skill: str, md_path: str) -> None:
    """Every backtick span that points somewhere must point at something real:
    a relative path, a `skill:file` pointer, or another skill's name."""
    base = os.path.dirname(md_path)
    rel = os.path.relpath(md_path, ROOT)
    with open(md_path, encoding="utf-8") as fh:
        content = fh.read()
    for span in BACKTICK_RE.findall(content):
        s = span.strip()
        if "://" in s or " " in s:
            continue
        if PATH_RE.match(s):
            target = os.path.normpath(os.path.join(base, s.rstrip("/")))
            if os.path.exists(target):
                continue
            # Name the usual cause: a ../ path aimed at a skill in another pack.
            parts = target.split(os.sep)
            other = parts[parts.index("skills") + 1] if "skills" in parts[:-1] else None
            if other in skills and skills[other][0] != skills[skill][0]:
                tail = "/".join(parts[parts.index("skills") + 2:])
                fix = f"`{other}:{tail}`" if tail else f"`{other}`"
                err(skill, f"`{s}` in {rel} reaches into another pack ({skills[other][0]}) — packs "
                    f"install into separate folders, so write {fix} instead")
            else:
                err(skill, f"unresolved reference `{s}` in {rel}")
            continue
        m = SKILL_FILE_RE.match(s)
        if m:
            other, path = m.groups()
            if other not in skills:
                err(skill, f"`{s}` in {rel} names a skill that does not exist")
            elif not os.path.exists(os.path.join(skills[other][1], path)):
                err(skill, f"`{s}` in {rel}: no such file in {other}")
            continue
        if SKILL_NAME_SHAPE_RE.match(s) and s not in skills:
            err(skill, f"`{s}` in {rel} looks like a skill hand-off, but no such skill exists")


def check_planned_tags(skill: str, md_path: str) -> None:
    with open(md_path, encoding="utf-8") as fh:
        if "(planned)" in fh.read():
            rel = os.path.relpath(md_path, ROOT)
            err(skill, f"stray '(planned)' tag in {rel}")


def md_files(skill_dir: str):
    for dirpath, _dirs, files in os.walk(skill_dir):
        for f in files:
            if f.endswith(".md"):
                yield os.path.join(dirpath, f)


def frontmatter_yaml_issues(fm: str) -> list[str]:
    """Detect plain-scalar YAML hazards in top-level frontmatter values.

    A ``: `` (colon-space) or `` #`` (space-hash) inside an UNQUOTED scalar makes a
    YAML parser misread it as a mapping / comment, and the skill fails to load.
    This is the bug class the basic key checks miss.
    """
    issues: list[str] = []
    cur_key = None
    quoted = False
    for ln in fm.split("\n"):
        m = re.match(r"^(\S[^:]*):(.*)$", ln)
        if m and not ln[:1].isspace():
            cur_key = m.group(1).strip()
            seg = m.group(2)
            quoted = seg.lstrip().startswith(('"', "'"))
        else:
            seg = ln  # continuation line of the current key's value
        if cur_key == "description" and not quoted:
            snippet = seg.strip()[:70]
            if ": " in seg:
                issues.append(f"unquoted description contains ': ' (breaks YAML load) — …{snippet}")
            if " #" in seg:
                issues.append(f"unquoted description contains ' #' (YAML comment hazard) — …{snippet}")
    return issues


def validate_skill(name: str) -> None:
    skill_dir = skills[name][1]
    skill_md = os.path.join(skill_dir, "SKILL.md")
    if not os.path.isfile(skill_md):
        err(name, "missing SKILL.md")
        return

    with open(skill_md, encoding="utf-8") as fh:
        text = fh.read()
    fm, body = split_frontmatter(text)
    if fm is None:
        err(name, "SKILL.md has no YAML frontmatter")
    else:
        fm_name = frontmatter_value(fm, "name")
        if not fm_name:
            err(name, "frontmatter missing 'name'")
        elif fm_name != name:
            err(name, f"frontmatter name '{fm_name}' != folder name '{name}'")
        elif not NAME_RE.match(fm_name):
            err(name, f"name '{fm_name}' is not lowercase-hyphenated")
        if not has_key(fm, "description"):
            err(name, "frontmatter missing 'description'")
        else:
            # description may be a YAML block scalar; approximate length from the FM region.
            desc_region = fm[fm.find("description:"):]
            if len(desc_region) < 80:
                warn(name, "description looks very short — say what it does and when to use it")
            desc_len = len(description_text(fm))
            desc_lengths[name] = desc_len
            if desc_len > DESC_MAX_CHARS:
                err(name, f"description is {desc_len} chars — Agent Skills spec max is "
                    f"{DESC_MAX_CHARS} (over by {desc_len - DESC_MAX_CHARS}); "
                    "claude.ai / Desktop upload rejects it")
        for issue in frontmatter_yaml_issues(fm):
            err(name, issue)

    low = body.lower()
    if "disclaimer" not in low and "not legal advice" not in low:
        err(name, "no disclaimer / 'not legal advice' statement in body")

    for md in md_files(skill_dir):
        check_cross_refs(name, md)
        check_planned_tags(name, md)


def discover_skills() -> None:
    """Fill `packs` and `skills` from the folders. The folder a skill sits in IS its
    pack — a plugin manager counts what is on disk, so nothing else may decide it."""
    for pack in subdirs(PACKS_DIR):
        packs[pack] = []
        for name in subdirs(os.path.join(PACKS_DIR, pack, "skills")):
            if name in skills:
                err(name, f"exists in two packs ({skills[name][0]} and {pack}) — "
                    "a skill belongs to exactly one")
                continue
            skills[name] = (pack, os.path.join(PACKS_DIR, pack, "skills", name))
            packs[pack].append(name)
        if not packs[pack]:
            err(pack, "pack folder has no skills/")
    # A skill added the v1/v2.0 way would be in no pack, and would never install.
    for stray in subdirs(LEGACY_SKILLS_DIR):
        err(stray, "is in the old top-level skills/ folder — move it to packs/<pack>/skills/")


# ------------------------------------------------------------------ packs & bundles

def validate_plugin_folder(label: str, entry: dict, folder: str):
    """Checks shared by packs and bundles. Returns the parsed plugin.json, or None."""
    # plugin.json's version silently wins over the entry's, so keep it in one place.
    if entry.get("version"):
        err(label, "set 'version' in the plugin.json only, not on the marketplace entry")
    data = load_json(os.path.join(folder, ".claude-plugin", "plugin.json"), label)
    if data is None:
        return None
    if data.get("name") != label:
        err(label, f"plugin.json name '{data.get('name')}' != marketplace entry name '{label}'")
    if not data.get("version"):
        err(label, "plugin.json has no 'version' — installs are pinned by version, so users "
            "would never receive an update")
    # The description sits in both places (the official validator wants it in
    # plugin.json; marketplace browsers read the entry) — keep them identical.
    if data.get("description") != entry.get("description"):
        err(label, "plugin.json 'description' differs from its marketplace.json entry")
    return data


def dependency_names(data: dict) -> list[str]:
    return [d if isinstance(d, str) else d.get("name") for d in data.get("dependencies", [])]


def validate_pack(label: str, entry: dict):
    """A pack = packs/<name>/ with its own plugin.json and a skills/ folder, which
    Claude Code scans. Returns its version (or None)."""
    folder_name = entry["source"][len(PACK_PREFIX):].rstrip("/")
    if folder_name != label:
        err(label, f"source folder 'packs/{folder_name}' must be named after the plugin")
    if label not in packs:
        err(label, f"marketplace.json lists it but there is no packs/{folder_name}/ folder")
        return None
    # The skills/ folder is the list. A second list here could only disagree with it.
    if "skills" in entry:
        err(label, "remove 'skills' from the marketplace entry — the pack's skills/ folder is "
            "scanned, and that folder is what decides membership")
    if entry.get("strict") is False:
        err(label, "remove \"strict\": false — the pack has its own plugin.json")
    data = validate_plugin_folder(label, entry, os.path.join(PACKS_DIR, folder_name))
    if data is None:
        return None
    if "skills" in data:
        err(label, "remove 'skills' from plugin.json — the default skills/ folder is scanned")
    deps = dependency_names(data)
    if label != CORE_PACK and CORE_PACK not in deps:
        err(label, f"plugin.json must list '{CORE_PACK}' in 'dependencies' — its skills hand "
            "off to the orchestrator and the law/method skills there")
    for dep in deps:
        if dep not in packs:
            err(label, f"depends on '{dep}', which is not a pack")
    return data.get("version")


def validate_bundle(label: str, entry: dict):
    """A bundle = its own folder holding only .claude-plugin/plugin.json with a
    `dependencies` list. Returns its version (or None)."""
    folder = os.path.join(ROOT, entry["source"])
    # A skills/ folder here would load skills under the bundle's name as well.
    if os.path.isdir(os.path.join(folder, "skills")) or entry.get("skills"):
        err(label, "a bundle must not carry skills — it only lists packs in 'dependencies'")
    data = validate_plugin_folder(label, entry, folder)
    if data is None:
        return None
    deps = dependency_names(data)
    if not deps:
        err(label, "plugin.json has no 'dependencies' — a bundle exists to install packs")
    for dep in deps:
        if dep not in packs:
            err(label, f"depends on '{dep}', which is not a pack")
    bundles[label] = deps
    return data.get("version")


def validate_marketplace() -> None:
    data = load_json(MARKETPLACE, "marketplace.json")
    if data is None:
        return
    if not data.get("name"):
        err("marketplace.json", "missing top-level 'name'")

    # owner must be an object with a 'name' — a bare string is the old form and
    # fails current schema validation in `/plugin marketplace add`.
    owner = data.get("owner")
    if owner is None:
        warn("marketplace.json", "no 'owner' set")
    elif not isinstance(owner, dict):
        err("marketplace.json", "'owner' must be an object with a 'name' field, "
            f"not a bare {type(owner).__name__} (e.g. {{\"name\": \"you\"}})")
    elif not owner.get("name"):
        err("marketplace.json", "'owner' object is missing 'name'")

    plugins = data.get("plugins", [])
    if not plugins:
        err("marketplace.json", "no plugins declared")

    seen: set[str] = set()
    versions: set[str] = set()
    bundle_folders: set[str] = set()
    for i, plugin in enumerate(plugins):
        label = plugin.get("name") or f"#{i}"
        if not plugin.get("name"):
            err("marketplace.json", f"plugin #{i} is missing 'name'")
        elif label in seen:
            err("marketplace.json", f"plugin name '{label}' is declared more than once")
        seen.add(label)
        # Without a displayName the plugin manager shows the raw kebab-case name.
        if not plugin.get("displayName"):
            warn("marketplace.json", f"plugin '{label}' has no 'displayName'")
        # `source` is a required field on every plugin entry — omitting it makes
        # `/plugin marketplace add` fail with "Failed to add marketplace". Relative
        # paths must start with "./" or the installer cannot resolve them.
        source = plugin.get("source")
        if not isinstance(source, str) or not source:
            err("marketplace.json", f"plugin '{label}' is missing required 'source'")
        elif source.startswith(PACK_PREFIX):
            version = validate_pack(label, plugin)
            if version:
                versions.add(version)
        elif source.startswith(BUNDLE_PREFIX):
            bundle_folders.add(source[len(BUNDLE_PREFIX):].rstrip("/"))
            version = validate_bundle(label, plugin)
            if version:
                versions.add(version)
        else:
            # "./" would make the plugin the whole repo: it would carry every pack's
            # skills on disk, and a plugin manager would count them all.
            err("marketplace.json", f"plugin '{label}' source '{source}' must be "
                f"'{PACK_PREFIX}<name>' or '{BUNDLE_PREFIX}<name>'")

    for pack in packs:
        if pack not in seen:
            err("marketplace.json", f"packs/{pack}/ exists but has no marketplace entry")
    for folder in subdirs(BUNDLES_DIR):
        if folder not in bundle_folders:
            err("marketplace.json", f"bundles/{folder}/ exists but has no marketplace entry")
    if os.path.isfile(ROOT_PLUGIN_MANIFEST):
        err("plugin.json", "a plugin.json at the repo root is not used — each pack and bundle "
            "has its own")

    # One release number for the whole collection. If a pack changes but its version
    # doesn't, users keep the stale cached copy with no warning.
    if len(versions) > 1:
        err("marketplace.json", f"packs/bundles carry different versions {sorted(versions)} — "
            "run scripts/bump-version.py to set them all together")


# ------------------------------------------------------------- orchestrator & README

def validate_orchestrator() -> None:
    """hse-advisor is the router, and since descriptions are kept short it carries the
    trigger vocabulary for every specialist. Two ways it silently drifts:
    a specialist with no routing row, and a pack table that disagrees with the
    folders (it tells users which pack to install)."""
    if ORCHESTRATOR not in skills:
        err(ORCHESTRATOR, "the orchestrator skill is missing")
        return
    with open(os.path.join(skills[ORCHESTRATOR][1], "SKILL.md"), encoding="utf-8") as fh:
        text = fh.read()
    for name in sorted(set(skills) - {ORCHESTRATOR}):
        if f"**{name}**" not in text:
            err(ORCHESTRATOR, f"routing map has no row for **{name}** — it can't be routed to")
    for pack, names in packs.items():
        row = next((ln for ln in text.split("\n") if ln.startswith(f"| `{pack}` |")), None)
        if row is None:
            err(ORCHESTRATOR, f"pack table has no row for `{pack}`")
            continue
        cells = {c.strip() for c in row.split("|")[2].split(",")}
        for name in names:
            short = name[:-len("-specialist")] if name.endswith("-specialist") else name
            if name not in cells and short not in cells:
                err(ORCHESTRATOR, f"pack table row `{pack}` is missing '{short}' "
                    f"(it is in packs/{pack}/skills/)")
        for cell in cells:
            full = cell if cell in skills else f"{cell}-specialist"
            if full in skills and skills[full][0] != pack:
                err(ORCHESTRATOR, f"pack table row `{pack}` lists '{cell}', which is in "
                    f"{skills[full][0]}")


def validate_readme() -> None:
    """The README roster and install table are what users read before installing."""
    path = os.path.join(ROOT, "README.md")
    if not os.path.isfile(path):
        return
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    for name in sorted(skills):
        if f"**{name}**" not in text:
            err("README.md", f"skills roster has no row for **{name}**")
        elif f"| **{name}** | `{skills[name][0]}` |" not in text:
            err("README.md", f"roster row for **{name}** should show pack `{skills[name][0]}`")
    for name in list(packs) + list(bundles):
        if f"`{name}`" not in text:
            err("README.md", f"install section does not mention `{name}`")


def check_listing_budget() -> list[str]:
    """Warn on oversize descriptions/packs; return the per-pack size report."""
    for name, n in sorted(desc_lengths.items()):
        if DESC_TARGET_CHARS < n <= DESC_MAX_CHARS:
            warn(name, f"description is {n} chars — keep it under {DESC_TARGET_CHARS}; put the "
                 f"trigger keywords in the {ORCHESTRATOR} routing map instead")
    report = []
    for pack, names in packs.items():
        size = sum(desc_lengths.get(s, 0) for s in names)
        report.append(f"  {pack:32s} {len(names):3d} skills  {size:6,} chars")
        if size > PACK_BUDGET_CHARS:
            warn(pack, f"descriptions total {size:,} chars — over {PACK_BUDGET_CHARS:,} "
                 f"(half Claude Code's ~{LISTING_BUDGET_CHARS:,}-char listing budget, which is "
                 "shared with every other skill the user has). Shorten, or split the pack")
    if bundles:
        report.append("  -- bundles (what one install loads) --")
    for bundle, deps in bundles.items():
        names = [s for d in deps for s in packs.get(d, [])]
        size = sum(desc_lengths.get(s, 0) for s in names)
        report.append(f"  {bundle:32s} {len(names):3d} skills  {size:6,} chars"
                      f"  = {size / LISTING_BUDGET_CHARS:.1f}x the ~{LISTING_BUDGET_CHARS:,}-char budget")
    return report


def main() -> int:
    if not os.path.isdir(PACKS_DIR):
        print(f"No packs/ directory at {PACKS_DIR}")
        return 1
    discover_skills()
    for name in sorted(skills):
        validate_skill(name)
    validate_marketplace()
    validate_orchestrator()
    validate_readme()
    budget_report = check_listing_budget()

    print(f"Validated {len(skills)} skills in {len(packs)} pack(s), {len(bundles)} bundle(s).\n")
    print("Skill-listing cost (description chars loaded into context every turn):")
    print("\n".join(budget_report) + "\n")
    for w in warnings:
        print(w)
    if warnings:
        print()
    if errors:
        for e in errors:
            print(e)
        print(f"\n{len(errors)} error(s) — FAILED")
        return 1
    print("All checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
