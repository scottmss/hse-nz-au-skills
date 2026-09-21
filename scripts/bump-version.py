#!/usr/bin/env python3
"""bump-version.py — set one release version across every pack and bundle.

Installs are pinned by version: a pack or bundle whose version doesn't change never
updates for people who already have it. So the whole collection carries ONE version,
bumped together. It lives in two kinds of place:

- each pack's entry in .claude-plugin/marketplace.json
- each bundle's bundles/<name>/.claude-plugin/plugin.json

Pure standard library. Edits text in place so the manifests keep their formatting.

    python3 scripts/bump-version.py 2.1.0
    python3 scripts/bump-version.py            # just print the current version(s)

Exit codes: 0 = done, 1 = bad input or nothing to change.
"""
from __future__ import annotations

import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MARKETPLACE = os.path.join(ROOT, ".claude-plugin", "marketplace.json")
BUNDLE_MANIFESTS = os.path.join(ROOT, "bundles", "*", ".claude-plugin", "plugin.json")

VERSION_RE = re.compile(r'("version"\s*:\s*")([^"]*)(")')
SEMVER_RE = re.compile(r"^\d+\.\d+\.\d+$")


def targets() -> list[str]:
    return [MARKETPLACE] + sorted(glob.glob(BUNDLE_MANIFESTS))


def main() -> int:
    files = [f for f in targets() if os.path.isfile(f)]
    current: set[str] = set()
    for path in files:
        with open(path, encoding="utf-8") as fh:
            current.update(m.group(2) for m in VERSION_RE.finditer(fh.read()))

    if len(sys.argv) < 2:
        print(f"Current version(s): {', '.join(sorted(current)) or 'none'}")
        return 0

    new = sys.argv[1].lstrip("v")
    if not SEMVER_RE.match(new):
        print(f"'{sys.argv[1]}' is not a MAJOR.MINOR.PATCH version (e.g. 2.1.0)")
        return 1

    changed = 0
    for path in files:
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
        updated, n = VERSION_RE.subn(rf"\g<1>{new}\g<3>", text)
        if n and updated != text:
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(updated)
        changed += n
        print(f"  {os.path.relpath(path, ROOT)}: {n} version field(s)")

    if not changed:
        print("No version fields found — nothing changed.")
        return 1
    print(f"\n{', '.join(sorted(current))} -> {new}  ({changed} fields). "
          "Now run: python3 scripts/validate-skills.py")
    return 0


if __name__ == "__main__":
    sys.exit(main())
