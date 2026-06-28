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

NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
# A backtick code-span whose entire content looks like an internal relative path.
PATH_RE = re.compile(r"^(?:\.\.?/|references/|scripts/)[\w./-]+$")
BACKTICK_RE = re.compile(r"`([^`]+)`")

errors: list[str] = []
warnings: list[str] = []


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
                warn(name, "description looks very short — make it trigger-rich")
        for issue in frontmatter_yaml_issues(fm):
            err(name, issue)

    low = body.lower()
    if "disclaimer" not in low and "not legal advice" not in low:
        err(name, "no disclaimer / 'not legal advice' statement in body")

    for md in md_files(skill_dir):
        check_cross_refs(name, md)
        check_planned_tags(name, md)


def validate_marketplace(disk_skills: set[str]) -> None:
    if not os.path.isfile(MARKETPLACE):
        err("marketplace.json", "file not found")
        return
    try:
        with open(MARKETPLACE, encoding="utf-8") as fh:
            data = json.load(fh)
    except json.JSONDecodeError as e:
        err("marketplace.json", f"invalid JSON: {e}")
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

    listed_paths: list[str] = []
    for i, plugin in enumerate(plugins):
        if not plugin.get("name"):
            err("marketplace.json", f"plugin #{i} is missing 'name'")
        listed_paths.extend(plugin.get("skills", []))

    listed = set()
    seen_paths: set[str] = set()
    for p in listed_paths:
        if p in seen_paths:
            err("marketplace.json", f"skill path '{p}' is listed more than once")
        seen_paths.add(p)
        if not p.startswith("skills/"):
            err("marketplace.json", f"skill path '{p}' does not start with 'skills/'")
            continue
        listed.add(p[len("skills/"):])
        if not os.path.isdir(os.path.join(ROOT, p)):
            err("marketplace.json", f"listed skill '{p}' has no directory on disk")
    for missing in sorted(disk_skills - listed):
        err("marketplace.json", f"skill '{missing}' exists on disk but is not listed")


def validate_plugin_manifest() -> None:
    """Optional plugin.json: must be valid JSON, have a name, and that name must
    match a plugin declared in marketplace.json."""
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
    if not data.get("version"):
        warn("plugin.json", "no 'version' set")
    if os.path.isfile(MARKETPLACE):
        try:
            with open(MARKETPLACE, encoding="utf-8") as fh:
                names = {p.get("name") for p in json.load(fh).get("plugins", [])}
        except json.JSONDecodeError:
            names = set()
        if data.get("name") and names and data["name"] not in names:
            err("plugin.json", f"name '{data['name']}' is not a plugin in marketplace.json "
                f"{sorted(n for n in names if n)}")


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
    validate_marketplace(disk_skills)
    validate_plugin_manifest()

    print(f"Validated {len(disk_skills)} skills.\n")
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
