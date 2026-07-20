#!/usr/bin/env python3
"""
generate_quotes_batch.py — generate 名言/*.md quote files and new thinker entries
from batch_quotes_data.py.

Usage:
    python3 _meta/scripts/generate_quotes_batch.py
"""

from __future__ import annotations

import sys
from collections import defaultdict
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("ERROR: pyyaml required. Install with `pip install pyyaml`.")

from batch_quotes_data import NEW_THINKERS, QUOTES, REPO_ROOT


def quote_frontmatter(q: dict, related: list[str]) -> dict:
    return {
        "id": q["id"],
        "title": q["title"],
        "type": "quote",
        "author": q["author"],
        "author_era": q["author_era"],
        "author_nationality": q["author_nationality"],
        "domain": q["domain"],
        "school": q["school"],
        "era": q["era"],
        "year": q["year"],
        "original_language": q["original_language"],
        "tags": q["tags"],
        "mood": q["mood"],
        "cross-refs": [{"id": q["cross_ref_id"], "relation": "思想家"}],
        "related_quotes": related,
    }


def write_quote(q: dict, related: list[str]) -> Path:
    theme_dir = REPO_ROOT / "名言" / q["theme"]
    theme_dir.mkdir(parents=True, exist_ok=True)
    path = theme_dir / q["filename"]

    fm = quote_frontmatter(q, related)
    fm_yaml = yaml.safe_dump(fm, allow_unicode=True, sort_keys=False, line_break="\n").strip()

    lines = [
        "---",
        fm_yaml,
        "---",
        "",
        f"# {q['title']}",
        "",
        f"> *{q['original']}*",
        ">",
        f"> {q['translation']}",
        f"> — {q['source']}",
        "",
        "---",
        "",
        "## 出处",
        "",
        q["context"],
        "",
        "---",
        "",
        "## 解读",
        "",
    ]
    for heading, body in q["interpretation"]:
        lines.extend([f"### {heading}", "", body, ""])

    lines.extend([
        "---",
        "",
        "## 思想谱系",
        "",
        "| 传统 | 表述 | 侧重 |",
        "|------|------|------|",
    ])
    for row in q["genealogy"]:
        lines.append(f"| {row[0]} | {row[1]} | {row[2]} |")

    lines.extend([
        "",
        "---",
        "",
        "## 自媒体金句",
        "",
        f"- **封面句**：{q['hooks']['cover']}",
        f"- **短视频 Hook**：{q['hooks']['video']}",
        f"- **朋友圈文案**：{q['hooks']['social']}",
        "",
        "### 情绪与视觉",
        "",
        f"- **情绪基调**：{q['mood']}",
        f"- **视觉意象**：{q['visual']}",
        "",
        "---",
        "",
        "## 延伸阅读",
        "",
    ])
    for item in q["further"]:
        lines.append(f"- {item}")
    lines.append("")

    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def write_thinker(tid: str, info: dict) -> Path:
    path = REPO_ROOT / info["path"]
    path.parent.mkdir(parents=True, exist_ok=True)

    raw_sources = info.get("sources", [])
    sources = []
    for s in raw_sources:
        if isinstance(s, dict):
            sources.append({"title": s["title"], "year": s["year"]})
        else:
            title, year = s
            sources.append({"title": title, "year": year})
    fm = {
        "id": tid,
        "title": info["title"],
        "type": "thinker",
        "domain": info["domain"],
        "school": info["school"],
        "era": info["era"],
        "birth": info.get("birth"),
        "tags": info["tags"],
        "aliases": info.get("aliases", []),
    }
    if info.get("death"):
        fm["death"] = info["death"]
    if sources:
        fm["sources"] = sources

    fm_yaml = yaml.safe_dump(fm, allow_unicode=True, sort_keys=False, line_break="\n").strip()

    lines = [
        "---",
        fm_yaml,
        "---",
        "",
        f"# {info['title']}",
        "",
        info["intro"],
        "",
        "## 核心命题 / Core Theses",
        "",
    ]
    for i, (heading, body) in enumerate(info["theses"], 1):
        lines.extend([f"### {i}. {heading}", "", body, ""])

    lines.extend([
        "## 关键著作 / Key Works",
        "",
    ])
    for w in info["works"]:
        lines.append(f"- {w}")
    lines.append("")

    lines.extend([
        "## 跨学科关联 / Interdisciplinary Links",
        "",
    ])
    for link in info["links"]:
        lines.append(f"- {link}")
    lines.append("")

    lines.extend([
        "## 进阶阅读 / Further Reading",
        "",
    ])
    for r in info["reading"]:
        lines.append(f"- {r}")
    lines.append("")

    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def main() -> int:
    # Group quotes by theme to build related_quotes
    by_theme: dict[str, list[dict]] = defaultdict(list)
    for q in QUOTES:
        by_theme[q["theme"]].append(q)

    theme_files = {
        theme: [f"名言/{q['theme']}/{q['filename']}" for q in qs]
        for theme, qs in by_theme.items()
    }

    quote_count = 0
    for q in QUOTES:
        related = [p for p in theme_files[q["theme"]] if p != f"名言/{q['theme']}/{q['filename']}"]
        write_quote(q, related)
        quote_count += 1

    thinker_count = 0
    for tid, info in NEW_THINKERS.items():
        write_thinker(tid, info)
        thinker_count += 1

    print(f"Generated {quote_count} quotes in {len(by_theme)} themes.")
    print(f"Generated {thinker_count} new thinker entries.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
