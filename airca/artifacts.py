from __future__ import annotations

from datetime import datetime, UTC
import json

from .models import AIRCADecision


SCHEMA_VERSION = "0.1.0"


def build_artifact(decision: AIRCADecision) -> dict:
    return {
        "schema_version": SCHEMA_VERSION,
        "generated_at": datetime.now(UTC).isoformat(),
        "decision": {
            "id": decision.decision_id or decision.title.lower().replace(" ", "-"),
            "title": decision.title,
            "question": decision.question,
            "context": decision.context,
            "status": decision.status,
            "chosen_option": decision.chosen_option,
            "rationale": decision.rationale,
            "action_items": decision.action_items,
            "tags": decision.tags,
            "roles": {
                "architect": decision.roles.architect,
                "inform": decision.roles.inform,
                "rank": decision.roles.rank,
                "commit": decision.roles.commit,
                "act": decision.roles.act,
            },
            "options": [
                {
                    "name": option.name,
                    "description": option.description,
                    "scores": option.scores,
                    "total_score": option.total_score,
                    "evidence": option.evidence,
                }
                for option in decision.options
            ],
            "metadata": decision.metadata,
        },
    }


def build_markdown_record(decision: AIRCADecision) -> str:
    lines = [
        f"# {decision.title}",
        "",
        f"**Question:** {decision.question}",
        f"**Status:** {decision.status}",
        f"**Chosen option:** {decision.chosen_option or 'TBD'}",
        "",
        "## Context",
        decision.context,
        "",
        "## AIRCA Roles",
        f"- Architect: {decision.roles.architect}",
        f"- Inform: {', '.join(decision.roles.inform) or 'None'}",
        f"- Rank: {', '.join(decision.roles.rank) or 'None'}",
        f"- Commit: {decision.roles.commit or 'None'}",
        f"- Act: {', '.join(decision.roles.act) or 'None'}",
        "",
        "## Options",
    ]

    for option in decision.options:
        lines.extend(
            [
                f"### {option.name}",
                option.description,
                f"- Total score: {option.total_score}",
                f"- Evidence: {', '.join(option.evidence) or 'None'}",
                "",
            ]
        )

    lines.extend(
        [
            "## Rationale",
            decision.rationale or "TBD",
            "",
            "## Action Items",
        ]
    )

    if decision.action_items:
        lines.extend([f"- {item}" for item in decision.action_items])
    else:
        lines.append("- None yet")

    return "\n".join(lines)


def to_json(decision: AIRCADecision) -> str:
    return json.dumps(build_artifact(decision), indent=2)
