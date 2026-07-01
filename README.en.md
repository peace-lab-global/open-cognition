# Open Cognition

> A cross-disciplinary cognitive knowledge base for **human deep reading** and **AI agent consumption**.
> Structured, linkable, and searchable ideas, propositions, and methods from philosophy, religion, sociology, psychology, ethics, aesthetics, literature, arts, and cognitive systems engineering.

[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](./LICENSE)
[![Status](https://img.shields.io/badge/status-v0.9%20buddhist--academy--deep-blue.svg)](#)
[![Domains](https://img.shields.io/badge/domains-9-orange.svg)](#domains)
[![Entries](https://img.shields.io/badge/entries-210%20thinkers%20%7C%20213%20concepts%20%7C%20126%20skills-brightgreen.svg)](#content-overview)

**Chinese version**: see [README.md](README.md)

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
= 210 thinkers | 213 concepts | 126 Skills | 650+ structured .md files
```

### Domains

| Domain | Thinkers | Concepts | Skills | Entry point |
|---|:---:|:---:|:---:|---|
| Philosophy | 42 | 8 | 19 | [philosophy](philosophy/README.md) |
| Religion | 34 | 127 | 39 | [religion](religion/README.md) |
| Sociology | 18 | 7 | 15 | [sociology](sociology/README.md) |
| Psychology | 42 | 8 | 16 | [psychology](psychology/README.md) |
| Ethics & Politics | 15 | 11 | 10 | [ethics-politics](ethics-politics/README.md) |
| Aesthetics | 23 | 9 | 3 | [aesthetics](aesthetics/README.md) |
| Literature | 5 | 8 | 5 | [literature](literature/README.md) |
| Arts | 3 | 8 | 3 | [arts](arts/README.md) |
| Cognitive Systems Engineering | 28 | 27 | 16 | [cognitive-systems](cognitive-systems/README.md) |

Full index: [INDEX.md](INDEX.md) | Tag taxonomy: [TAGS.md](TAGS.md)

---

## Flagship: Buddhist Cognitive Theory

Under `religion/buddhism/concepts/cognitive-theory/`, this repository contains the deepest thematic treatment in the entire knowledge base -- a systematic treatment of Buddhism's cognitive science and epistemology resources.

Quick start guide: [QUICKSTART.md](religion/buddhism/concepts/cognitive-theory/QUICKSTART.md)

### Scope

| Layer | Count | Coverage |
|------|------|------|
| Concept files | 15 core + 4 meditation topics = **19** | Yogacara, Madhyamaka, Abhidharma, Pramana, Early Buddhism, Chan/Zen |
| Applied Skills | **15** | Eight Consciousness diagnosis, Three Natures diagnosis, Pramana verification, Dependent Origination tracing, Five Aggregates deconstruction |
| Sutra cognitive architectures | **18 sutras** | Shurangama, Samdhinirmocana, Lankavatara, Heart Sutra, Diamond Sutra, Platform Sutra, and more |
| School cognitive frameworks | **8** | Theravada, Madhyamaka, Yogacara, Tiantai, Huayan, Chan, Pure Land, Vajrayana |
| Master cognitive contributions | **32** | Nagarjuna, Asanga/Vasubandhu, Zhiyi, Fazang, Huineng, Tsongkhapa, Dogen, Padmasambhava, and more |

### Entry Points

- **Main index**: [`religion/buddhism/INDEX.md`](religion/buddhism/INDEX.md)
- **Cognitive theory catalog**: [`concepts/cognitive-theory/README.md`](religion/buddhism/concepts/cognitive-theory/README.md)
- **Representative concepts**: [Pramana](religion/buddhism/concepts/cognitive-theory/pramana.md) | [Three Natures](religion/buddhism/concepts/cognitive-theory/three-natures.md) | [Consciousness Transformation](religion/buddhism/concepts/cognitive-theory/consciousness-transformation.md) | [Koan Mechanics](religion/buddhism/concepts/cognitive-theory/koan-mechanics.md)
- **Representative Skills**: [Eight Consciousness Diagnosis](religion/buddhism/skills/eight-consciousness-diagnosis/SKILL.md) | [Three Natures Diagnosis](religion/buddhism/skills/three-natures-diagnosis/SKILL.md) | [Dependent Origination Tracing](religion/buddhism/skills/dependent-origination-tracing/SKILL.md) | [Five Aggregates Deconstruction](religion/buddhism/skills/five-aggregates-deconstruction/SKILL.md)

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
  philosophy/                  # Philosophy (42 thinkers / 8 concepts / 19 skills)
  religion/                    # Religion (incl. Buddhist cognitive theory flagship)
  sociology/                   # Sociology
  psychology/                  # Psychology
  ethics-politics/             # Ethics & Political Philosophy
  aesthetics/                  # Aesthetics
  literature/                  # Literature
  arts/                        # Arts
  cognitive-systems/           # Cognitive Systems Engineering
  _meta/                       # Metadata, taxonomy, templates, reports
```

See the [Chinese README](README.md) for the full directory tree.

---

## Entry Types

### Thinker

Fixed structure: basic info, core propositions, intellectual context, key works, important concepts, coordinate mapping, contemporary applications, common misreadings, cross-disciplinary links, further reading, linked Skills.

Examples: [Freud](psychology/schools/psychoanalysis/freud.md) | [Weber](sociology/schools/classical/weber.md) | [Kant](philosophy/schools/german-idealism/kant.md) | [Nagarjuna](religion/buddhism/masters/nagarjuna.md) | [Dogen](religion/buddhism/masters/dogen.md)

### Concept

Fixed structure: one-line definition, historical context, core content, colloquial vs. scholarly framing, related concepts, representative thinkers, application scenarios, common misreadings, cross-disciplinary links, further reading.

Examples: [Flow](psychology/concepts/flow.md) | [Cultural Capital](sociology/concepts/cultural-capital.md) | [Sacred](religion/concepts/sacred.md) | [Pramana](religion/buddhism/concepts/cognitive-theory/pramana.md)

### Skill

Agent-executable operational framework with YAML frontmatter, one-line function description, when-to-use / when-not-to-use guidance, theoretical basis, step-by-step procedure, worked examples, and counterexamples.

Examples: [CBT Cognitive Distortion](./psychology/skills/cbt-cognitive-distortion/SKILL.md) | [Bourdieu Field Analysis](./sociology/skills/bourdieu-field-analysis/SKILL.md) | [Four Noble Truths](./religion/skills/four-noble-truths-framework/SKILL.md) | [Eight Consciousness Diagnosis](religion/buddhism/skills/eight-consciousness-diagnosis/SKILL.md)

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

Full agent integration guide: [AGENT.md](AGENT.md)

---

## License

Content is licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Free to use, modify, and distribute with attribution.

---

## Contributing

Contributions of new entries, misreading corrections, and cross-disciplinary links are welcome. See:

- [CONTRIBUTING.md](CONTRIBUTING.md) -- contribution workflow
- [_meta/quality-criteria.md](./_meta/quality-criteria.md) -- quality standards
- [_meta/taxonomy.md](./_meta/taxonomy.md) -- taxonomy
- [_meta/templates/](./_meta/templates/) -- entry templates

---

> "All conditioned phenomena are like dreams, illusions, bubbles, shadows; like dew and like lightning -- one should contemplate them thus." -- *Diamond Sutra*
>
> "The map is not the territory." -- Alfred Korzybski
