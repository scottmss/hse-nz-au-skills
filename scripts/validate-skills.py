#!/usr/bin/env python3
"""validate-skills.py — lint every SKILL.md before commit.

Repo-level linter for the hse-nz-au-skills collection. Checks each skill's
frontmatter and body, that internal cross-reference paths resolve, that no
stray "(planned)" tags remain, and that .claude-plugin/marketplace.json is
consistent with the skills on disk.

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
SKILLS_DIR = os.path.join(ROOT, "skills")
MARKETPLACE = os.path.join(ROOT, ".claude-plugin", "marketplace.json")
PLUGIN_MANIFEST = os.path.join(ROOT, ".claude-plugin", "plugin.json")
# A bundle is a plugin with no skills of its own — only `dependencies` on packs — so
# one install pulls in a curated set. Each lives in its own folder under bundles/.
BUNDLE_PREFIX = "./bundles/"

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
ORCHESTRATOR = "hse-advisor"

NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
# A backtick code-span whose entire content looks like an internal relative path.
PATH_RE = re.compile(r"^(?:\.\.?/|references/|scripts/)[\w./-]+$")
BACKTICK_RE = re.compile(r"`([^`]+)`")

errors: list[str] = []
warnings: list[str] = []
desc_lengths: dict[str, int] = {}
bundles: dict[str, list[str]] = {}   # bundle name -> pack names it installs


def err(skill: str, msg: str) -> None:
    errors.append(f"  [FAIL] {skill}: {msg}")


def warn(skill: str, msg: str) -> None:
    warnings.append(f"  [warn] {skill}: {msg}")


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
    """Every backtick path-span in this file must resolve on disk."""
    base = os.path.dirname(md_path)
    with open(md_path, encoding="utf-8") as fh:
        content = fh.read()
    for span in BACKTICK_RE.findall(content):
        s = span.strip()
        if "://" in s or " " in s or not PATH_RE.match(s):
            continue
        target = os.path.normpath(os.path.join(base, s.rstrip("/")))
        if not os.path.exists(target):
            rel = os.path.relpath(md_path, ROOT)
            err(skill, f"unresolved reference `{s}` in {rel}")


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
    skill_dir = os.path.join(SKILLS_DIR, name)
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
            desc = frontmatter_value(fm, "description") or ""
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


def validate_bundle(label: str, entry: dict):
    """A bundle = its own folder holding only .claude-plugin/plugin.json with a
    `dependencies` list. Returns its version (or None)."""
    folder = os.path.join(ROOT, entry["source"])
    manifest = os.path.join(folder, ".claude-plugin", "plugin.json")
    # If the folder had a skills/ dir — or the entry pointed at the repo root — the
    # default scan would load skills under the bundle's name as well as the pack's.
    if os.path.isdir(os.path.join(folder, "skills")) or entry.get("skills"):
        err(label, "a bundle must not carry skills — it only lists packs in 'dependencies'")
    # plugin.json's version silently wins over the entry's, so keep it in one place.
    if entry.get("version"):
        err(label, "set a bundle's 'version' in its plugin.json only, not on the marketplace entry")
    if not os.path.isfile(manifest):
        err(label, f"missing {os.path.relpath(manifest, ROOT)}")
        return None
    try:
        with open(manifest, encoding="utf-8") as fh:
            data = json.load(fh)
    except json.JSONDecodeError as e:
        err(label, f"plugin.json is invalid JSON: {e}")
        return None
    if data.get("name") != label:
        err(label, f"plugin.json name '{data.get('name')}' != marketplace entry name '{label}'")
    deps = [d if isinstance(d, str) else d.get("name") for d in data.get("dependencies", [])]
    if not deps:
        err(label, "plugin.json has no 'dependencies' — a bundle exists to install packs")
    bundles[label] = deps
    # The description sits in both places (the official validator wants it in
    # plugin.json; marketplace browsers read the entry) — keep them identical.
    if data.get("description") != entry.get("description"):
        err(label, "plugin.json 'description' differs from its marketplace.json entry")
    if not data.get("version"):
        err(label, "plugin.json has no 'version'")
    return data.get("version")


def validate_marketplace(disk_skills: set[str]) -> dict[str, list[str]]:
    """Validate marketplace.json. Returns {pack name: [skill names]}."""
    packs: dict[str, list[str]] = {}
    if not os.path.isfile(MARKETPLACE):
        err("marketplace.json", "file not found")
        return packs
    try:
        with open(MARKETPLACE, encoding="utf-8") as fh:
            data = json.load(fh)
    except json.JSONDecodeError as e:
        err("marketplace.json", f"invalid JSON: {e}")
        return packs
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

    listed_paths: list[str] = []
    by_source: dict[str, list[str]] = {}
    versions: set[str] = set()
    for i, plugin in enumerate(plugins):
        label = plugin.get("name") or f"#{i}"
        if not plugin.get("name"):
            err("marketplace.json", f"plugin #{i} is missing 'name'")
        elif label in packs:
            err("marketplace.json", f"plugin name '{label}' is declared more than once")
        # `source` is a required field on every plugin entry — omitting it makes
        # `/plugin marketplace add` fail with "Failed to add marketplace".
        if not plugin.get("source"):
            err("marketplace.json", f"plugin '{label}' is missing required 'source' "
                "(e.g. \"./\" when the plugin lives at the marketplace root)")
        elif isinstance(plugin["source"], str):
            by_source.setdefault(plugin["source"].rstrip("/") or ".", []).append(label)
        # Without a displayName the /plugin UI shows the raw kebab-case name.
        if not plugin.get("displayName"):
            warn("marketplace.json", f"plugin '{label}' has no 'displayName'")
        if str(plugin.get("source", "")).startswith(BUNDLE_PREFIX):
            version = validate_bundle(label, plugin)
            if version:
                versions.add(version)
            continue
        if not plugin.get("skills"):
            err("marketplace.json", f"plugin '{label}' lists no skills")
        if not plugin.get("version"):
            err("marketplace.json", f"plugin '{label}' has no 'version' — installs are pinned "
                "by version, so users would never receive an update")
        else:
            versions.add(plugin["version"])
        packs[label] = [s[len("./skills/"):] for s in plugin.get("skills", [])
                        if s.startswith("./skills/")]
        listed_paths.extend(plugin.get("skills", []))

    # The packs are several plugins carved out of ONE folder (the flat skills/ tree
    # stays whole so the ../<skill>/ cross-references resolve whichever packs a user
    # installs). With a marketplace-root source, an entry's listed skill paths are the
    # complete set for that pack. There is no plugin.json, so each entry must be
    # "strict": false — the marketplace entry is then the pack's entire definition.
    # (Same layout as github.com/anthropics/skills.)
    for source, labels in by_source.items():
        if len(labels) < 2:
            continue
        for plugin in plugins:
            if plugin.get("name") in labels and plugin.get("strict") is not False:
                err("marketplace.json", f"plugin '{plugin.get('name')}' shares source "
                    f"'{source}' with {len(labels) - 1} other pack(s) and has no plugin.json, "
                    "so it must set \"strict\": false (the entry is its whole definition)")
        # A plugin.json at the shared root would stamp its name and version on every
        # pack (plugin.json's version silently wins over the marketplace entry's).
        if os.path.isfile(PLUGIN_MANIFEST):
            err("plugin.json", f"must not exist while {len(labels)} packs share source "
                f"'{source}' — put name/version/metadata in each marketplace.json entry")

    # One release number for the whole collection. If a pack changes but its version
    # doesn't, users keep the stale cached copy with no warning.
    if len(versions) > 1:
        err("marketplace.json", f"packs/bundles carry different versions {sorted(versions)} — "
            "run scripts/bump-version.py to set them all together")

    for bundle, deps in bundles.items():
        for dep in deps:
            if dep not in packs:
                err(bundle, f"depends on '{dep}', which is not a pack in marketplace.json")

    # Component paths in a plugin manifest are relative paths and must start with
    # "./" — without it the installer can't resolve them and the plugin fails to
    # install. The skills live under "./skills/<name>".
    listed = set()
    seen_paths: set[str] = set()
    for p in listed_paths:
        if p in seen_paths:
            err("marketplace.json", f"skill path '{p}' is listed more than once "
                "(a skill belongs to exactly one pack)")
        seen_paths.add(p)
        if not p.startswith("./skills/"):
            err("marketplace.json", f"skill path '{p}' must start with './skills/' "
                "(relative manifest paths require the './' prefix)")
            continue
        listed.add(p[len("./skills/"):])
        if not os.path.isdir(os.path.join(ROOT, p)):
            err("marketplace.json", f"listed skill '{p}' has no directory on disk")
    for missing in sorted(disk_skills - listed):
        err("marketplace.json", f"skill '{missing}' exists on disk but is not in any pack")
    return packs


def validate_plugin_manifest() -> None:
    """Optional plugin.json (single-plugin layouts only): must be valid JSON, have a
    name that matches the marketplace entry, and agree with it on version."""
    if not os.path.isfile(PLUGIN_MANIFEST):
        return
    try:
        with open(PLUGIN_MANIFEST, encoding="utf-8") as fh:
            data = json.load(fh)
    except json.JSONDecodeError as e:
        err("plugin.json", f"invalid JSON: {e}")
        return
    if not data.get("name"):
        err("plugin.json", "missing 'name'")
    if os.path.isfile(MARKETPLACE):
        try:
            with open(MARKETPLACE, encoding="utf-8") as fh:
                entries = {p.get("name"): p for p in json.load(fh).get("plugins", [])}
        except json.JSONDecodeError:
            entries = {}
        if data.get("name") and entries and data["name"] not in entries:
            err("plugin.json", f"name '{data['name']}' is not a plugin in marketplace.json "
                f"{sorted(n for n in entries if n)}")
        entry = entries.get(data.get("name")) or {}
        # When both set a version, Claude Code silently uses plugin.json's. If they
        # drift, users stay pinned to the stale one and never receive the release.
        if entry.get("version") and data.get("version") and entry["version"] != data["version"]:
            err("plugin.json", f"version '{data['version']}' != marketplace.json entry "
                f"version '{entry['version']}' — bump both together")


def validate_orchestrator(disk_skills: set[str], packs: dict[str, list[str]]) -> None:
    """hse-advisor is the router, and since descriptions are kept short it carries the
    trigger vocabulary for every specialist. Two ways it silently drifts:
    a specialist with no routing row, and a pack table that disagrees with
    marketplace.json (it tells users which pack to install)."""
    path = os.path.join(SKILLS_DIR, ORCHESTRATOR, "SKILL.md")
    if not os.path.isfile(path):
        return
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    for name in sorted(disk_skills - {ORCHESTRATOR}):
        if f"**{name}**" not in text:
            err(ORCHESTRATOR, f"routing map has no row for **{name}** — it can't be routed to")
    for pack, skills in packs.items():
        row = next((ln for ln in text.split("\n") if ln.startswith(f"| `{pack}` |")), None)
        if row is None:
            err(ORCHESTRATOR, f"pack table has no row for `{pack}`")
            continue
        cells = {c.strip() for c in row.split("|")[2].split(",")}
        for name in skills:
            short = name[:-len("-specialist")] if name.endswith("-specialist") else name
            if name not in cells and short not in cells:
                err(ORCHESTRATOR, f"pack table row `{pack}` is missing '{short}' "
                    "(marketplace.json lists it in that pack)")


def validate_readme(disk_skills: set[str], packs: dict[str, list[str]]) -> None:
    """The README roster and install table are what users read before installing."""
    path = os.path.join(ROOT, "README.md")
    if not os.path.isfile(path):
        return
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    for name in sorted(disk_skills):
        if f"**{name}**" not in text:
            err("README.md", f"skills roster has no row for **{name}**")
    for name in list(packs) + list(bundles):
        if f"`{name}`" not in text:
            err("README.md", f"install section does not mention `{name}`")


def check_listing_budget(packs: dict[str, list[str]]) -> list[str]:
    """Warn on oversize descriptions/packs; return the per-pack size report."""
    for name, n in sorted(desc_lengths.items()):
        if DESC_TARGET_CHARS < n <= DESC_MAX_CHARS:
            warn(name, f"description is {n} chars — keep it under {DESC_TARGET_CHARS}; put the "
                 f"trigger keywords in the {ORCHESTRATOR} routing map instead")
    report = []
    for pack, skills in packs.items():
        size = sum(desc_lengths.get(s, 0) for s in skills)
        report.append(f"  {pack:32s} {len(skills):3d} skills  {size:6,} chars")
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
    if not os.path.isdir(SKILLS_DIR):
        print(f"No skills/ directory at {SKILLS_DIR}")
        return 1
    disk_skills = {
        d for d in os.listdir(SKILLS_DIR)
        if os.path.isdir(os.path.join(SKILLS_DIR, d)) and not d.startswith(".")
    }
    for name in sorted(disk_skills):
        validate_skill(name)
    packs = validate_marketplace(disk_skills)
    validate_plugin_manifest()
    validate_orchestrator(disk_skills, packs)
    validate_readme(disk_skills, packs)
    budget_report = check_listing_budget(packs)

    print(f"Validated {len(disk_skills)} skills in {len(packs)} pack(s).\n")
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
