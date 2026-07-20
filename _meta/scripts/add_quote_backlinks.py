#!/usr/bin/env python3
"""
add_quote_backlinks.py — sync `## 相关名言` sections in thinker entries from 名言/ quotes.

Scans every 名言/*.md file for cross-refs with `relation: 思想家`, maps the target
thinker id to its canonical entry file (following `redirect:` stubs), and ensures
the thinker entry contains a back-link section listing all quotes that point to it.

Usage:
    python3 _meta/scripts/add_quote_backlinks.py [--dry-run]
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("ERROR: pyyaml required. Install with `pip install pyyaml`.")

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
MINGYAN_DIR = REPO_ROOT / "名言"

FM_RE = re.compile(r"^---\n(.*?)\n---", re.S)
SECTION_RE = re.compile(r"^## 相关名言\s*$", re.MULTILINE)
NEXT_SECTION_RE = re.compile(r"^## ", re.MULTILINE)


def extract_frontmatter(text: str) -> tuple[dict, str]:
    m = FM_RE.match(text)
    if not m:
        return {}, text
    try:
        fm = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError:
        fm = {}
    return fm, text[m.end():]


def canonical_thinker_files() -> dict[str, Path]:
    """Map thinker id -> canonical entry file, following redirect stubs.

    Preference: a non-redirect file with the id wins; if all files with the id
    are redirects, follow the redirect to its target. This handles both legacy
    root entries (e.g. 孔子.md) and expanded entries whose root .md is a stub
    pointing to a README.
    """
    by_id: dict[str, list[Path]] = {}
    redirect_map: dict[Path, Path] = {}

    for p in sorted(REPO_ROOT.rglob("*.md")):
        if "__pycache__" in p.parts or p.name == "AGENT.md":
            continue
        text = p.read_text(encoding="utf-8")
        if not text.startswith("---"):
            continue
        fm, _ = extract_frontmatter(text)
        if fm.get("type") != "thinker":
            continue
        tid = fm.get("id")
        if not tid:
            continue
        by_id.setdefault(tid, []).append(p)
        redirect = fm.get("redirect")
        if redirect:
            redirect_map[p] = (p.parent / redirect).resolve()

    canonical: dict[str, Path] = {}
    for tid, paths in by_id.items():
        # Prefer non-redirect files; if only redirects exist, resolve target.
        non_redirects = [p for p in paths if p not in redirect_map]
        if non_redirects:
            # Prefer root-level file over README.md when both are non-redirects.
            def sort_key(p: Path) -> tuple[int, int, str]:
                return (p.name == "README.md", len(p.parts), str(p))
            canonical[tid] = sorted(non_redirects, key=sort_key)[0]
        else:
            target = redirect_map.get(paths[0])
            if target and target.exists():
                canonical[tid] = target
    return canonical


def quote_backlinks() -> dict[str, list[Path]]:
    """Return mapping thinker id -> sorted list of quote file paths."""
    refs: dict[str, list[Path]] = {}
    if not MINGYAN_DIR.exists():
        return refs
    for p in sorted(MINGYAN_DIR.rglob("*.md")):
        text = p.read_text(encoding="utf-8")
        if not text.startswith("---"):
            continue
        fm, _ = extract_frontmatter(text)
        if fm.get("type") != "quote":
            continue
        for ref in fm.get("cross-refs", []) or []:
            if ref.get("relation") == "思想家":
                tid = ref.get("id")
                if tid:
                    refs.setdefault(tid, []).append(p)
    for tid in refs:
        refs[tid].sort()
    return refs


def update_thinker_file(path: Path, quotes: list[Path], dry_run: bool) -> bool:
    text = path.read_text(encoding="utf-8")
    fm, body = extract_frontmatter(text)
    # If this file itself is a redirect stub, do not edit it.
    if fm.get("redirect"):
        return False

    intro_line = "本思想在 `名言/` 模块中的独立条目：\n\n"
    # Number of parent directories between the thinker file and the repo root
    up_count = len(path.parent.relative_to(REPO_ROOT).parts)
    bullet_lines = "\n".join(
        f"- [{q.stem}]({Path(*(['..'] * up_count)) / q.relative_to(REPO_ROOT)})"
        for q in quotes
    )
    # Ensure the bullet list always ends with a newline so any following
    # content (e.g. a later H2) does not get glued to the last bullet.
    new_section = f"## 相关名言\n\n{intro_line}{bullet_lines}\n"

    m = SECTION_RE.search(text)
    if m:
        start = m.start()
        after_heading = m.end()
        # Find the next H2 heading or end of file.
        nm = NEXT_SECTION_RE.search(text, after_heading)
        end = nm.start() if nm else len(text)
        # Preserve any intro paragraph (non-bullet lines) between heading and bullets.
        old_body = text[after_heading:end]
        preserved_lines: list[str] = []
        in_bullets = False
        for line in old_body.splitlines(keepends=True):
            if line.lstrip().startswith("- ["):
                in_bullets = True
            elif in_bullets and line.strip():
                # Non-empty line after bullets starts something else; stop preserving.
                break
            if not in_bullets:
                preserved_lines.append(line)
        preserved = "".join(preserved_lines).rstrip("\n")
        if preserved and not preserved.endswith("\n"):
            preserved += "\n"
        section = f"## 相关名言\n\n{preserved}{bullet_lines}"
        new_text = text[:start] + section + text[end:]
    else:
        # Append a new section at the end, ensuring one blank line before it.
        new_text = text.rstrip("\n") + "\n\n" + new_section

    if new_text != text:
        if not dry_run:
            path.write_text(new_text, encoding="utf-8")
        return True
    return False


def main() -> int:
    parser = argparse.ArgumentParser(description="Sync quote backlinks to thinker entries.")
    parser.add_argument("--dry-run", action="store_true", help="Print changes without writing.")
    args = parser.parse_args()

    thinkers = canonical_thinker_files()
    quotes = quote_backlinks()

    changed = 0
    for tid, qpaths in sorted(quotes.items()):
        target = thinkers.get(tid)
        if not target:
            print(f"WARN: thinker id '{tid}' referenced by quotes but no canonical entry found")
            continue
        if update_thinker_file(target, qpaths, args.dry_run):
            rel = target.relative_to(REPO_ROOT)
            print(f"{'[dry-run] ' if args.dry_run else ''}updated {rel} ({len(qpaths)} quotes)")
            changed += 1

    print(f"\n{len(quotes)} thinker ids referenced; {changed} thinker file(s) updated.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
