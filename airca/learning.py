from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def review_artifact(input_path: str | Path, reviewer: str, notes: str, status: str = "approved") -> dict[str, Any]:
    path = Path(input_path)
    artifact = json.loads(path.read_text(encoding="utf-8"))
    decision = artifact.setdefault("decision", {})
    metadata = decision.setdefault("metadata", {})
    metadata["human_review"] = {
        "required": True,
        "reviewer": reviewer,
        "status": status,
        "notes": notes,
    }
    path.write_text(json.dumps(artifact, indent=2), encoding="utf-8")
    return artifact


def learn_from_artifact(
    input_path: str | Path,
    signals: list[str],
    outcome_summary: str,
    review_horizon: str = "30 days",
) -> dict[str, Any]:
    path = Path(input_path)
    artifact = json.loads(path.read_text(encoding="utf-8"))
    decision = artifact.setdefault("decision", {})
    metadata = decision.setdefault("metadata", {})
    metadata["learning"] = {
        "review_horizon": review_horizon,
        "signals": signals,
        "outcome_summary": outcome_summary,
    }
    path.write_text(json.dumps(artifact, indent=2), encoding="utf-8")
    return artifact
