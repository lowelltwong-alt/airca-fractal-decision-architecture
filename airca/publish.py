from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def _bullet_list(items: list[str]) -> list[str]:
    if not items:
        return ["- None recorded"]
    return [f"- {item}" for item in items]


def _option_section(options: list[dict[str, Any]]) -> list[str]:
    lines: list[str] = []
    for index, option in enumerate(options, start=1):
        lines.extend(
            [
                f"### Option {index}: {option.get('name', 'Unnamed option')}",
                option.get("description", "No description provided."),
                f"- Total score: {option.get('total_score', 'N/A')}",
                f"- Evidence: {', '.join(option.get('evidence', [])) or 'None recorded'}",
                "",
            ]
        )
    return lines


def _criteria_section(options: list[dict[str, Any]]) -> list[str]:
    criteria: set[str] = set()
    for option in options:
        criteria.update(option.get("scores", {}).keys())
    if not criteria:
        return ["- No explicit criteria recorded"]
    return [f"- {criterion}" for criterion in sorted(criteria)]


def build_white_paper(artifact: dict[str, Any]) -> str:
    decision = artifact.get("decision", {})
    options = decision.get("options", [])
    metadata = decision.get("metadata", {})
    learning = metadata.get("learning", {})
    human_review = metadata.get("human_review", {})

    lines = [
        f"# Decision Paper: {decision.get('title', 'Untitled Decision')}",
        "",
        "## Abstract",
        (
            "This paper documents a structured AIRCA decision and converts it into a "
            "public-facing record that can be reviewed, reused, and improved over time."
        ),
        "",
        "## Problem",
        decision.get("question", "No decision question recorded."),
        "",
        "## Context",
        decision.get("context", "No context recorded."),
        "",
        "## Options Considered",
    ]

    lines.extend(_option_section(options))
    lines.extend([
        "## Evaluation Criteria",
        *_criteria_section(options),
        "",
        "## Decision",
        decision.get("chosen_option") or "No final choice recorded.",
        "",
        "## Rationale",
        decision.get("rationale") or "No rationale recorded.",
        "",
        "## AIRCA Roles",
        f"- Architect: {decision.get('roles', {}).get('architect', 'None recorded')}",
        f"- Inform: {', '.join(decision.get('roles', {}).get('inform', [])) or 'None recorded'}",
        f"- Rank: {', '.join(decision.get('roles', {}).get('rank', [])) or 'None recorded'}",
        f"- Commit: {decision.get('roles', {}).get('commit', 'None recorded')}",
        f"- Act: {', '.join(decision.get('roles', {}).get('act', [])) or 'None recorded'}",
        "",
        "## Implications",
    ])

    lines.extend(_bullet_list(decision.get("action_items", [])))
    lines.extend([
        "",
        "## Human Review",
        f"- Required: {human_review.get('required', False)}",
        f"- Reviewer: {human_review.get('reviewer', 'Not assigned')}",
        f"- Status: {human_review.get('status', 'not-reviewed')}",
        f"- Notes: {human_review.get('notes', 'No review notes recorded')}",
        "",
        "## Future Review",
        learning.get("review_horizon", "No review horizon recorded."),
        "",
        "## Learning Signals",
    ])
    lines.extend(_bullet_list(learning.get("signals", [])))
    lines.extend([
        "",
        "## Assumptions",
    ])
    lines.extend(_bullet_list(metadata.get("assumptions", [])))
    lines.extend([
        "",
        "## Uncertainties",
    ])
    lines.extend(_bullet_list(metadata.get("uncertainties", [])))
    lines.extend([
        "",
        "## Publication Notes",
        "This white-paper-style document was generated from an AIRCA decision artifact.",
        "",
    ])
    return "\n".join(lines)


def publish_artifact(input_path: str | Path, output_dir: str | Path = "papers/generated") -> tuple[Path, Path]:
    input_file = Path(input_path)
    artifact = json.loads(input_file.read_text(encoding="utf-8"))
    decision = artifact.get("decision", {})
    decision_id = decision.get("id") or decision.get("title", "decision").lower().replace(" ", "-")

    output_directory = Path(output_dir)
    output_directory.mkdir(parents=True, exist_ok=True)

    paper_path = output_directory / f"{decision_id}.md"
    summary_path = output_directory / f"{decision_id}-summary.md"

    paper = build_white_paper(artifact)
    summary = "\n".join([
        f"# Summary: {decision.get('title', 'Untitled Decision')}",
        "",
        f"- Chosen option: {decision.get('chosen_option', 'None recorded')}",
        f"- Status: {decision.get('status', 'unknown')}",
        f"- Review horizon: {decision.get('metadata', {}).get('learning', {}).get('review_horizon', 'None recorded')}",
        f"- Human reviewer: {decision.get('metadata', {}).get('human_review', {}).get('reviewer', 'None recorded')}",
    ])

    paper_path.write_text(paper, encoding="utf-8")
    summary_path.write_text(summary, encoding="utf-8")
    return paper_path, summary_path
