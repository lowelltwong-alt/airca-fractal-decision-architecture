# AIRCA Framework Spec

This package adds a framework-agnostic core schema for AIRCA-style decision architecture, with separate extension packs for religious and secular use.

It implements the core separation between:

- Question / Topic
- View / Position
- Assessment
- Assertion
- Coherence

It is intended as a starter architecture slice for the repository and can later be folded into a deeper fractal structure.

## Included

- docs/core-schema-spec.md
- schemas/core/classes.yaml
- schemas/core/edges.yaml
- schemas/extensions/religious.yaml
- schemas/extensions/secular.yaml
- validation/shacl/core.shacl.ttl
- examples/religious-justification.ttl
- examples/secular-ai-safety.ttl

## Design goal

The architecture is domain-neutral at the core, then specialized by extension packs. This avoids making theology the universal default while still supporting theology as a first-class implementation.
