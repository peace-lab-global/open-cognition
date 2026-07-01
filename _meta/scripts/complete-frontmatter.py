#!/usr/bin/env python3
"""
complete-frontmatter.py — fill in missing REQUIRED frontmatter fields.

For concept/text entries that parse but lack one of the required fields, derive
a sensible value rather than leaving the entry broken. Derivation rules are
conservative and documented per-field:

  id     — <domain>.<type-path>.<stem>  (deterministic from path)
  type   — from classify() (concept / text / thinker / ...)
  domain — from path's top-level domain dir
  school — 'general-<domain>' for cross-school concepts (the honest value when
           a concept is not tied to one school)
  era    — 'universal' for trans-historical concepts; 'ancient' for sutras

Only adds fields that are ABSENT. Never overwrites an existing value.
Dry-run by default; --apply to write.

Usage:
    python3 scripts/complete-frontmatter.py
    python3 scripts/complete-frontmatter.py --apply
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
DOMAINS_DIR = REPO_ROOT / "domains"


def extract_frontmatter(text: str) -> tuple[str, str, str]:
    """Return (fm_text_incl_delimiters, body, fm_dict). fm_text excludes ---."""
    if not text.startswith("---"):
        return "", text, {}
    try:
        end = text.index("---", 3)
    except ValueError:
        return "", text, {}
    fm_text = text[3:end]
    body = text[end:]
    try:
        fm = yaml.safe_load(fm_text) or {}
    except yaml.YAMLError:
        return "", text, {}
    return fm_text, body, fm


def classify(rel: str, name: str) -> str | None:
    if "/reports/" in rel:
        return None
    if "/skills/" in rel and name == "SKILL.md":
        return "skill"
    if "/schools/" in rel:
        return "thinker"
    if "/concepts/" in rel:
        return "concept"
    if "/masters/" in rel:
        return "thinker"
    if "/sutras/" in rel:
        return "text"
    if "/core-concepts/" in rel:
        return "concept"
    if "/traditions/" in rel:
        return "tradition"
    return None


def derive(entry_type: str, rel: str, stem: str, domain: str) -> dict:
    """Return the set of derivable defaults for this entry."""
    defaults = {}
    defaults["id"] = f"{domain}.{rel.replace('/', '.').removesuffix('.md')}"
    defaults["type"] = entry_type
    defaults["domain"] = domain
    if entry_type == "concept":
        defaults["school"] = f"general-{domain}"
        defaults["era"] = "universal"
    elif entry_type == "text":
        defaults["school"] = f"{domain}-canon"
        defaults["era"] = "ancient"
    return defaults


REQUIRED = {
    "thinker": ["id", "type", "domain", "school", "era", "tags"],
    "concept": ["id", "title", "type", "domain", "school", "era", "tags"],
    "skill":   ["name", "description", "domain", "tags"],
    "text":    ["id", "title", "type", "domain"],
    "tradition": ["id", "title", "type", "domain"],
}


def add_field(fm_lines: list[str], key: str, value) -> list[str]:
    """Insert `key: value` as the 2nd line (right after opening), preserving order.
    Uses YAML-safe scalar formatting."""
    if isinstance(value, str):
        line = f'{key}: "{value}"' if needs_quote(value) else f"{key}: {value}"
    else:
        line = f"{key}: {yaml.safe_dump(value, allow_unicode=True, default_flow_style=True).strip()}"
    # insert after the first content line (id/type usually first)
    out = list(fm_lines)
    out.insert(0, line)
    return out


def needs_quote(v: str) -> bool:
    return any(c in v for c in [":", "#", "*", "?", "|", ">", "@", "`"]) or v.strip() != v


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    completed, already_ok = [], 0
    for path in sorted(DOMAINS_DIR.rglob("*.md")):
        if path.name in {"README.md", "INDEX.md", "QUICKSTART.md", "SKILLS.md", "AGENT.md"}:
            continue
        rel = path.relative_to(REPO_ROOT).as_posix()
        etype = classify(rel, path.name)
        if etype is None:
            continue
        text = path.read_text(encoding="utf-8")
        fm_text, body, fm = extract_frontmatter(text)
        if not fm:
            continue  # E001 territory, not this script's job
        domain = rel.split("/")[1] if rel.startswith("domains/") else ""
        required = REQUIRED.get(etype, [])
        missing = [f for f in required if f not in fm or fm.get(f) in (None, "", [])]
        if not missing:
            already_ok += 1
            continue
        defaults = derive(etype, rel, path.stem, domain)
        # only fill those we can derive
        fillable = [m for m in missing if m in defaults]
        if not fillable:
            continue
        new_fm = dict(fm)
        for m in fillable:
            new_fm[m] = defaults[m]
        # rebuild frontmatter block preserving key order: required first
        ordered = {}
        for k in required:
            if k in new_fm:
                ordered[k] = new_fm[k]
        for k, v in new_fm.items():
            if k not in ordered:
                ordered[k] = v
        dump = yaml.safe_dump(ordered, allow_unicode=True, default_flow_style=False, sort_keys=False).strip()
        new_text = "---\n" + dump + "\n" + body
        completed.append((path, fillable))
        if args.apply:
            path.write_text(new_text, encoding="utf-8")

    print(f"Completed: {len(completed)} files")
    for path, filled in completed:
        print(f"  + {path.relative_to(REPO_ROOT)}: added {filled}")
    print(f"\nAlready complete: {already_ok}")
    print(f"Mode: {'APPLIED' if args.apply else 'DRY-RUN (--apply to write)'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
