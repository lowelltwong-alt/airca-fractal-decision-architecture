# AIRCA Framework Core Schema Specification

This file defines the starter contract for the root `framework/` package.

## Purpose

The framework package is the executable spine of the repository's claim that decision architecture should be:
- legible
- governable
- machine-readable
- extensible across domains

The core stays domain-neutral.
Extension packs add theological or secular specialization without changing the core object model.

## Core classes

### 1. QuestionTopic
The issue, question, problem, or bounded decision object under consideration.

Required fields:
- `id`
- `label`
- `description`

### 2. ViewPosition
A candidate interpretation, proposal, tradition-scoped view, policy option, or stance relevant to a question.

Required fields:
- `id`
- `label`
- `position_type`

### 3. Assessment
An evaluation of a view or question under explicit criteria.

Required fields:
- `id`
- `label`
- `assessment_type`
- `score`

### 4. Assertion
A sourced claim attached to a view, assessment, or question.

Required fields:
- `id`
- `label`
- `source_ref`

### 5. CoherenceState
A machine-readable summary of fit, tension, contradiction, or reinforcement across a cluster of positions and assertions.

Required fields:
- `id`
- `label`
- `coherence_score`

## Core edge families

- `addresses_question` — a view addresses a question
- `supports` — an assertion or assessment supports a view
- `challenges` — an assertion or assessment challenges a view
- `assesses` — an assessment evaluates a target node
- `depends_on` — a view or assertion depends on another node
- `coheres_with` — positive coherence signal
- `conflicts_with` — negative coherence signal
- `summarizes_state` — a coherence object summarizes a cluster

## Design rules

1. **Questions are not views.**
2. **Views are not evidence.**
3. **Assertions must be sourceable.**
4. **Coherence is computed or curated state, not raw doctrine.**
5. **Extension packs add fields and edge types, but should not collapse these distinctions.**

## Extension packs

### Religious extension
Adds:
- tradition
- authority source
- canon boundary
- doctrinal cluster
- confession / catechism / council references

### Secular extension
Adds:
- policy regime
- stakeholder
- regulation / standard references
- risk and control metadata

## Validation

The starter SHACL file in `framework/validation/shacl/core.shacl.ttl` enforces a minimal contract:
- labels are present
- key class-specific fields are present
- assertion objects carry source references

## Examples

- `framework/examples/religious-justification.ttl`
- `framework/examples/secular-ai-safety.ttl`

These examples are intentionally small.
They exist to prove the starter contract works and to give future contributors a pattern to extend.
