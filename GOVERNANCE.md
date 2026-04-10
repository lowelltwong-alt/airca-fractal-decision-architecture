# GOVERNANCE

This repository treats meaning, identifiers, and machine-readable artifacts as governed assets.

## Core rules

### 1. Stable artifact identity
- Every `artifact.json` must have a stable `artifact_id`.
- IDs should not be reused.
- If meaning changes substantially, prefer deprecate-and-replace over silent mutation.

### 2. Validate before merge
Every pull request should pass repository validation:
- artifact schema validation
- duplicate-ID checks
- source document existence checks
- framework starter file presence checks

### 3. Deprecate instead of disappearing
If a concept, schema, or mapping becomes obsolete:
- keep the identifier resolvable
- mark it deprecated
- point to a replacement where possible
- record the reason in the change log or action log

### 4. Keep theory and execution aligned
If a README says a package includes files or capabilities, those files must exist in the repository.

## Change taxonomy

See `governance/change-taxonomy.yaml` for the default change types, review expectations, and lifecycle rules.

## Current governance focus

This repository is still early-stage. The main governance goal is to lock the contract layer now so later growth does not create:
- semantic drift
- broken artifact references
- undocumented framework claims
- incompatible machine-readable examples
