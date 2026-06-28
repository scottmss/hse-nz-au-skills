#!/usr/bin/env python3
"""bundle.py — package the skills into distributable zips under dist/.

Produces installable artifacts for users who can't (or don't want to) add the
Claude Code marketplace from GitHub:

- dist/<skill>.zip        one zip per skill (the skill folder at the zip root,
                          e.g. critical-risk-manager/SKILL.md) — ready to upload
                          as a custom skill in Claude.ai (Settings -> Capabilities
                          -> Skills) or to drop into ~/.claude/skills/.
- dist/hse-nz-au-skills.zip  the whole collection (skills/, the marketplace
                          manifest, README and LICENSE) — a single download of
                          everything.

Pure standard library. No network. Run from anywhere:

    python3 scripts/bundle.py

Build output goes to dist/ (gitignored). Exit 0 on success.
"""
from __future__ import annotations

import os
import sys
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS_DIR = os.path.join(ROOT, "skills")
DIST = os.path.join(ROOT, "dist")

EXCLUDE_DIRS = {".git", "dist", "__pycache__", ".venv", "venv", ".github"}
EXCLUDE_FILES = {".DS_Store"}
# Files/dirs (relative to repo root) included in the combined collection zip.
COLLECTION_INCLUDE = ["skills", ".claude-plugin", "scripts", "README.md", "LICENSE"]


def _keep(name: str) -> bool:
    return name not in EXCLUDE_FILES and not name.endswith(".pyc")


def _add_tree(zf: zipfile.ZipFile, src_dir: str, arc_base: str) -> int:
    """Add a directory tree to the zip under arc_base; return file count."""
    n = 0
    for dirpath, dirs, files in os.walk(src_dir):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS and not d.startswith(".")]
        for f in sorted(files):
            if not _keep(f):
                continue
            full = os.path.join(dirpath, f)
            arc = os.path.join(arc_base, os.path.relpath(full, src_dir))
            zf.write(full, arc)
            n += 1
    return n


def main() -> int:
    if not os.path.isdir(SKILLS_DIR):
        print(f"No skills/ directory at {SKILLS_DIR}")
        return 1
    os.makedirs(DIST, exist_ok=True)
    # Clean previous artifacts.
    for f in os.listdir(DIST):
        if f.endswith(".zip"):
            os.remove(os.path.join(DIST, f))

    skills = sorted(
        d for d in os.listdir(SKILLS_DIR)
        if os.path.isdir(os.path.join(SKILLS_DIR, d)) and not d.startswith(".")
    )

    # 1) One zip per skill (skill folder at the zip root).
    print(f"Packaging {len(skills)} skills into {os.path.relpath(DIST, ROOT)}/ ...\n")
    for name in skills:
        out = os.path.join(DIST, f"{name}.zip")
        with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zf:
            count = _add_tree(zf, os.path.join(SKILLS_DIR, name), name)
        size = os.path.getsize(out)
        print(f"  {name}.zip  ({count} files, {size/1024:.0f} KB)")

    # 2) Combined collection zip (preserves repo structure).
    combined = os.path.join(DIST, "hse-nz-au-skills.zip")
    total = 0
    with zipfile.ZipFile(combined, "w", zipfile.ZIP_DEFLATED) as zf:
        for item in COLLECTION_INCLUDE:
            path = os.path.join(ROOT, item)
            if os.path.isdir(path):
                total += _add_tree(zf, path, item)
            elif os.path.isfile(path):
                zf.write(path, item)
                total += 1
    print(f"\n  hse-nz-au-skills.zip  (whole collection: {total} files, "
          f"{os.path.getsize(combined)/1024:.0f} KB)")

    print(f"\nDone. {len(skills)} per-skill zips + 1 collection zip in "
          f"{os.path.relpath(DIST, ROOT)}/.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
