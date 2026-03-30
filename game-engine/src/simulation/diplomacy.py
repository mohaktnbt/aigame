"""Diplomacy engine for Project Nexus."""

from __future__ import annotations

import logging
from typing import Any

from src.models.world_state import Nation, WorldState

logger = logging.getLogger(__name__)


class DiplomacyEngine:
    """Evaluates treaties and manages diplomatic relations between nations.

    Tracks bilateral relation scores and determines the viability and
    consequences of treaties, alliances, and sanctions.
    """

    def __init__(self) -> None:
        # Bilateral relation scores keyed by (nation_a, nation_b) tuple-strings.
        # Values range from -1.0 (hostile) to 1.0 (allied).
        self._relations: dict[tuple[str, str], float] = {}

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------
    @staticmethod
    def _key(a: str, b: str) -> tuple[str, str]:
        """Canonical key so (A,B) == (B,A)."""
        return (min(a, b), max(a, b))

    def get_relation(self, nation_a: str, nation_b: str) -> float:
        """Return the current relation score between two nations.

        Args:
            nation_a: First nation name.
            nation_b: Second nation name.

        Returns:
            Relation score from -1.0 to 1.0 (default 0.0 if unset).
        """
        return self._relations.get(self._key(nation_a, nation_b), 0.0)

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------
    def evaluate_treaty(
        self,
        proposer: Nation,
        target: Nation,
        treaty_type: str,
        terms: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """Evaluate whether a proposed treaty is likely to be accepted.

        Args:
            proposer: The nation proposing the treaty.
            target: The target nation.
            treaty_type: Type of treaty (e.g. 'trade', 'alliance', 'ceasefire', 'sanctions').
            terms: Optional dict of specific treaty terms.

        Returns:
            Dict with keys: feasible (bool), acceptance_probability (float),
            counter_terms (dict | None), reasoning (str).
        """
        # TODO: Implement detailed treaty evaluation model incorporating
        #       economic leverage, military balance, historical relations,
        #       and third-party pressure.
        relation = self.get_relation(proposer.name, target.name)

        # Simple heuristic: higher relations -> higher acceptance
        base_probability = max(0.0, min(1.0, (relation + 1.0) / 2.0))

        # Adjust by treaty type difficulty
        type_modifiers: dict[str, float] = {
            "trade": 0.1,
            "ceasefire": 0.05,
            "alliance": -0.1,
            "sanctions": -0.2,
            "non_aggression": 0.0,
        }
        modifier = type_modifiers.get(treaty_type, 0.0)
        probability = max(0.0, min(1.0, base_probability + modifier))

        feasible = probability > 0.3

        return {
            "feasible": feasible,
            "acceptance_probability": round(probability, 3),
            "counter_terms": None,  # TODO: Generate counter-proposals via LLM
            "reasoning": (
                f"Relation score {relation:.2f} yields base acceptance "
                f"{base_probability:.2f}, adjusted to {probability:.2f} "
                f"for treaty type '{treaty_type}'."
            ),
        }

    def update_relations(
        self,
        nation_a: str,
        nation_b: str,
        delta: float,
        reason: str = "",
    ) -> float:
        """Update the bilateral relation score between two nations.

        Args:
            nation_a: First nation name.
            nation_b: Second nation name.
            delta: Change in relation score.
            reason: Human-readable reason for the change.

        Returns:
            The new relation score after clamping to [-1.0, 1.0].
        """
        key = self._key(nation_a, nation_b)
        current = self._relations.get(key, 0.0)
        new_score = max(-1.0, min(1.0, current + delta))
        self._relations[key] = new_score

        logger.info(
            "Relations %s <-> %s: %.2f -> %.2f (%s)",
            nation_a,
            nation_b,
            current,
            new_score,
            reason or "no reason given",
        )
        return new_score

    def initialize_from_world_state(self, world_state: WorldState) -> None:
        """Seed relation scores from allies/rivals lists in the world state.

        Args:
            world_state: The initial world state to read from.
        """
        for nation in world_state.nations:
            for ally in nation.allies:
                key = self._key(nation.name, ally)
                self._relations.setdefault(key, 0.5)
            for rival in nation.rivals:
                key = self._key(nation.name, rival)
                self._relations.setdefault(key, -0.5)
