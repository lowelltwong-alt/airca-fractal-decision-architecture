# ROADMAP

This roadmap turns the repository from a strong concept-and-notes project into a validated, machine-readable, governance-ready architecture.

## Why this roadmap exists

The repository already has a clear thesis: as AI makes answers cheaper, the scarce resource becomes decision capacity.

What is still missing is the execution layer that makes that thesis durable:
- consistent artifact contracts
- validation and CI
- explicit framework files, not only framework intent
- lifecycle and change governance
- pilot examples that prove the architecture can travel from theory into use

## Phase 0 — Repository hygiene and truth-in-structure

### Goals
- Keep `docs/how-to-read-this-repo.md` as the reading guide.
- Make `ROADMAP.md` an actual roadmap.
- Align every “included” or “coming next” claim with the files that actually exist.

### Deliverables
- Replace the duplicated reading-guide content in `ROADMAP.md`.
- Add a repository-wide artifact schema.
- Add a validator script and CI workflow.
- Fill the root `framework/` package with the files it already promises.

### Exit criteria
- The repository tree matches its own README claims.
- All `artifact.json` files validate.
- CI fails on contract drift.

## Phase 1 — Artifact contract and repository validation

### Goals
- Make machine-readable artifacts real repository primitives, not just examples.
- Normalize metadata across root and concept-node artifacts.

### Deliverables
- `schemas/artifact.schema.json`
- normalized `artifact.json` files across the repo
- `scripts/validate_repo.py`
- `.github/workflows/validate.yml`

### Exit criteria
- every artifact has:
  - stable `artifact_id`
  - consistent `artifact_type`
  - normalized author structure
  - version and status
  - summary
  - scope
  - source document references
- duplicate IDs are rejected
- broken source references are rejected

## Phase 2 — Framework core becomes executable

### Goals
- Turn the root `framework/` package into a usable starter kit.
- Make the architecture legible to humans and testable by machines.

### Deliverables
- `framework/docs/core-schema-spec.md`
- `framework/schemas/core/classes.yaml`
- `framework/schemas/core/edges.yaml`
- `framework/schemas/extensions/religious.yaml`
- `framework/schemas/extensions/secular.yaml`
- `framework/validation/shacl/core.shacl.ttl`
- `framework/examples/religious-justification.ttl`
- `framework/examples/secular-ai-safety.ttl`

### Exit criteria
- the framework package is self-describing
- example data conforms to the starter shape rules
- the root `framework/README.md` is no longer aspirational

## Phase 3 — Governance and lifecycle

### Goals
- Make ontology/taxonomy evolution governable.
- Prevent silent semantic drift.

### Deliverables
- `GOVERNANCE.md`
- `governance/change-taxonomy.yaml`
- lifecycle expectations for draft → active → deprecated → retired
- replacement and migration rules for future term changes

### Exit criteria
- breaking vs non-breaking changes are defined
- deprecations preserve resolvability and replacement pointers
- reviewers and required artifacts are explicit

## Phase 4 — Applied pilots

### Goals
- Demonstrate that AIRCA + fractal architecture works on real decisions, not only on conceptual notes.

### Pilot tracks
1. **Secular pilot**
   - AI safety / policy / product governance example
2. **Christian pilot**
   - LAIRCA / theological governance example
3. **Cross-context pilot**
   - same core framework + different extension pack

### Exit criteria
- each pilot has:
  - a bounded question
  - structured views / positions
  - assessments and assertions
  - evidence / provenance
  - coherence or ranking output
  - review trail

## Suggested release sequence

### v0.2
Repository contracts and validation
- artifact schema
- normalized artifacts
- CI
- real roadmap

### v0.3
Framework starter package
- classes
- edges
- extension packs
- SHACL
- examples

### v0.4
Governance release
- change taxonomy
- lifecycle policy
- migration rules

### v0.5
Pilot release
- one secular pilot
- one Christian pilot
- documented review path

## Current priority

The highest-leverage next move is not writing more notes.

It is locking the repository’s own contracts:
1. schema
2. validation
3. framework starter files
4. governance rules

That is the shortest path from “interesting architecture” to “credible reference implementation.”
