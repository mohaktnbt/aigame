"""
DistributionCalculator — Computes probability distributions over outcomes
for a given action in the current world state.
"""

from __future__ import annotations

from typing import Any

import numpy as np
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class OutcomeProbability(BaseModel):
    """A single outcome with its probability."""
    outcome: str
    probability: float
    impact_description: str


class DistributionResult(BaseModel):
    """Full probability distribution over outcomes."""
    action: str
    outcomes: list[OutcomeProbability]
    entropy: float  # Shannon entropy of the distribution
    most_likely: str
    confidence: float


class DistributionCalculator:
    """Calculates probability distributions for actions in context.

    Given an action, the current world state, and agent attitudes, the
    calculator produces a probability distribution over possible outcomes.
    This is used for decision support, risk assessment, and scenario
    planning.

    TODO: Use Bayesian network for structured causal reasoning.
    TODO: Incorporate historical outcome data for calibration.
    TODO: Weight agent influence in outcome determination.
    """

    def _softmax(self, scores: list[float]) -> list[float]:
        """Convert raw scores to a probability distribution."""
        arr = np.array(scores)
        exp_arr = np.exp(arr - np.max(arr))
        return (exp_arr / exp_arr.sum()).tolist()

    def calculate(
        self,
        action: str,
        world_state: dict[str, Any],
        agent_states: list[dict[str, Any]] | None = None,
    ) -> DistributionResult:
        """Calculate probability distribution over outcomes.

        Args:
            action: Description of the proposed action.
            world_state: Current world state parameters.
            agent_states: Optional list of agent state summaries.

        Returns:
            DistributionResult with ranked outcomes and probabilities.

        TODO: Replace stub outcomes with LLM-generated possibilities.
        TODO: Use world_state and agent_states for conditional probabilities.
        """
        # STUB: generate placeholder outcomes
        stub_outcomes = [
            ("Success with strong support", 2.0, "Action succeeds and gains popular support"),
            ("Partial success", 1.5, "Action partially achieves goals with mixed reception"),
            ("Neutral outcome", 0.5, "Action has minimal impact"),
            ("Backlash", -0.5, "Action provokes opposition and unrest"),
            ("Failure", -1.5, "Action fails and destabilizes the situation"),
        ]

        raw_scores = [s[1] for s in stub_outcomes]
        probabilities = self._softmax(raw_scores)

        outcomes = [
            OutcomeProbability(
                outcome=name,
                probability=round(prob, 4),
                impact_description=desc,
            )
            for (name, _, desc), prob in zip(stub_outcomes, probabilities)
        ]

        # Shannon entropy
        probs_arr = np.array(probabilities)
        entropy = float(-np.sum(probs_arr * np.log2(probs_arr + 1e-10)))

        most_likely = max(outcomes, key=lambda o: o.probability)

        return DistributionResult(
            action=action,
            outcomes=outcomes,
            entropy=round(entropy, 4),
            most_likely=most_likely.outcome,
            confidence=round(1.0 - entropy / np.log2(len(outcomes)), 4),
        )


_calculator = DistributionCalculator()


class CalculateRequest(BaseModel):
    action: str
    world_state: dict[str, Any] = {}
    agent_states: list[dict[str, Any]] | None = None


@router.post("/calculate", response_model=DistributionResult)
async def calculate_distribution(req: CalculateRequest) -> DistributionResult:
    """Calculate probability distribution for an action."""
    return _calculator.calculate(req.action, req.world_state, req.agent_states)
