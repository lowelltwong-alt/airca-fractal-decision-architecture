# Fractal Artifact Class Naming

This note explains how classes of artifacts should be named in a fractal architecture so that the naming logic itself remains stable, interpretable, and scalable across levels.

The purpose is not simply to make artifact names look tidy. It is to make names carry enough structure that both humans and machines can infer what kind of thing an artifact is, how durable it is, what role it plays, where it sits in the broader architecture, and what kinds of governance or lifecycle expectations apply.

## Why naming matters

Naming is often treated as a superficial layer.

In a machine-readable architecture, it is not.

Names are part of how artifacts become legible across a system. Poor naming introduces several problems:

- category confusion
- retrieval noise
- inconsistent lifecycle handling
- weak governance signaling
- difficulty in grouping similar artifacts
- difficulty in distinguishing durable artifacts from temporary ones
- poor portability across teams, documents, and systems

A fractal naming system is meant to reduce that ambiguity.

## Core claim

Artifact names should encode enough structure to signal at least:

- what kind of artifact this is
- what role it plays
- what level or layer it belongs to
- how durable it is
- what lifecycle treatment applies
- how it relates to other artifact classes

This does not require every filename to be overly long.

It means the naming system should be systematic enough that the architecture remains intelligible as the number of artifacts grows.

## Why this should be fractal

A fractal architecture should not only have recursive content and recursive metadata. It should also have recursive naming logic.

That means the same naming principles should work whether the artifact is:

- an enterprise-level governance artifact
- a workflow-level decision artifact
- a document-level evidence artifact
- a task-level action artifact
- a node inside a larger recursive object

The object changes in scale, but the naming grammar should remain stable.

## What naming should help answer

A useful artifact name should help a reader or system infer questions such as:

- Is this a decision artifact, evidence artifact, policy artifact, taxonomy artifact, or ontology artifact?
- Is it core, working, temporary, archival, or superseded?
- Does it mainly support Architect, Inform, Rank, Commit, or Act?
- Is it meant to persist, refresh, expire, or be retired?
- Is it a top-level artifact or a subnode within a broader structure?

Names do not need to answer all of those alone, but the naming system should align with those distinctions.

## Major naming dimensions

A fractal artifact naming system should usually draw from several dimensions.

### 1. Artifact class

This is the strongest naming anchor.

Examples:
- Decision Artifact
- Evidence Artifact
- Policy Artifact
- Governance Artifact
- Synthesis Artifact
- Taxonomy Artifact
- Ontology Artifact
- Review Artifact
- Ledger Artifact
- Execution Artifact

Artifact class answers:
- what kind of thing this is
- what function it primarily serves

### 2. Artifact tier

Tier helps distinguish importance and durability.

The schema already provides a very useful starting vocabulary here, including values such as:

- first_order_ephemeral
- second_order_core
- master_control
- archive_reference
- superseded_record

These are strong because they carry both structural and lifecycle meaning.

Tier answers:
- how central the artifact is
- how durable it is likely meant to be
- how much governance or review should attach to it

### 3. Durability

Durability helps distinguish how long the artifact is expected to remain useful.

Examples:
- ephemeral
- working
- durable
- persistent
- archival

Durability answers:
- whether the artifact should be treated as short-lived or long-lived
- whether refresh and deletion logic should be aggressive or cautious

### 4. State

State clarifies where the artifact is in its current lifecycle.

Examples:
- draft
- active
- review_due
- stale
- archived
- superseded
- retired

State answers:
- whether the artifact is currently trustworthy
- whether it requires action
- whether it should still be used in active reasoning

### 5. Decision role

Decision role helps connect artifact naming to AIRCA and the broader decision architecture.

Examples:
- Architect
- Inform
- Rank
- Commit
- Act

Decision role answers:
- where this artifact most strongly sits in the decision flow
- how it supports movement from signal to action

Not every artifact must map cleanly to a single AIRCA role, but where it does, naming or metadata should make that visible.

### 6. Level

Level clarifies the scale of the artifact.

Examples:
- enterprise
- function
- team
- workflow
- document
- issue
- task
- node

Level answers:
- where this artifact sits in the architecture
- what scale of governance may apply

## Naming models

There are several possible naming models.

### Model 1: Human-readable class-first naming

Format:

`[Tier] [Class] [Role]`

Examples:
- First-Order Ephemeral Evidence Artifact
- Second-Order Core Decision Artifact
- Master Control Governance Artifact
- Archive Reference Ontology Artifact

This model is readable and good for explanatory documents.

### Model 2: Structured machine-readable naming

Format:

`[level]-[tier]-[class]-[role]-[state]-[version]`

Examples:
- workflow-second_order_core-decision_artifact-rank-active-v1
- document-first_order_ephemeral-evidence_artifact-inform-draft-v1
- enterprise-master_control-governance_artifact-architect-active-v2

This model is stronger for systems and machine parsing.

### Model 3: Hybrid naming

Format:

`[Class] - [Tier] - [Level] - [Role]`

Examples:
- Decision Artifact - Second-Order Core - Workflow - Rank
- Governance Artifact - Master Control - Enterprise - Architect
- Evidence Artifact - First-Order Ephemeral - Document - Inform

This model is good when both human readability and machine alignment matter.

## Recommended class families

A strong fractal architecture will likely need at least the following artifact classes.

### Core architecture classes
- Taxonomy Artifact
- Ontology Artifact
- Decision Artifact
- Governance Artifact
- Policy Artifact

### Support classes
- Evidence Artifact
- Synthesis Artifact
- Review Artifact
- Execution Artifact
- Ledger Artifact

### Lifecycle and control classes
- Archive Reference Artifact
- Superseded Record Artifact
- Master Control Artifact

These can be treated as classes, sub-classes, or tier-class combinations depending on how tightly the architecture is formalized.

## Relationship to taxonomy

Fractal artifact naming is partly a taxonomy problem.

It creates a stable classification layer for artifacts themselves.

Without naming logic, artifact classes can drift, and retrieval becomes inconsistent.

That means naming is not separate from taxonomy.  
It is one of the most visible expressions of taxonomy.

## Relationship to ontology

Naming also interacts with ontology.

Artifact names should not attempt to carry all relational meaning themselves. That is what ontology fields are for.

But names should still help make core distinctions visible so that:
- related artifacts are easier to connect
- artifact roles are easier to interpret
- humans can infer likely relationships before opening the object

So naming supports ontology without replacing it.

## Relationship to decision-making

Naming also supports decision-making.

An artifact that clearly identifies itself as:
- a Decision Artifact
- a Governance Artifact
- a Review Artifact
- an Evidence Artifact

immediately changes how it should be used.

Likewise, durability and state influence decision relevance:
- a stale artifact should not be weighted the same as an active one
- a superseded artifact should not quietly govern present decisions
- a master control artifact should likely carry stronger review and override logic

This means naming is part of how artifacts become decision-ready.

## Relationship to lifecycle

Naming should align with lifecycle but not replace lifecycle fields.

For example:
- the name may indicate that something is archival or superseded
- lifecycle metadata should still carry the authoritative rules for review, refresh, archive, or deletion

The name helps with first-glance interpretation.  
The lifecycle fields govern action.

## Fractal naming principles

This repository should treat the following as naming principles:

### 1. Same grammar, different scale
The same naming logic should work across enterprise, workflow, document, task, and node levels.

### 2. Class before decoration
Artifact names should foreground what kind of thing the object is.

### 3. Durability should be visible
The naming system should make it easier to distinguish temporary from durable artifacts.

### 4. State should be discoverable
Where useful, active/draft/stale/superseded distinctions should be visible or easily derivable.

### 5. Metadata remains authoritative
Names assist interpretation, but machine-readable fields remain the source of truth.

### 6. Naming should reduce ambiguity
If two artifact types would likely be confused, the naming system is not doing enough.

## Minimum naming recommendation

At minimum, every meaningful artifact should have explicit values for:

- artifact class
- artifact tier
- durability
- state

And where relevant:
- decision role
- level

This can live in machine-readable metadata even if the human-facing file name is shorter.

## Example set

Here are examples of how the same naming logic can recur across levels.

### Enterprise level
- Master Control Governance Artifact - Enterprise - Architect
- Second-Order Core Decision Artifact - Enterprise - Commit

### Workflow level
- Second-Order Core Decision Artifact - Workflow - Rank
- First-Order Ephemeral Evidence Artifact - Workflow - Inform

### Document level
- Synthesis Artifact - Document - Inform
- Review Artifact - Document - Commit

### Task level
- Execution Artifact - Task - Act
- Evidence Artifact - Task - Inform

The scale changes, but the naming grammar remains stable.

## Working thesis

Fractal artifact class naming is not merely a cosmetic convention.

It is part of the architecture.

A good naming system helps preserve classification, lifecycle awareness, decision relevance, and interpretability across levels. In a fractal machine-readable environment, names should therefore function as structured signals, not just labels.
