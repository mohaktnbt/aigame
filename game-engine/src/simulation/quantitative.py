"""Quantitative simulation engine for Project Nexus."""

from __future__ import annotations

import logging
from typing import Any

from src.models.world_state import Nation, WorldState

logger = logging.getLogger(__name__)


class QuantitativeSimulator:
    """Handles all numeric calculations for the simulation.

    Computes GDP changes, military impacts, sentiment shifts, and
    applies them to the world state deterministically.
    """

    def calculate_gdp_change(
        self,
        nation: Nation,
        event_modifiers: dict[str, float],
        global_economy: float = 1.0,
    ) -> float:
        """Calculate GDP change for a nation based on event modifiers.

        Args:
            nation: The nation to calculate for.
            event_modifiers: Dict of modifier keys to float values.
            global_economy: Global economic multiplier.

        Returns:
            The absolute GDP change (positive or negative).
        """
        # TODO: Implement detailed economic model with trade, sanctions, tech bonuses
        base_growth = nation.gdp * 0.02 * global_economy  # 2% base growth
        modifier_impact = sum(event_modifiers.values()) * nation.gdp
        return base_growth + modifier_impact

    def calculate_military_impact(
        self,
        nation: Nation,
        action_type: str,
        intensity: float = 0.5,
    ) -> float:
        """Calculate military strength change.

        Args:
            nation: The nation affected.
            action_type: Type of military action (e.g. 'mobilize', 'conflict', 'disarm').
            intensity: Intensity of the action from 0 to 1.

        Returns:
            Change in military strength index.
        """
        # TODO: Implement detailed military model with unit types, logistics, morale
        multipliers = {
            "mobilize": 0.1,
            "conflict": -0.15,
            "disarm": -0.2,
            "invest": 0.05,
        }
        multiplier = multipliers.get(action_type, 0.0)
        return nation.military * multiplier * intensity

    def calculate_sentiment_shift(
        self,
        nation: Nation,
        event_type: str,
        severity: float = 0.5,
    ) -> float:
        """Calculate public sentiment change.

        Args:
            nation: The nation affected.
            event_type: The type of event triggering the shift.
            severity: How severe the event is (0 to 1).

        Returns:
            Sentiment delta (clamped to keep final value in [-1, 1]).
        """
        # TODO: Implement media influence, propaganda, and historical memory
        sentiment_impacts: dict[str, float] = {
            "economic_boom": 0.1,
            "economic_crisis": -0.2,
            "military_victory": 0.15,
            "military_defeat": -0.25,
            "diplomatic_success": 0.05,
            "scandal": -0.15,
        }
        base_shift = sentiment_impacts.get(event_type, 0.0) * severity
        # Ensure final sentiment stays within bounds
        new_sentiment = max(-1.0, min(1.0, nation.sentiment + base_shift))
        return new_sentiment - nation.sentiment

    def apply_changes(
        self,
        world_state: WorldState,
        changes: dict[str, dict[str, Any]],
    ) -> WorldState:
        """Apply a set of quantitative changes to the world state.

        Args:
            world_state: The current world state (will not be mutated).
            changes: Dict keyed by nation name, each containing field deltas.

        Returns:
            A new WorldState with changes applied.
        """
        # TODO: Implement cascading effects (e.g. GDP collapse triggers sentiment drop)
        updated = world_state.model_copy(deep=True)

        for nation in updated.nations:
            if nation.name in changes:
                deltas = changes[nation.name]
                if "gdp" in deltas:
                    nation.gdp += deltas["gdp"]
                if "military" in deltas:
                    nation.military = max(0.0, nation.military + deltas["military"])
                if "sentiment" in deltas:
                    nation.sentiment = max(-1.0, min(1.0, nation.sentiment + deltas["sentiment"]))
                if "tech_level" in deltas:
                    nation.tech_level = max(0.0, nation.tech_level + deltas["tech_level"])
                if "population" in deltas:
                    nation.population = max(0, nation.population + int(deltas["population"]))

        return updated
