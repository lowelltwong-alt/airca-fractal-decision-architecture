from pathlib import Path

from airca.learning import learn_from_artifact, review_artifact
from airca.publish import publish_artifact


def main() -> None:
    artifact_path = Path("examples/artifacts/architecture-decision.json")

    review_artifact(
        artifact_path,
        reviewer="Lowell T. Wong",
        notes="Approved after reviewing risk, maintainability, and onboarding impact.",
        status="approved",
    )

    learn_from_artifact(
        artifact_path,
        signals=[
            "Watch onboarding time for new contributors",
            "Track artifact reuse in future architecture decisions",
            "Review whether human review reduced ambiguity",
        ],
        outcome_summary="Decision prepared for publication and later retrospective review.",
        review_horizon="30 days",
    )

    paper_path, summary_path = publish_artifact(artifact_path, "papers/generated")
    print(f"Generated {paper_path}")
    print(f"Generated {summary_path}")


if __name__ == "__main__":
    main()
