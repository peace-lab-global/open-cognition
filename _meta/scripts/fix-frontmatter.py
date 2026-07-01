#!/usr/bin/env python3
"""
fix-frontmatter.py — repair YAML frontmatter that lint.py cannot parse.

Handles three mechanical failure patterns (no semantic judgement needed);
files with NO frontmatter at all are reported for manual authoring, since
synthesizing id/domain/school/era/tags from prose is not safe to automate.

Patterns auto-fixed:
  1. MD_IN_FM  — a list field (related_concepts / cross_refs / ...) holds
                 markdown-link items like `  - [foo.md](foo.md)`. Converted
                 to a plain list of bare paths.
  2. SOURCES_INLINE — `sources: [*Title*, 1999, "Other", 2001]` flow-sequence
                 with italics / nested quotes. Converted to a block sequence
                 of double-quoted strings.
  3. TITLE_COLON — `title: Foo: Bar` unquoted colon. Title value quoted.

Usage:
    python3 scripts/fix-frontmatter.py            # dry-run
    python3 scripts/fix-frontmatter.py --apply    # write changes
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
DOMAINS_DIR = REPO_ROOT / "domains"


def find_failing_lines(fm_text: str) -> list[tuple[int, str, str]]:
    """Return [(lineno, line, category)] for lines whose presence breaks YAML."""
    lines = fm_text.split("\n")
    failing = []
    for i, line in enumerate(lines):
        probe = "\n".join(lines[: i + 1])
        try:
            yaml.safe_load(probe)
        except yaml.YAMLError:
            cat = classify_failure(line, lines)
            failing.append((i, line, cat))
    return failing


def classify_failure(line: str, all_lines: list[str]) -> str:
    stripped = line.strip()
    if stripped.startswith("- [") and "](" in stripped:
        return "MD_IN_FM"
    if "sources:" in line and ("[" in line and "]" in line):
        return "SOURCES_INLINE"
    # title with unquoted colon
    if re.match(r"^title:\s*.+:\s", line) and not line.strip().endswith('"'):
        return "TITLE_COLON"
    # continuation of a sources list with italics/special chars
    if stripped.startswith("- ") and ("*" in stripped or '"' in stripped):
        return "MD_IN_FM"
    return "OTHER"


def fix_md_in_fm(fm_text: str) -> str:
    """Convert `  - [text](path)` list items to bare `  - path`."""
    out = []
    for line in fm_text.split("\n"):
        m = re.match(r"^(\s*-\s+)\[([^\]]*)\]\(([^)]+)\)\s*$", line)
        if m:
            indent, _text, path = m.groups()
            out.append(f"{indent}{path}")
        else:
            out.append(line)
    return "\n".join(out)


def fix_sources_inline(fm_text: str) -> str:
    """Convert `sources: [*X*, 1999, "Y", 2001]` to a block sequence."""
    lines = fm_text.split("\n")
    out = []
    i = 0
    while i < len(lines):
        line = lines[i]
        m = re.match(r"^(\s*)sources:\s*\[(.*)\]\s*$", line)
        if m:
            indent, body = m.groups()
            # split on commas NOT inside quotes; simple approach: split top-level
            items = split_flow_items(body)
            out.append(f"{indent}sources:")
            for it in items:
                it = it.strip()
                if it.startswith('"') and it.endswith('"'):
                    val = it[1:-1]
                elif it.startswith("*") and it.endswith("*") and it.count("*") >= 2:
                    val = it.strip("*").strip()
                else:
                    val = it.strip("*").strip()
                # escape any double quotes inside, then quote
                val = val.replace('"', '\\"')
                out.append(f'{indent}  - "{val}"')
        else:
            out.append(line)
        i += 1
    return "\n".join(out)


def split_flow_items(body: str) -> list[str]:
    """Split a YAML flow-seq body on commas that are outside quotes."""
    items, cur, in_squote, in_dquote = [], "", False, False
    for ch in body:
        if ch == '"' and not in_squote:
            in_dquote = not in_dquote
            cur += ch
        elif ch == "'" and not in_dquote:
            in_squote = not in_squote
            cur += ch
        elif ch == "," and not in_squote and not in_dquote:
            items.append(cur)
            cur = ""
        else:
            cur += ch
    if cur.strip():
        items.append(cur)
    return items


def fix_title_colon(fm_text: str) -> str:
    """Quote a title value that contains a colon and isn't already quoted."""
    out = []
    for line in fm_text.split("\n"):
        m = re.match(r"^title:\s*(.+)$", line)
        if m and ":" in m.group(1):
            val = m.group(1).strip()
            if not (val.startswith('"') and val.endswith('"')):
                val = val.replace('"', '\\"')
                line = f'title: "{val}"'
        out.append(line)
    return "\n".join(out)


def process_file(path: Path) -> tuple[str, str | None]:
    """Return (category, new_text_or_None). new_text None => no change/manual."""
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return "NO_FRONTMATTER", None
    try:
        end = text.index("---", 3)
    except ValueError:
        return "NO_CLOSING", None
    fm_text = text[3:end]
    body = text[end:]

    failures = find_failing_lines(fm_text)
    if not failures:
        return "PARSES_OK", None

    cats = {c for _, _, c in failures}
    new_fm = fm_text
    if "MD_IN_FM" in cats:
        new_fm = fix_md_in_fm(new_fm)
    if "SOURCES_INLINE" in cats:
        new_fm = fix_sources_inline(new_fm)
    if "TITLE_COLON" in cats:
        new_fm = fix_title_colon(new_fm)

    # verify the result parses
    try:
        yaml.safe_load(new_fm)
    except yaml.YAMLError:
        return "UNFIXABLE", None

    return "FIXED", "---" + new_fm + body


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    fixed, manual, unfixable, unchanged = [], [], [], 0
    for path in sorted(DOMAINS_DIR.rglob("*.md")):
        cat, new_text = process_file(path)
        rel = path.relative_to(REPO_ROOT)
        if cat == "FIXED":
            fixed.append(rel)
            if args.apply:
                path.write_text(new_text, encoding="utf-8")
        elif cat == "NO_FRONTMATTER":
            manual.append(rel)
        elif cat == "UNFIXABLE":
            unfixable.append(rel)
        elif cat == "PARSES_OK":
            unchanged += 1

    print(f"Fixed (mechanical): {len(fixed)}")
    for r in fixed:
        print(f"  ✓ {r}")
    print(f"\nNeeds manual frontmatter (no/invalid block): {len(manual)}")
    for r in manual:
        print(f"  ✗ {r}")
    print(f"\nUnfixable (complex): {len(unfixable)}")
    for r in unfixable:
        print(f"  ? {r}")
    print(f"\nAlready-valid: {unchanged}")
    print(f"Mode: {'APPLIED' if args.apply else 'DRY-RUN'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
