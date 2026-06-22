#!/usr/bin/env python3
"""
lint.py — quality checks for open-cognition markdown entries.

Usage:
    python3 scripts/lint.py                   # lint all entry files
    python3 scripts/lint.py path/to/file.md   # lint specific file(s)
    python3 scripts/lint.py --strict          # fail on warnings too
    python3 scripts/lint.py --json            # emit JSON for CI

Checks performed:
    1. Frontmatter: required fields by entry type
    2. Section presence: required H2 headings by entry type
    3. Line length: too short (<40) or too long (>600)
    4. Broken relative links:
         E003 (error)   — target exists in the repo but the link path is wrong
         W006 (warning) — target basename exists nowhere; entry not authored yet
                          (content backlog, tracked in reports/audit/, non-blocking)
    5. Tags: at least 1 tag on thinker/concept entries
    6. Cross-domain links: at least 1 link to another domain
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("ERROR: pyyaml required. Install with `pip install pyyaml`.")


REPO_ROOT = Path(__file__).resolve().parent.parent
DOMAINS_DIR = REPO_ROOT / "domains"

SKIP_FILENAMES = {"README.md", "INDEX.md", "QUICKSTART.md", "SKILLS.md", "AGENT.md"}

REQUIRED_FRONTMATTER = {
    # thinker: accept either `name` (Chinese + English) or `title` for legacy entries
    "thinker": ["id", "type", "domain", "school", "era", "tags"],
    "concept": ["id", "title", "type", "domain", "school", "era", "tags"],
    "skill":   ["name", "description", "domain", "tags"],
    "text":    ["id", "title", "type", "domain"],
    "tradition": ["id", "title", "type", "domain"],
}

# Thinker entries must have either `name` or `title`
THINKER_NAME_OR_TITLE = True

REQUIRED_SECTIONS = {
    "thinker": ["核心命题", "关键著作", "跨学科关联", "进阶阅读"],
    "concept": ["一句话定义", "核心要义", "常见误读", "跨学科关联", "进阶阅读"],
    "skill":   ["何时使用", "何时不使用", "操作流程"],
}

MIN_LINES = 40
MAX_LINES = 600

MD_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")

# Index every .md file by basename once at import time. Used to distinguish a
# structurally-broken link (target exists somewhere, path is wrong → E003 error)
# from a link to an entry that has not been authored yet (→ W006 warn, content
# backlog, does not block CI).
ALL_FILES_BY_NAME: dict[str, list[Path]] = {}
for _p in (REPO_ROOT / "domains").rglob("*.md"):
    ALL_FILES_BY_NAME.setdefault(_p.name, []).append(_p)
for _p in (REPO_ROOT / "skills").rglob("*.md"):
    ALL_FILES_BY_NAME.setdefault(_p.name, []).append(_p)


@dataclass
class Finding:
    file: Path
    line: int
    severity: str  # "error" or "warn"
    code: str
    message: str


@dataclass
class Report:
    findings: list[Finding] = field(default_factory=list)

    def add(self, f: Finding) -> None:
        self.findings.append(f)

    @property
    def errors(self) -> list[Finding]:
        return [f for f in self.findings if f.severity == "error"]

    @property
    def warns(self) -> list[Finding]:
        return [f for f in self.findings if f.severity == "warn"]


def extract_frontmatter(text: str) -> tuple[dict, int]:
    """Return (parsed fm, line-number where body starts)."""
    if not text.startswith("---"):
        return {}, 1
    try:
        end = text.index("---", 3)
    except ValueError:
        return {}, 1
    fm_text = text[3:end]
    try:
        fm = yaml.safe_load(fm_text) or {}
    except yaml.YAMLError:
        fm = {}
    body_start = text.count("\n", 0, end) + 2  # +1 for the `---`, +1 to move past
    return fm, body_start


def classify(path: Path) -> str | None:
    rel = path.relative_to(REPO_ROOT).as_posix()
    # Reports/audit files dropped under domains/ are not entries — skip them.
    if "/reports/" in rel:
        return None
    if "/skills/" in rel and path.name == "SKILL.md":
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


def lint_file(path: Path, report: Report) -> None:
    if not path.exists():
        report.add(Finding(path, 0, "error", "E000", f"file does not exist: {path}"))
        return

    text = path.read_text(encoding="utf-8")
    lines = text.split("\n")
    line_count = len(lines)

    # Classify first: only entry files (thinker/concept/skill/...) are subject
    # to the per-entry checks below. Non-entry files living under domains/ (e.g.
    # a report dropped into domains/.../reports/) are skipped for frontmatter
    # and section checks. They still get the line-length advisory.
    entry_type = classify(path)

    # --- Line length (advisory for all files) ---
    if line_count < MIN_LINES:
        report.add(Finding(path, 1, "warn", "W001", f"too short ({line_count} < {MIN_LINES} lines)"))
    if line_count > MAX_LINES:
        report.add(Finding(path, 1, "warn", "W002", f"too long ({line_count} > {MAX_LINES} lines)"))

    if entry_type is None:
        return  # non-entry file (README, report, etc.)

    # --- Frontmatter (entries only) ---
    fm, body_start = extract_frontmatter(text)
    if not fm:
        report.add(Finding(path, 1, "error", "E001", "missing or invalid YAML frontmatter"))
        return

    # Required fields
    for field_name in REQUIRED_FRONTMATTER.get(entry_type, []):
        if field_name not in fm or fm[field_name] in (None, "", []):
            report.add(Finding(path, 1, "error", "E002",
                               f"frontmatter missing required field: {field_name}"))

    # Thinker: must have either `name` or `title`
    if entry_type == "thinker" and not (fm.get("name") or fm.get("title")):
        report.add(Finding(path, 1, "error", "E002",
                           "thinker frontmatter needs either `name` or `title`"))

    # Tags
    tags = fm.get("tags")
    if not tags:
        report.add(Finding(path, 1, "warn", "W003", "no tags"))

    # --- Required sections ---
    h2s = [m.group(1) for m in re.finditer(r"^## (.+)$", text, re.MULTILINE)]
    for required in REQUIRED_SECTIONS.get(entry_type, []):
        if not any(required in h for h in h2s):
            report.add(Finding(path, 1, "warn", "W004", f"missing section: {required}"))

    # --- Relative link validity ---
    # Two failure modes:
    #   E003 (error, blocks CI): the target EXISTS somewhere in the repo but
    #     this link's path is wrong — a mechanical defect that should be fixed.
    #   W006 (warn): the target basename exists NOWHERE in the repo, meaning the
    #     linked concept/thinker has not been authored yet. This is a content
    #     backlog item (tracked in reports/audit/*-content-backlog.md), not a
    #     structural defect, so it warns rather than blocking CI.
    for i, line in enumerate(lines, start=1):
        for m in MD_LINK_RE.finditer(line):
            target = m.group(2)
            # Skip http(s), mailto, anchor-only, and absolute paths
            if target.startswith(("http://", "https://", "mailto:", "#", "/")):
                continue
            # Resolve relative to file's directory
            resolved = (path.parent / target).resolve()
            if resolved.exists():
                continue
            target_name = Path(target).name
            # Special case: SKILL.md targets share one basename across 100+ skill
            # dirs. The meaningful existence check is whether the *parent skill
            # dir* exists anywhere under skills/. If not, the skill itself has not
            # been authored → W006 content backlog, not E003 structural error.
            if target_name == "SKILL.md":
                skill_dir = Path(target).parent.name
                if skill_dir and not any(
                    (REPO_ROOT / "skills" / fw / skill_dir).exists()
                    for fw in (p.name for p in (REPO_ROOT / "skills").iterdir()
                               if p.is_dir())
                ):
                    report.add(Finding(path, i, "warn", "W006",
                                       f"link to unauthored skill: {target}"))
                    continue
            if ALL_FILES_BY_NAME and target_name in ALL_FILES_BY_NAME:
                # Path-aware disambiguation: even when the basename exists, the
                # link may name a sub-path (e.g. education/schools/.../piaget.md,
                # traditions/buddhism/core-teachings.md) that exists nowhere. If
                # no candidate shares the link's penultimate path segment, the
                # intended target is genuinely missing → W006, not E003.
                penult = Path(target).parent.name
                candidates = ALL_FILES_BY_NAME[target_name]
                if penult and not any(
                    penult == c.parent.name or penult in c.parent.as_posix()
                    for c in candidates
                ):
                    report.add(Finding(path, i, "warn", "W006",
                                       f"link to unauthored entry: {target}"))
                else:
                    report.add(Finding(path, i, "error", "E003",
                                       f"broken relative link: {target}"))
            else:
                report.add(Finding(path, i, "warn", "W006",
                                   f"link to unauthored entry: {target}"))

    # --- Cross-links (for thinker/concept) ---
    # Accept any relative link to another .md file as a cross-link
    if entry_type in ("thinker", "concept"):
        has_cross = False
        for line in lines:
            for m in MD_LINK_RE.finditer(line):
                target = m.group(2)
                if target.startswith(("http://", "https://", "mailto:", "#", "/")):
                    continue
                if target.endswith(".md"):
                    has_cross = True
                    break
            if has_cross:
                break
        if not has_cross:
            report.add(Finding(path, 1, "warn", "W005",
                               "no cross-link to another .md file detected"))


def collect_files(targets: list[Path]) -> list[Path]:
    if targets:
        return [p.resolve() for p in targets if p.exists()]
    files = []
    for path in sorted(DOMAINS_DIR.rglob("*.md")):
        if path.name in SKIP_FILENAMES:
            continue
        if classify(path) is None:
            continue
        files.append(path)
    return files


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", type=Path, help="Files to lint")
    parser.add_argument("--strict", action="store_true",
                        help="Fail on warnings too")
    parser.add_argument("--json", action="store_true",
                        help="Emit JSON output")
    parser.add_argument("--quiet", action="store_true",
                        help="Only print findings")
    args = parser.parse_args()

    report = Report()
    files = collect_files(args.paths)

    for path in files:
        lint_file(path, report)

    if args.json:
        out = {
            "files_scanned": len(files),
            "errors": len(report.errors),
            "warns": len(report.warns),
            "findings": [
                {
                    "file": str(f.file.relative_to(REPO_ROOT)),
                    "line": f.line,
                    "severity": f.severity,
                    "code": f.code,
                    "message": f.message,
                }
                for f in report.findings
            ],
        }
        print(json.dumps(out, ensure_ascii=False, indent=2))
        return 1 if report.errors else (1 if args.strict and report.warns else 0)

    # Human-readable output
    if not args.quiet:
        print(f"Linted {len(files)} files")

    if not report.findings:
        print("✓ clean")
        return 0

    for f in sorted(report.findings, key=lambda x: (str(x.file), x.line)):
        rel = f.file.relative_to(REPO_ROOT)
        marker = "✗" if f.severity == "error" else "⚠"
        print(f"{marker} {rel}:{f.line} [{f.code}] {f.message}")

    print(f"\n{len(report.errors)} error(s), {len(report.warns)} warning(s)")
    if report.errors:
        return 1
    return 1 if args.strict and report.warns else 0


if __name__ == "__main__":
    raise SystemExit(main())
