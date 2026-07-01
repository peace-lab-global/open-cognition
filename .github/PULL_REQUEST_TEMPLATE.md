## Summary

<!-- 1-3 sentences describing what changed and why. -->

## Type of change

- [ ] 📚 New entry (thinker / concept / Skill)
- [ ] ✏️ Edit to existing entry (content correction, typo, deeper analysis)
- [ ] 🔗 Cross-link / backlink repair
- [ ] 🏗 Infrastructure (scripts, CI, templates, README)
- [ ] 🐛 Bug fix (rendering, broken link, lint error)
- [ ] 🧹 Chore (formatting, rename, reorganize)

## Scope

| Dimension | Count |
|---|---|
| Files added |  |
| Files modified |  |
| Files deleted |  |
| Domains touched |  |

<!-- Example: "3 files added, 2 modified, philosophy + psychology" -->

## Checklist

- [ ] I have read [CONTRIBUTING.md](../CONTRIBUTING.md) and [meta/quality-criteria.md](../meta/quality-criteria.md).
- [ ] New entries follow the templates in `templates/`.
- [ ] Frontmatter contains required fields (see `scripts/lint.py` for the schema).
- [ ] Every entry has a `## 跨学科关联` section with at least 1 cross-domain link.
- [ ] Every entry has a `## 常见误读` section (for thinker/concept entries).
- [ ] All relative links resolve (no E003 lint errors).
- [ ] `scripts/lint.py` passes: `python3 scripts/lint.py --strict path/to/file.md`
- [ ] `index.json` is up-to-date (auto-rebuilt by pre-commit hook, or run `python3 scripts/build-index.py` manually).
- [ ] Chinese is the main language; original terms (English/German/French/Greek/Sanskrit/Pali) in parentheses.

## Pre-merge self-check

Run locally before requesting review:

```bash
python3 scripts/lint.py                     # entry quality
python3 scripts/build-index.py --check      # index consistency
git diff --stat                             # scope sanity
```

## Related issues

<!-- Closes #NNN, Related to #NNN -->

## Notes for reviewers

<!-- Anything that deserves attention: trade-offs, design choices, open questions. -->

## License

By submitting this PR, I confirm my contribution is licensed under the project's
[CC BY-SA 4.0](../LICENSE) and that I have the right to license it as such.
