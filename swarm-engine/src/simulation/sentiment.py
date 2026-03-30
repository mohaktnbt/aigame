"""
SentimentAggregator — Aggregates agent attitudes into regional and
factional sentiment scores, protest probabilities, and loyalty indices.
"""

from __future__ import annotations

from typing import Any

import numpy as np
from pydantic import BaseModel

from src.agents.persona_generator import AgentPersona


class SentimentReport(BaseModel):
    """Aggregated sentiment for a group of agents."""
    group_label: str
    agent_count: int
    mean_sentiment: float
    sentiment_std: float
    protest_probability: float
    loyalty_index: float
    top_grievances: list[str]


class SentimentAggregator:
    """Computes collective sentiment metrics from individual agent states.

    Sentiment is derived from agent stances, personality traits (especially
    neuroticism and agreeableness), and recent social-media activity.

    TODO: Weight sentiment by agent influence.
    TODO: Incorporate temporal trend (sentiment momentum).
    TODO: Cross-reference with graph-based community detection.
    """

    def _compute_protest_probability(
        self,
        mean_sentiment: float,
        neuroticism_mean: float,
        grievance_count: float,
    ) -> float:
        """Heuristic protest probability.

        TODO: Replace with calibrated logistic model.
        """
        raw = (1.0 - mean_sentiment) * 0.4 + neuroticism_mean * 0.3 + min(grievance_count / 5.0, 1.0) * 0.3
        return float(np.clip(raw, 0.0, 1.0))

    def _compute_loyalty_index(
        self,
        mean_sentiment: float,
        agreeableness_mean: float,
    ) -> float:
        """Heuristic loyalty index (0 = disloyal, 1 = fiercely loyal).

        TODO: Factor in leader approval and recent policy changes.
        """
        raw = mean_sentiment * 0.5 + agreeableness_mean * 0.5
        return float(np.clip(raw, 0.0, 1.0))

    def aggregate(
        self,
        agents: list[AgentPersona],
        group_label: str = "all",
    ) -> SentimentReport:
        """Aggregate sentiment across a set of agents.

        Args:
            agents: The agents to aggregate over.
            group_label: Human-readable label (e.g., region or faction name).

        Returns:
            SentimentReport with scores and probabilities.
        """
        if not agents:
            return SentimentReport(
                group_label=group_label,
                agent_count=0,
                mean_sentiment=0.0,
                sentiment_std=0.0,
                protest_probability=0.0,
                loyalty_index=0.0,
                top_grievances=[],
            )

        sentiments = []
        neuroticisms = []
        agreeablenesses = []
        grievance_counts: list[float] = []
        grievance_bag: dict[str, int] = {}

        for agent in agents:
            # Average across all stance values as a rough overall sentiment
            stance_vals = list(agent.stance.values())
            avg_stance = float(np.mean(stance_vals)) if stance_vals else 0.0
            # Normalize from [-1,1] to [0,1]
            sentiments.append((avg_stance + 1.0) / 2.0)
            neuroticisms.append(agent.personality.neuroticism)
            agreeablenesses.append(agent.personality.agreeableness)

            # Collect negative-stance topics as grievances
            for topic, val in agent.stance.items():
                if val < -0.3:
                    grievance_bag[topic] = grievance_bag.get(topic, 0) + 1
            grievance_counts.append(sum(1 for v in stance_vals if v < -0.3))

        mean_sent = float(np.mean(sentiments))
        std_sent = float(np.std(sentiments))
        mean_neuro = float(np.mean(neuroticisms))
        mean_agree = float(np.mean(agreeablenesses))
        mean_griev = float(np.mean(grievance_counts))

        top_grievances = sorted(grievance_bag, key=grievance_bag.get, reverse=True)[:5]  # type: ignore[arg-type]

        return SentimentReport(
            group_label=group_label,
            agent_count=len(agents),
            mean_sentiment=round(mean_sent, 4),
            sentiment_std=round(std_sent, 4),
            protest_probability=round(self._compute_protest_probability(mean_sent, mean_neuro, mean_griev), 4),
            loyalty_index=round(self._compute_loyalty_index(mean_sent, mean_agree), 4),
            top_grievances=top_grievances,
        )
