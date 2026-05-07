from __future__ import annotations

import argparse
from pathlib import Path

from .artifacts import build_markdown_record, to_json
from .engine import DecisionEngine
from .models import AIRCADecision, AIRCAOption, AIRCARoleAssignment


EXAMPLE_DECISION = AIRCADecision(
    title="Choose architecture decision format",
    question="What format should the team adopt for AI-assisted architecture decisions?",
    context=(
        "The team needs a repeatable way to evaluate options, preserve rationale, "
        "and generate machine-readable records for future review."
    ),
    options=[
        AIRCAOption(
            name="Plain markdown notes",
            description="Use unstructured markdown files with no shared schema.",
            scores={"speed": 5, "governance": 2, "reuse": 2},
            evidence=["Fast to write", "Hard to validate"],
        ),
        AIRCAOption(
            name="AIRCA artifact",
            description="Use AIRCA markdown + JSON artifact generation.",
            scores={"speed": 4, "governance": 5, "reuse": 5},
            evidence=["Structured", "Machine-readable", "Git-friendly"],
        ),
    ],
    roles=AIRCARoleAssignment(
        architect="Lowell T. Wong",
        inform=["Engineering lead", "Product lead"],
        rank=["Engineering lead", "Operations lead"],
        commit="Lowell T. Wong",
        act=["Engineering team"],
    ),
    rationale=(
        "AIRCA artifact generation provides a practical balance of readability, "
        "accountability, and machine-readability."
    ),
    action_items=[
        "Adopt AIRCA template for new architecture decisions",
        "Validate artifacts in pull requests",
    ],
    tags=["architecture", "ai-governance", "decision-record"],
)


def main() -> None:
    parser = argparse.ArgumentParser(description="AIRCA decision tooling")
    parser.add_argument("command", choices=["demo", "init"], help="Command to run")
    parser.add_argument(
        "--output-dir",
        default="output",
        help="Directory where generated artifacts will be written",
    )
    args = parser.parse_args()

    if args.command == "init":
        Path(args.output_dir).mkdir(parents=True, exist_ok=True)
        print(f"Initialized AIRCA workspace at {args.output_dir}")
        return

    engine = DecisionEngine()
    decision = engine.choose_best_option(EXAMPLE_DECISION)

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    markdown_path = output_dir / "decision.md"
    json_path = output_dir / "decision.json"

    markdown_path.write_text(build_markdown_record(decision), encoding="utf-8")
    json_path.write_text(to_json(decision), encoding="utf-8")

    print(f"Generated {markdown_path}")
    print(f"Generated {json_path}")
