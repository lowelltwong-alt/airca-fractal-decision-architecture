# Framework Core in Fractal Ontology

This node places the framework-agnostic ontology core inside the repository's fractal ontology structure.

It provides the reusable semantic layer for representing:

- questions and topics
- views and positions
- assertions and provenance
- scoped assessments
- typed dependencies and contradictions
- constraint bundles
- coherence-relevant relationship structures

## Purpose

The core ontology should remain domain-neutral.

It is designed so that theology is not the universal default, while still supporting theology as a first-class extension. The same core can also support policy, governance, legal reasoning, organizational values, and other structured worldview or decision domains.

## Included artifacts

- `core-schema-spec.md`
- `schemas/core/classes.yaml`
- `schemas/core/edges.yaml`
- `schemas/extensions/religious.yaml`
- `schemas/extensions/secular.yaml`
- `validation/shacl/core.shacl.ttl`

## Core separation

The ontology separates:

- `Question` / `Topic`
- `View`
- `Assessment`
- `Assertion`
- `FrameworkProfile`
- `ConstraintBundle`

This prevents a single concept such as doctrine, policy, or principle from carrying every concern at once.

## Why this matters

The architecture treats the problem as more than taxonomy. It is also a coherence problem.

That means the ontology needs to preserve not only classification and relation types, but also enough structure for downstream scoring, propagation, review, and misalignment analysis.
