# Example Machine-Readable Artifact

This note shows what a machine-readable artifact can look like when the repository’s core ideas are carried together in one structured object.

The goal is not to present a final schema implementation. The goal is to make the architecture concrete.

This example brings together:

- fractal taxonomy
- fractal ontology
- fractal decision-making
- AIRCA as decision spine
- lifecycle logic
- inheritance logic
- interpretation and safety rules
- machine-readable anchors and tags
- artifact class naming

## Why this example matters

A conceptual architecture becomes easier to understand once it is shown in object form.

This example is meant to demonstrate how one artifact can encode:

- what it is
- where it fits
- what it relates to
- what decision it supports
- what should happen next
- who owns it
- how durable it is
- what an agent may and may not do with it

## Example artifact

```json
{
  "identity": {
    "id": "workflow-decision-rank-001",
    "anchor": "intake-automation-prioritization",
    "title": "Workflow Decision Artifact - Intake Automation Prioritization",
    "slug": "workflow-decision-intake-automation-prioritization",
    "version": "0.1.0",
    "status": "active"
  },
  "classification": {
    "document_type": "decision_artifact",
    "primary_use": "prioritization",
    "domain": "legal_operations",
    "subdomain": "workflow_design",
    "object_type": "workflow_decision_node",
    "tags": [
      "ai-governance",
      "decision-intelligence",
      "workflow-redesign",
      "prioritization"
    ],
    "audience_tags": [
      "cino",
      "coo",
      "legal_ops"
    ],
    "source_domains": [
      "operations",
      "governance",
      "workflow"
    ]
  },
  "system": {
    "system_role": "decision_layer",
    "intent": "rank_and_support_commitment",
    "author_logic": "human_led_ai_assisted",
    "ai_compatibility": "high",
    "interaction_mode": "human_commit_required",
    "requires_human_judgment": true
  },
  "relationships": {
    "parent": "workflow-governance-node",
    "parents": [
      "intake-automation-program"
    ],
    "children": [
      "vendor-evaluation-subnode",
      "change-management-subnode"
    ],
    "depends_on": [
      "current-intake-map",
      "claims-volume-analysis",
      "staff-capacity-review"
    ],
    "enables": [
      "workflow-standardization-plan",
      "pilot-implementation-decision"
    ],
    "related_to": [
      "ocg-parsing-initiative",
      "matter-intake-modernization"
    ],
    "supersedes": [],
    "superseded_by": [],
    "relationship_metadata": {
      "upstream_of": [
        "pilot-approval"
      ],
      "downstream_of": [
        "workflow-assessment"
      ]
    }
  },
  "logic": {
    "inputs": [
      "current state workflow analysis",
      "estimated manual effort",
      "AI fit assessment",
      "governance constraints"
    ],
    "outputs": [
      "ranked implementation options",
      "recommended next action"
    ],
    "decision_type": "prioritization",
    "output_type": "decision_ledger_entry",
    "constraints": [
      "human review required before deployment",
      "budget constraints",
      "process disruption tolerance"
    ],
    "assumptions": [
      "current intake process has repeatable structure",
      "staff adoption risk is moderate",
      "automation should not outrun governance"
    ],
    "tradeoffs": [
      "speed vs. review quality",
      "automation gain vs. change fatigue",
      "local workflow optimization vs. enterprise standardization"
    ],
    "evaluation_criteria": [
      "operational value",
      "risk reduction",
      "human review burden",
      "implementation complexity"
    ],
    "success_metrics": [
      "reduced intake cycle time",
      "reduced manual rework",
      "higher consistency in matter intake decisions"
    ]
  },
  "execution": {
    "recommended_actions": [
      "pilot one intake sub-process first",
      "require human review at commit stage",
      "review results after 30 days"
    ],
    "ai_prompt_template": "Compare workflow options against constraints, rank viable paths, and identify which choice most deserves human commitment.",
    "human_instructions": "Review ranked options, confirm constraints, and approve or reject the pilot path.",
    "implementation_notes": [
      "start with a narrow workflow slice",
      "do not automate exception handling in v1"
    ],
    "risks": [
      "premature automation",
      "false confidence from incomplete workflow data"
    ],
    "mitigations": [
      "human approval gate",
      "30-day review checkpoint"
    ]
  },
  "governance": {
    "owner": "Lowell Wong",
    "reviewers": [
      "operations lead",
      "innovation lead"
    ],
    "decision_rights": "human_commit_required",
    "approval_required": true,
    "review_cycle": "30_days",
    "sensitivity": "internal",
    "retention_guidance": "retain while active and review before archival"
  },
  "evidence": {
    "citations": [],
    "data_sources": [
      "workflow interviews",
      "process maps",
      "internal operational metrics"
    ],
    "confidence": "moderate",
    "confidence_notes": "Strong enough for pilot recommendation, not yet strong enough for enterprise rollout.",
    "confidence_model": {
      "evidence_quality": "moderate",
      "source_freshness": "high",
      "completeness": "partial",
      "model_confidence": "moderate",
      "human_review_status": "reviewed",
      "confidence_rationale": "Signal is directionally strong but not yet complete."
    }
  },
  "persistence": {
    "decision_ledger_entry": {
      "problem": "Which intake automation path should be prioritized first?",
      "options_considered": [
        "full workflow automation",
        "partial automation with review gates",
        "manual optimization only"
      ],
      "criteria_used": [
        "operational value",
        "risk reduction",
        "implementation complexity"
      ],
      "decision_made": "prioritize partial automation with review gates",
      "expected_outcome": "Reduce intake cycle time while preserving accountability.",
      "actual_outcome": null,
      "follow_up_date": "2026-04-27"
    }
  },
  "content": {
    "summary": "This artifact supports a ranking decision on intake automation options and recommends a pilot-first path with human commitment retained at the decision point.",
    "body": "The artifact evaluates multiple automation pathways for intake and supports a ranked choice under governance and operational constraints.",
    "attachments": [],
    "examples": [
      "pilot-first workflow modernization",
      "ranked decision support under constraints"
    ]
  },
  "time": {
    "created_at": "2026-03-27",
    "updated_at": "2026-03-27",
    "effective_date": "2026-03-27",
    "review_date": "2026-04-27",
    "expires_at": null
  },
  "permissions": {
    "visibility": "internal",
    "allowed_audiences": [
      "innovation",
      "operations",
      "leadership"
    ],
    "restricted_audiences": [],
    "usage_notes": "Safe for internal decision support. Not a substitute for final human approval.",
    "action_permissions": {
      "agent_may_read": true,
      "agent_may_summarize": true,
      "agent_may_tag": true,
      "agent_may_propose_edits": true,
      "agent_may_delete": false,
      "agent_may_archive": false,
      "agent_may_change_structure": false
    }
  },
  "provenance": {
    "source_refs": [
      "workflow-review-2026-q1"
    ],
    "derived_from": [
      "current-intake-analysis"
    ],
    "created_by": "Lowell Wong",
    "last_modified_by": "Lowell Wong",
    "transformation_history": [
      "initial draft from workflow analysis",
      "structured into machine-readable decision artifact"
    ],
    "derivation_method": "human-authored with machine-readable structuring",
    "process_refs": [
      "airca-informed workflow design"
    ],
    "authoring_mix": {
      "human_primary": true,
      "ai_assisted": true
    }
  },
  "validation": {
    "required_fields": [
      "identity.id",
      "identity.title",
      "classification.document_type",
      "system.system_role",
      "governance.owner",
      "lifecycle.state"
    ],
    "field_rules": [
      "decision artifacts must include logic.decision_type",
      "artifacts requiring commitment must preserve human approval requirements"
    ],
    "status_checks": [
      "review cycle assigned",
      "owner assigned",
      "permissions checked"
    ],
    "fit_notes": "Fits current recursive artifact pattern without requiring schema expansion.",
    "interpretation_checks": [
      "blank values do not imply permission",
      "null actual outcome means follow-up still pending"
    ]
  },
  "entity_model": {
    "entity_type": "artifact",
    "entity_subtype": "decision_artifact",
    "canonical_id": "workflow-decision-rank-001",
    "lifecycle_state": "active",
    "canonical_status": "usable_with_human_commit_gate",
    "source_of_truth_ref": "this_artifact",
    "aliases": [
      "intake automation prioritization artifact"
    ]
  },
  "lifecycle": {
    "artifact_tier": "second_order_core",
    "artifact_class": "decision_artifact",
    "durability": "durable",
    "state": "active",
    "last_reviewed_at": "2026-03-27",
    "next_review_due": "2026-04-27",
    "refresh_interval_days": 30,
    "staleness_rule": "stale if not reviewed by next_review_due",
    "disposition_recommendation": "review_for_refresh_before_archive",
    "archive_after": null,
    "delete_after": null,
    "deletion_allowed": false,
    "human_approval_required_for_delete": true,
    "human_approval_required_for_archive": true,
    "human_approval_required_for_supersession": true,
    "protected_from_autonomous_deletion": true,
    "next_human_action": "review pilot results and confirm whether to refresh, supersede, or expand scope"
  },
  "inheritance": {
    "inherits_from_parent_by_default": true,
    "inherit_if_blank": true,
    "fields_never_inherited": [
      "identity.id",
      "identity.title",
      "time.created_at"
    ],
    "child_may_override": [
      "classification.tags",
      "execution.implementation_notes"
    ],
    "parent_protection_flows_down": true,
    "stricter_child_controls_allowed": true,
    "looser_child_controls_require_human_approval": true,
    "conflict_resolution_rule": "prefer stricter control unless human-approved override exists"
  },
  "interpretation_rules": {
    "missing_field_means": "not used on this node",
    "empty_value_means": "reserved but not yet populated",
    "explicit_false_means": "explicitly not allowed or not present",
    "explicit_true_means": "explicitly present or allowed",
    "never_infer_destructive_action_from_blank": true,
    "blank_fields_are_behaviorally_dormant_until_populated": true
  }
}
