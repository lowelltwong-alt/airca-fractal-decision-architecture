from airca.artifacts import build_markdown_record, to_json
from airca.engine import DecisionEngine
from airca.models import AIRCADecision, AIRCAOption, AIRCARoleAssignment


def build_demo_decision() -> AIRCADecision:
    return AIRCADecision(
        title="Choose what to build next",
        question="Which AIRCA feature should be built first for public adoption?",
        context=(
            "The goal is to make AIRCA easy to understand, easy to try, and useful in GitHub-native workflows."
        ),
        options=[
            AIRCAOption(
                name="Schema + CLI",
                description="Ship a schema, CLI, and example artifacts first.",
                scores={"adoption": 5, "clarity": 5, "difficulty": 4},
                evidence=["Fastest useful MVP", "Easy to demonstrate"],
            ),
            AIRCAOption(
                name="Full orchestration engine",
                description="Build a larger workflow engine before examples and packaging.",
                scores={"adoption": 2, "clarity": 2, "difficulty": 1},
                evidence=["Powerful later", "Too heavy for first release"],
            ),
            AIRCAOption(
                name="Visual app first",
                description="Start with a user interface before artifact stability.",
                scores={"adoption": 3, "clarity": 4, "difficulty": 2},
                evidence=["Good demo potential", "Premature before core format stabilizes"],
            ),
        ],
        roles=AIRCARoleAssignment(
            architect="Lowell T. Wong",
            inform=["GitHub users", "Potential contributors"],
            rank=["Maintainer", "Developer advisor"],
            commit="Lowell T. Wong",
            act=["Repository maintainer"],
        ),
        rationale=(
            "Schema + CLI is the strongest first move because it creates a usable standard, "
            "a fast demo path, and a base for future integrations."
        ),
        action_items=[
            "Finalize schema",
            "Add GitHub Action validation",
            "Create contributor-friendly examples",
        ],
        tags=["mvp", "github", "decision-architecture"],
    )


def main() -> None:
    engine = DecisionEngine()
    decision = engine.choose_best_option(build_demo_decision())

    print(build_markdown_record(decision))
    print()
    print(to_json(decision))


if __name__ == "__main__":
    main()
