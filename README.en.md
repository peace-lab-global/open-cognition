# Open Cognition

> A cross-disciplinary cognitive knowledge base for **human deep reading** and **AI agent consumption**.
> Structured, linkable, and searchable ideas, propositions, and methods from philosophy, religion, sociology, psychology, ethics, aesthetics, literature, arts, and cognitive systems engineering.

[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](./LICENSE)
[![Status](https://img.shields.io/badge/status-v0.9%20buddhist--academy--deep-blue.svg)](#)
[![Domains](https://img.shields.io/badge/domains-9-orange.svg)](#domains)
[![Entries](https://img.shields.io/badge/entries-178%20thinkers%20%7C%20144%20concepts%20%7C%20111%20skills-brightgreen.svg)](#content-overview)

**Chinese version**: see [README.md](./README.md)

---

## Overview

Insights across disciplines are scattered across hard-to-read primary texts and mutually unintelligible schools. This project aims to:

1. **Lower the barrier** -- Build a holistic sense of a thinker or concept through compact ~100-line entries.
2. **Preserve depth** -- No pop-psychology simplifications. Each entry includes primary sources, scholarly references, and introductory readings.
3. **Cross-link disciplines** -- Explicitly annotate relationships: derivation, complementarity, opposition, development, critique, parallel, tension, inheritance, borrowing, and subordination.
4. **Serve AI agents directly** -- Distill standardized **Skills** (operational frameworks) so that LLMs and humans can work from the same knowledge base.
5. **Deep-dive topics** -- Build thematic deep-dives on key axes (e.g., Buddhist cognitive theory) forming sub-systems usable for research, teaching, and practice.

---

## Content Overview

```
9 domains x N thinker/concept entries + Skills + thematic deep-dives
= 178 thinkers | 144 concepts | 111 Skills | 550+ structured .md files
```

### Domains

| Domain | Thinkers | Concepts | Skills | Entry point |
|---|:---:|:---:|:---:|---|
| Philosophy | 28 | 8 | 19 | [domains/philosophy](./domains/philosophy/README.md) |
| Religion | 32 | 76 | 39 | [domains/religion](./domains/religion/README.md) |
| Sociology | 18 | 7 | 15 | [domains/sociology](./domains/sociology/README.md) |
| Psychology | 28 | 8 | 16 | [domains/psychology](./domains/psychology/README.md) |
| Ethics & Politics | 15 | 11 | 10 | [domains/ethics-politics](./domains/ethics-politics/README.md) |
| Aesthetics | 23 | 7 | 3 | [domains/aesthetics](./domains/aesthetics/README.md) |
| Literature | 5 | -- | 5 | [domains/literature](./domains/literature/README.md) |
| Arts | 3 | -- | 3 | [domains/arts](./domains/arts/README.md) |
| Cognitive Systems Engineering | 26 | 27 | 16 | [domains/cognitive-systems](./domains/cognitive-systems/README.md) |

Full index: [INDEX.md](./INDEX.md) | Tag taxonomy: [TAGS.md](./TAGS.md)

---

## Flagship: Buddhist Cognitive Theory

Under `domains/religion/buddhism/concepts/cognitive-theory/`, this repository contains the deepest thematic treatment in the entire knowledge base -- a systematic treatment of Buddhism's cognitive science and epistemology resources.

Quick start guide: [QUICKSTART.md](./domains/religion/buddhism/concepts/cognitive-theory/QUICKSTART.md)

### Scope

| Layer | Count | Coverage |
|------|------|------|
| Concept files | 15 core + 4 meditation topics = **19** | Yogacara, Madhyamaka, Abhidharma, Pramana, Early Buddhism, Chan/Zen |
| Applied Skills | **15** | Eight Consciousness diagnosis, Three Natures diagnosis, Pramana verification, Dependent Origination tracing, Five Aggregates deconstruction |
| Sutra cognitive architectures | **18 sutras** | Shurangama, Samdhinirmocana, Lankavatara, Heart Sutra, Diamond Sutra, Platform Sutra, and more |
| School cognitive frameworks | **8** | Theravada, Madhyamaka, Yogacara, Tiantai, Huayan, Chan, Pure Land, Vajrayana |
| Master cognitive contributions | **32** | Nagarjuna, Asanga/Vasubandhu, Zhiyi, Fazang, Huineng, Tsongkhapa, Dogen, Padmasambhava, and more |

### Entry Points

- **Main index**: [`domains/religion/buddhism/INDEX.md`](./domains/religion/buddhism/INDEX.md)
- **Cognitive theory catalog**: [`concepts/cognitive-theory/README.md`](./domains/religion/buddhism/concepts/cognitive-theory/README.md)
- **Representative concepts**: [Pramana](./domains/religion/buddhism/concepts/cognitive-theory/pramana.md) | [Three Natures](./domains/religion/buddhism/concepts/cognitive-theory/three-natures.md) | [Consciousness Transformation](./domains/religion/buddhism/concepts/cognitive-theory/consciousness-transformation.md) | [Koan Mechanics](./domains/religion/buddhism/concepts/cognitive-theory/koan-mechanics.md)
- **Representative Skills**: [Eight Consciousness Diagnosis](./domains/religion/buddhism/concepts/cognitive-theory/skills/eight-consciousness-diagnosis/SKILL.md) | [Three Natures Diagnosis](./domains/religion/buddhism/concepts/cognitive-theory/skills/three-natures-diagnosis/SKILL.md) | [Dependent Origination Tracing](./domains/religion/buddhism/concepts/cognitive-theory/skills/dependent-origination-tracing/SKILL.md) | [Five Aggregates Deconstruction](./domains/religion/buddhism/concepts/cognitive-theory/skills/five-aggregates-deconstruction/SKILL.md)

### Dialogue with Contemporary Thought

Each concept file explicitly builds bridges to modern cognitive science, psychology, phenomenology, philosophy of mind, and AI. For example:

- Eight Consciousnesses and the Default Mode Network (DMN)
- Five Aggregates and Hume's bundle theory / the binding problem
- Pramana and falsificationism / Carnap's internal-external distinction
- Koan and insight neuroscience (gamma band, Kounios & Beeman)
- Silent Illumination and pre-reflective self-awareness (Zahavi)
- Bija (seeds) and predictive coding (Friston)

---

## Repository Structure

```
open-cognition/
  README.md                   # Chinese README (project overview)
  README.en.md                # This file (English overview)
  AGENT.md                    # AI Agent integration guide
  INDEX.md                    # Full dual-perspective index
  TAGS.md                     # Unified tag taxonomy
  CONTRIBUTING.md             # Contribution guide
  index.json                  # Machine-readable index
  domains/                    # Main knowledge entries (9 domains)
  skills/                     # Operational skill frameworks
  wisdom-masters/             # Distilled contemplative wisdom
  meta/                       # Metadata, taxonomy, templates
  visual/                     # Infographics and visualizations
  reports/                    # Progress reports and audits
```

See the [Chinese README](./README.md) for the full directory tree.

---

## Entry Types

### Thinker

Fixed structure: basic info, core propositions, intellectual context, key works, important concepts, coordinate mapping, contemporary applications, common misreadings, cross-disciplinary links, further reading, linked Skills.

Examples: [Freud](./domains/psychology/schools/psychoanalysis/freud.md) | [Weber](./domains/sociology/schools/classical/weber.md) | [Kant](./domains/philosophy/schools/german-idealism/kant.md) | [Nagarjuna](./domains/religion/buddhism/masters/nagarjuna.md) | [Dogen](./domains/religion/buddhism/masters/dogen.md)

### Concept

Fixed structure: one-line definition, historical context, core content, colloquial vs. scholarly framing, related concepts, representative thinkers, application scenarios, common misreadings, cross-disciplinary links, further reading.

Examples: [Flow](./domains/psychology/concepts/flow.md) | [Cultural Capital](./domains/sociology/concepts/cultural-capital.md) | [Sacred](./domains/religion/concepts/sacred.md) | [Pramana](./domains/religion/buddhism/concepts/cognitive-theory/pramana.md)

### Skill

Agent-executable operational framework with YAML frontmatter, one-line function description, when-to-use / when-not-to-use guidance, theoretical basis, step-by-step procedure, worked examples, and counterexamples.

Examples: [CBT Cognitive Distortion](./skills/psychology-frameworks/cbt-cognitive-distortion/SKILL.md) | [Bourdieu Field Analysis](./skills/sociology-frameworks/bourdieu-field-analysis/SKILL.md) | [Four Noble Truths](./skills/religion-frameworks/four-noble-truths-framework/SKILL.md) | [Eight Consciousness Diagnosis](./domains/religion/buddhism/concepts/cognitive-theory/skills/eight-consciousness-diagnosis/SKILL.md)

---

## For AI Agents

All Skill files follow a unified frontmatter format:

```yaml
---
name: <skill-id>
description: <one-line function>
domain: <philosophy|religion|sociology|psychology|...>
linked_concepts: [relative paths to related concepts...]
tags: [...]
---
```

These can be directly indexed and invoked by agent runtimes (Claude Skills, Qoder Skills, custom RAG pipelines). Cross-references between entries use relative paths and explicit relationship-type annotations, supporting LLM graph reasoning.

Full agent integration guide: [AGENT.md](./AGENT.md)

---

## License

Content is licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Free to use, modify, and distribute with attribution.

---

## Contributing

Contributions of new entries, misreading corrections, and cross-disciplinary links are welcome. See:

- [CONTRIBUTING.md](./CONTRIBUTING.md) -- contribution workflow
- [meta/quality-criteria.md](./meta/quality-criteria.md) -- quality standards
- [meta/taxonomy.md](./meta/taxonomy.md) -- taxonomy
- [meta/templates/](./meta/templates/) -- entry templates

---

> "All conditioned phenomena are like dreams, illusions, bubbles, shadows; like dew and like lightning -- one should contemplate them thus." -- *Diamond Sutra*
>
> "The map is not the territory." -- Alfred Korzybski
