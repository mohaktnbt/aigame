"""
OptionRanker — Ranks a set of options against weighted criteria.
"""

from __future__ import annotations

from typing import Any

import numpy as np
from pydantic import BaseModel


class RankedOption(BaseModel):
    """An option with its computed score and breakdown."""
    option: str
    total_score: float
    criterion_scores: dict[str, float]
    rank: int


class OptionRanker:
    """Ranks options using multi-criteria weighted scoring.

    Given a list of options and a set of weighted criteria, the ranker
    evaluates each option against every criterion and produces a ranked
    list with detailed score breakdowns.

    TODO: Support pairwise comparison (AHP) mode.
    TODO: Support LLM-based criterion evaluation.
    TODO: Implement Pareto-optimal filtering for multi-objective cases.
    """

    def rank_options(
        self,
        options: list[str],
        criteria: dict[str, float],
        evaluations: dict[str, dict[str, float]] | None = None,
    ) -> list[RankedOption]:
        """Rank options against weighted criteria.

        Args:
            options: List of option descriptions.
            criteria: Mapping of criterion_name -> weight (weights are normalized).
            evaluations: Optional pre-computed scores:
                         {option -> {criterion -> score}}.
                         If None, stub scores are generated.

        Returns:
            List of RankedOption sorted by total_score descending.

        TODO: Replace stub evaluations with LLM or model-based scoring.
        """
        # Normalize weights
        total_weight = sum(criteria.values())
        norm_weights = {k: v / total_weight for k, v in criteria.items()} if total_weight > 0 else criteria

        ranked: list[RankedOption] = []

        for option in options:
            if evaluations and option in evaluations:
                scores = evaluations[option]
            else:
                # STUB: generate random scores for demonstration
                rng = np.random.default_rng(hash(option) % (2**31))
                scores = {c: float(round(rng.uniform(0.0, 1.0), 3)) for c in criteria}

            total = sum(scores.get(c, 0.0) * norm_weights.get(c, 0.0) for c in criteria)
            ranked.append(RankedOption(
                option=option,
                total_score=round(total, 4),
                criterion_scores=scores,
                rank=0,  # set below
            ))

        ranked.sort(key=lambda r: r.total_score, reverse=True)
        for i, item in enumerate(ranked, 1):
            item.rank = i

        return ranked
