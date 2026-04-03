from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class AIRCARoleAssignment:
    architect: str
    inform: list[str] = field(default_factory=list)
    rank: list[str] = field(default_factory=list)
    commit: str = ""
    act: list[str] = field(default_factory=list)


@dataclass
class AIRCAOption:
    name: str
    description: str
    scores: dict[str, float] = field(default_factory=dict)
    evidence: list[str] = field(default_factory=list)

    @property
    def total_score(self) -> float:
        return float(sum(self.scores.values()))


@dataclass
class AIRCADecision:
    title: str
    question: str
    context: str
    options: list[AIRCAOption]
    roles: AIRCARoleAssignment
    decision_id: str = ""
    status: str = "draft"
    chosen_option: str | None = None
    rationale: str = ""
    action_items: list[str] = field(default_factory=list)
    tags: list[str] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)
