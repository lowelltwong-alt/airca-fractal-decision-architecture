from __future__ import annotations

from .models import AIRCADecision, AIRCAOption


class DecisionEngine:
    """Minimal AIRCA engine for ranking and committing decisions."""

    def rank_options(self, decision: AIRCADecision) -> list[AIRCAOption]:
        return sorted(decision.options, key=lambda option: option.total_score, reverse=True)

    def choose_best_option(self, decision: AIRCADecision) -> AIRCADecision:
        ranked = self.rank_options(decision)
        if ranked:
            decision.chosen_option = ranked[0].name
            decision.status = "committed"
        return decision
