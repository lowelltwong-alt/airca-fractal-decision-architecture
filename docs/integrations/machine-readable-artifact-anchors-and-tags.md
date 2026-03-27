# Machine-Readable Artifact Anchors and Tags

This note explains what kinds of anchors, tags, and embedded fields should exist inside machine-readable artifacts if the broader architecture is meant to remain stable, governable, and reusable across levels.

It builds on the schema logic already established elsewhere in this repository: recursive nodes, stable field families, controlled vocabulary, lifecycle logic, inheritance logic, and interpretation rules. The schema materials already define the move from flat sections to recursive nodes and recommend keeping the recursive skeleton fixed while changing values, tags, roles, relationships, and subnodes as needed. :contentReference[oaicite:0]{index=0} :contentReference[oaicite:1]{index=1}

## Why this matters

A machine-readable artifact is not useful merely because it is stored as JSON.

It becomes useful when its internal structure makes it possible to answer questions such as:

- what is this artifact
- what kind of thing is it
- what does it relate to
- what decision does it support
- how durable is it
- when should it be reviewed
- what can an agent do with it
- what requires human approval
- how should blank or missing values be interpreted

Without those anchors and tags, the artifact may still be machine-readable in a narrow technical sense, but it will not be reliably interpretable, governable, or reusable.

## Core claim

Machine-readable artifacts should carry enough embedded structure to preserve:

- identity
- classification
- relationships
- decision logic
- execution relevance
- governance
- evidence
- provenance
- lifecycle
- inheritance
- interpretation rules

The v2 schema already defines these as stable field families and treats them as reusable containers rather than one-off document sections. :contentReference[oaicite:2]{index=2} :contentReference[oaicite:3]{index=3}

## What an anchor is

In this repository, an **anchor** is a field or field-group that helps stabilize interpretation across artifacts and across levels.

An anchor is not just metadata. It is part of what makes the artifact legible.

Examples:
- an `identity.id` anchors uniqueness
- an `identity.anchor` anchors addressability
- a `classification.document_type` anchors category
- a `system.system_role` anchors function
- a `logic.decision_type` anchors decision semantics
- a `lifecycle.artifact_tier` anchors durability and review expectations

Anchors reduce ambiguity.

## What a tag is

A **tag** is a lighter-weight classifier or retrieval signal.

Tags are useful, but they should not replace stronger structural anchors.

For example:
- tags can improve retrieval
- tags can improve clustering
- tags can improve discovery and filtering
- tags can express themes or audiences
- tags can support machine ranking

But tags alone are weaker than formal field placement.

So the general rule should be:

**Prefer anchors for stable meaning. Prefer tags for flexible retrieval and grouping.**

## Primary anchor families

The schema already provides the main anchor families.

### 1. Identity anchors

Identity fields answer:
- which artifact is this
- how is it named
- how can it be referenced
- what version is this
- what status is it in

Core examples already present in the template:
- `identity.id`
- `identity.anchor`
- `identity.title`
- `identity.slug`
- `identity.version`
- `identity.status` :contentReference[oaicite:4]{index=4}

These should exist in every meaningful node.

### 2. Classification anchors

Classification fields answer:
- what kind of artifact is this
- what domain is it in
- what object type is it
- who is it for
- what kinds of retrieval or grouping apply

Core examples already present:
- `classification.document_type`
- `classification.primary_use`
- `classification.domain`
- `classification.subdomain`
- `classification.object_type`
- `classification.tags`
- `classification.audience_tags`
- `classification.source_domains` :contentReference[oaicite:5]{index=5}

These are the main taxonomy layer.

### 3. System anchors

System fields answer:
- what role this node plays in the larger system
- what it is meant to do
- how AI should interact with it
- whether human judgment is required

Core examples already present:
- `system.system_role`
- `system.intent`
- `system.author_logic`
- `system.ai_compatibility`
- `system.interaction_mode`
- `system.requires_human_judgment` :contentReference[oaicite:6]{index=6}

The schema also recommends stable controlled vocabulary for `system_role`, including values like `taxonomy_layer`, `ontology_layer`, `decision_layer`, `governance_layer`, `evidence_layer`, and `persistence_layer`. :contentReference[oaicite:7]{index=7}

### 4. Relationship anchors

Relationship fields answer:
- what this artifact depends on
- what it enables
- what its parent and child nodes are
- what other objects it relates to
- whether it supersedes or is superseded

Core examples already present:
- `relationships.parent`
- `relationships.parents`
- `relationships.children`
- `relationships.depends_on`
- `relationships.enables`
- `relationships.related_to`
- `relationships.supersedes`
- `relationships.superseded_by`
- `relationships.relationship_metadata.*` :contentReference[oaicite:8]{index=8}

These are the main ontology layer.

### 5. Logic anchors

Logic fields answer:
- what decision or reasoning this artifact supports
- which inputs and outputs matter
- what constraints apply
- what assumptions are in play
- what tradeoffs exist
- what criteria define success

Core examples already present:
- `logic.inputs`
- `logic.outputs`
- `logic.decision_type`
- `logic.output_type`
- `logic.constraints`
- `logic.assumptions`
- `logic.tradeoffs`
- `logic.evaluation_criteria`
- `logic.success_metrics` :contentReference[oaicite:9]{index=9}

The schema also recommends controlled vocabulary for `decision_type` and `output_type`, including values such as `prioritization`, `governance`, `risk_assessment`, `tradeoff_map`, `decision_ledger_entry`, `taxonomy_entry`, and `ontology_object`. :contentReference[oaicite:10]{index=10}

### 6. Execution anchors

Execution fields answer:
- what should happen because of this artifact
- what the recommended next actions are
- what AI prompts or human instructions are attached
- what risks and mitigations exist

Core examples already present:
- `execution.recommended_actions`
- `execution.ai_prompt_template`
- `execution.human_instructions`
- `execution.implementation_notes`
- `execution.risks`
- `execution.mitigations` :contentReference[oaicite:11]{index=11}

### 7. Governance anchors

Governance fields answer:
- who owns this
- who reviews it
- what decision rights attach to it
- whether approval is required
- what sensitivity and retention rules apply

Core examples already present:
- `governance.owner`
- `governance.reviewers`
- `governance.decision_rights`
- `governance.approval_required`
- `governance.review_cycle`
- `governance.sensitivity`
- `governance.retention_guidance` :contentReference[oaicite:12]{index=12}

### 8. Evidence anchors

Evidence fields answer:
- what supports this artifact
- where the information came from
- how confident the system is
- what kind of confidence decomposition exists

Core examples already present:
- `evidence.citations`
- `evidence.data_sources`
- `evidence.confidence`
- `evidence.confidence_notes`
- `evidence.confidence_model.*` :contentReference[oaicite:13]{index=13}

The v2 schema explicitly expands confidence into subfields such as evidence quality, source freshness, completeness, model confidence, human review status, and confidence rationale. :contentReference[oaicite:14]{index=14}

### 9. Persistence anchors

Persistence fields answer:
- what durable decision memory should be carried forward
- what problem was being solved
- what options were considered
- what criteria were used
- what decision was made
- what outcome was expected and what outcome actually occurred

Core examples already present:
- `persistence.decision_ledger_entry.problem`
- `persistence.decision_ledger_entry.options_considered`
- `persistence.decision_ledger_entry.criteria_used`
- `persistence.decision_ledger_entry.decision_made`
- `persistence.decision_ledger_entry.expected_outcome`
- `persistence.decision_ledger_entry.actual_outcome`
- `persistence.decision_ledger_entry.follow_up_date` :contentReference[oaicite:15]{index=15}

This is one of the strongest AIRCA-adjacent bridges in the schema. The AIRCA materials also describe Commit as the human accountability hinge and argue that durable decision records should capture what signals were surfaced, what options were narrowed, who committed, under what criteria, and what action followed. :contentReference[oaicite:16]{index=16}

### 10. Content anchors

Content fields answer:
- what the human-readable layer actually says
- what summary and body exist
- what examples or attachments exist

Core examples already present:
- `content.summary`
- `content.body`
- `content.attachments`
- `content.examples` :contentReference[oaicite:17]{index=17}

### 11. Time anchors

Time fields answer:
- when the artifact was created
- when it was updated
- when it becomes effective
- when it should be reviewed
- when it expires

Core examples already present:
- `time.created_at`
- `time.updated_at`
- `time.effective_date`
- `time.review_date`
- `time.expires_at` :contentReference[oaicite:18]{index=18}

### 12. Permissions anchors

Permissions fields answer:
- who can see the artifact
- who should not see it
- what an agent may or may not do with it
- where human signoff is required

Core examples already present:
- `permissions.visibility`
- `permissions.allowed_audiences`
- `permissions.restricted_audiences`
- `permissions.usage_notes`
- `permissions.action_permissions.*` :contentReference[oaicite:19]{index=19}

The v2 template explicitly includes agent rights such as `agent_may_read`, `agent_may_summarize`, `agent_may_tag`, `agent_may_propose_edits`, while keeping destructive actions and structural changes gated behind human approval. :contentReference[oaicite:20]{index=20}

### 13. Provenance anchors

Provenance fields answer:
- where this artifact came from
- who created it
- how it has been transformed
- what sources or processes shaped it
- what the human/AI authoring mix was

Core examples already present:
- `provenance.source_refs`
- `provenance.derived_from`
- `provenance.created_by`
- `provenance.last_modified_by`
- `provenance.transformation_history`
- `provenance.derivation_method`
- `provenance.process_refs`
- `provenance.authoring_mix.*` :contentReference[oaicite:21]{index=21}

### 14. Validation anchors

Validation fields answer:
- what fields are required
- what rules must hold
- what checks should run
- how fit and interpretation should be assessed

Core examples already present:
- `validation.required_fields`
- `validation.field_rules`
- `validation.status_checks`
- `validation.fit_notes`
- `validation.interpretation_checks` :contentReference[oaicite:22]{index=22}

### 15. Entity-model anchors

Entity-model fields answer:
- what entity this artifact or node corresponds to
- what its canonical identity is
- what state and status it holds in a broader ontology

Core examples already present:
- `entity_model.entity_type`
- `entity_model.entity_subtype`
- `entity_model.canonical_id`
- `entity_model.lifecycle_state`
- `entity_model.canonical_status`
- `entity_model.source_of_truth_ref`
- `entity_model.aliases` :contentReference[oaicite:23]{index=23}

### 16. Lifecycle anchors

Lifecycle fields answer:
- how durable this artifact is meant to be
- when it should be reviewed
- when it becomes stale
- whether it should be archived, superseded, or deleted
- what human approval gates exist
- what the next human action should be

Core examples already present:
- `lifecycle.artifact_tier`
- `lifecycle.artifact_class`
- `lifecycle.durability`
- `lifecycle.state`
- `lifecycle.last_reviewed_at`
- `lifecycle.next_review_due`
- `lifecycle.refresh_interval_days`
- `lifecycle.staleness_rule`
- `lifecycle.disposition_recommendation`
- `lifecycle.archive_after`
- `lifecycle.delete_after`
- `lifecycle.deletion_allowed`
- `lifecycle.human_approval_required_for_delete`
- `lifecycle.human_approval_required_for_archive`
- `lifecycle.human_approval_required_for_supersession`
- `lifecycle.protected_from_autonomous_deletion`
- `lifecycle.next_human_action` :contentReference[oaicite:24]{index=24}

The schema explicitly treats lifecycle as a fractal layer that should appear at every meaningful node, not only at the top artifact level. :contentReference[oaicite:25]{index=25}

### 17. Inheritance anchors

Inheritance fields answer:
- what defaults flow downward
- which fields are never inherited
- what children may override
- whether stricter controls win
- when local overrides require human approval

Core examples already present:
- `inheritance.inherits_from_parent_by_default`
- `inheritance.inherit_if_blank`
- `inheritance.fields_never_inherited`
- `inheritance.child_may_override`
- `inheritance.parent_protection_flows_down`
- `inheritance.stricter_child_controls_allowed`
- `inheritance.looser_child_controls_require_human_approval`
- `inheritance.conflict_resolution_rule` :contentReference[oaicite:26]{index=26}

### 18. Interpretation anchors

Interpretation fields answer:
- how to read missing values
- how to read blank values
- what explicit false means
- what explicit true means
- whether blank values are behaviorally dormant
- whether blank values can ever imply destructive permission

Core examples already present:
- `interpretation_rules.missing_field_means`
- `interpretation_rules.empty_value_means`
- `interpretation_rules.explicit_false_means`
- `interpretation_rules.explicit_true_means`
- `interpretation_rules.never_infer_destructive_action_from_blank`
- `interpretation_rules.blank_fields_are_behaviorally_dormant_until_populated` :contentReference[oaicite:27]{index=27}

This is one of the most important v2 additions because it prevents agents from treating dormant or reserved blanks as active instructions. The schema explicitly states that blank values must never imply destructive permission. :contentReference[oaicite:28]{index=28}

## Tag strategy

Tags should be structured, not random.

A good tagging system for this architecture should include at least:

### Topical tags
Examples:
- ai-governance
- decision-intelligence
- ontology
- taxonomy
- legal-ops
- workflow-redesign

### Audience tags
Examples:
- cino
- cfo
- coo
- managing_partner
- legal_ops
- innovation

### Decision tags
Examples:
- prioritization
- governance
- risk_assessment
- implementation_choice

### Layer tags
Examples:
- taxonomy_layer
- ontology_layer
- decision_layer
- persistence_layer
- governance_layer

### Lifecycle tags
Examples:
- draft
- active
- review_due
- stale
- archived
- superseded
- retired

### Durability / tier tags
Examples:
- first_order_ephemeral
- second_order_core
- master_control
- archive_reference
- superseded_record :contentReference[oaicite:29]{index=29}

## Recommended anchor hierarchy

If an artifact cannot support every field at once, prioritize anchors in this order:

1. identity
2. classification
3. system
4. relationships
5. logic
6. governance
7. lifecycle
8. provenance
9. permissions
10. evidence
11. persistence
12. interpretation_rules

That priority closely tracks the schema’s fit order, which says new things should first be modeled as nodes, then fit into existing field families, then only later create new optional field groups. :contentReference[oaicite:30]{index=30}

## Minimum viable machine-readable artifact

At minimum, a reusable artifact should usually contain:

- identity
- classification
- system role
- key relationships
- logic
- governance owner
- lifecycle state
- permissions
- provenance
- summary/body

Without those, machine readability may exist syntactically but remain weak semantically.

## Safety rule

The single most important safety rule is this:

**Blank values must never imply destructive permission.**

The schema repeats this in both validation and interpretation guidance, and the repo should treat it as a non-negotiable design rule. :contentReference[oaicite:31]{index=31} :contentReference[oaicite:32]{index=32}

## Working thesis

Anchors and tags are not decorative metadata.

They are part of what makes a machine-readable artifact stable, interpretable, governable, and reusable across levels.

In a fractal architecture, that means anchors and tags must not only help with retrieval. They must preserve the meaning, role, lifecycle, and decision relevance of the artifact wherever it appears.

## Attribution note

This note reflects repository development by Lowell T. Wong on machine-readable artifact design, fractal taxonomy, ontology, and decision architecture.
