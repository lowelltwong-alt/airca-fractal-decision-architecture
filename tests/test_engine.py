from airca.engine import DecisionEngine
from airca.models import AIRCADecision, AIRCAOption, AIRCARoleAssignment


def test_choose_best_option_sets_committed_status():
    decision = AIRCADecision(
        title="Test Decision",
        question="Which option wins?",
        context="Test context",
        options=[
            AIRCAOption(name="A", description="Option A", scores={"score": 1}),
            AIRCAOption(name="B", description="Option B", scores={"score": 3}),
        ],
        roles=AIRCARoleAssignment(architect="Owner", commit="Owner"),
    )

    engine = DecisionEngine()
    result = engine.choose_best_option(decision)

    assert result.chosen_option == "B"
    assert result.status == "committed"
