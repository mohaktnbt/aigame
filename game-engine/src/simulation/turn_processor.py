"""Turn processor for Project Nexus.

Orchestrates the full turn lifecycle:
  validate action -> get probability -> resolve turn -> generate narrative -> update state
"""

from __future__ import annotations

import logging
import random
from datetime import datetime, timezone
from typing import Any

from src.agents.game_master import GameMasterAgent
from src.agents.narrator import NarratorAgent
from src.models.action import ActionValidation, PlayerAction, ValidationStatus
from src.models.event import GameEvent
from src.models.world_state import WorldState
from src.simulation.narrative_gravity import NarrativeGravityEngine
from src.simulation.quantitative import QuantitativeSimulator

logger = logging.getLogger(__name__)


class TurnResult:
    """Container for the outcome of processing a single turn."""

    def __init__(
        self,
        validation: ActionValidation,
        event: GameEvent | None,
        narrative: str,
        updated_state: WorldState,
        success: bool,
    ) -> None:
        self.validation = validation
        self.event = event
        self.narrative = narrative
        self.updated_state = updated_state
        self.success = success


class TurnProcessor:
    """Orchestrates a single game turn from player action to world-state update.

    Pipeline:
    1. Validate the player action via the Game Master agent.
    2. Calculate success probability (with narrative-gravity adjustment).
    3. Resolve the outcome stochastically.
    4. Compute quantitative changes.
    5. Generate a narrative via the Narrator agent.
    6. Apply changes to produce the next world state.
    """

    def __init__(
        self,
        game_master: GameMasterAgent | None = None,
        narrator: NarratorAgent | None = None,
        simulator: QuantitativeSimulator | None = None,
        gravity_engine: NarrativeGravityEngine | None = None,
    ) -> None:
        self.game_master = game_master or GameMasterAgent()
        self.narrator = narrator or NarratorAgent()
        self.simulator = simulator or QuantitativeSimulator()
        self.gravity = gravity_engine or NarrativeGravityEngine()

    async def process_turn(
        self,
        action: PlayerAction,
        world_state: WorldState,
    ) -> TurnResult:
        """Process a complete game turn.

        Args:
            action: The player's submitted action.
            world_state: The current world state before this turn.

        Returns:
            A TurnResult with the validation, event, narrative, and new state.
        """
        # 1. Validate
        validation = await self.game_master.validate_action(action, world_state)

        if validation.status == ValidationStatus.VOID:
            return TurnResult(
                validation=validation,
                event=None,
                narrative=validation.explanation,
                updated_state=world_state,
                success=False,
            )

        # 2. Calculate probability
        base_probability = validation.modifiers.get("success_probability", 0.6)
        adjusted_probability = self.gravity.calculate_adjusted_probability(
            base_probability=base_probability,
            world_state=world_state,
            action_text=action.text,
        )

        # 3. Resolve outcome
        roll = random.random()
        action_succeeded = roll < adjusted_probability
        is_backfire = validation.status == ValidationStatus.BACKFIRE

        if is_backfire and action_succeeded:
            # Backfire actions that "succeed" still have negative consequences
            event_type = "backfire"
        elif action_succeeded:
            event_type = "success"
        else:
            event_type = "failure"

        # 4. Compute quantitative changes
        # TODO: Use detailed modifiers from the validation and event type
        changes = self._compute_changes(action, world_state, event_type, validation)

        # Build event
        event = GameEvent(
            turn=world_state.turn + 1,
            type=event_type,
            title=f"Turn {world_state.turn + 1}: {action.text[:60]}",
            quantitative_changes=self._flatten_changes(changes),
            affected_factions=[action.faction_id],
            timestamp=datetime.now(tz=timezone.utc),
        )

        # 5. Generate narrative
        narrative = await self.narrator.generate_narrative(event, world_state)
        event.narrative = narrative

        # 6. Apply changes -> new world state
        updated_state = self.simulator.apply_changes(world_state, changes)
        updated_state.turn = world_state.turn + 1
        updated_state.recent_events.append(event.title)

        # Check narrative gravity for canonical events
        # TODO: Inject canonical events when they are due
        self.gravity.check_canonical_events(updated_state)

        return TurnResult(
            validation=validation,
            event=event,
            narrative=narrative,
            updated_state=updated_state,
            success=action_succeeded,
        )

    def _compute_changes(
        self,
        action: PlayerAction,
        world_state: WorldState,
        event_type: str,
        validation: ActionValidation,
    ) -> dict[str, dict[str, Any]]:
        """Compute per-nation quantitative deltas.

        Args:
            action: The player action.
            world_state: Current world state.
            event_type: Resolved event type (success/failure/backfire).
            validation: The action validation result.

        Returns:
            Dict keyed by nation name with sub-dicts of field deltas.
        """
        # TODO: Implement sophisticated change calculation using modifiers,
        #       nation capabilities, and cascading effects.
        changes: dict[str, dict[str, Any]] = {}
        sign = 1.0 if event_type == "success" else -1.0

        for nation in world_state.nations:
            if nation.name == action.faction_id or action.faction_id in nation.name:
                changes[nation.name] = {
                    "gdp": self.simulator.calculate_gdp_change(
                        nation,
                        {k: v * sign for k, v in validation.modifiers.items()},
                        world_state.global_economy,
                    ),
                    "sentiment": self.simulator.calculate_sentiment_shift(
                        nation,
                        event_type,
                        severity=abs(sum(validation.modifiers.values())) if validation.modifiers else 0.3,
                    ),
                }
        return changes

    @staticmethod
    def _flatten_changes(changes: dict[str, dict[str, Any]]) -> dict[str, float]:
        """Flatten per-nation changes into a single dict for the event model.

        Args:
            changes: Nested per-nation changes.

        Returns:
            Flat dict with 'nation.field' keys.
        """
        flat: dict[str, float] = {}
        for nation_name, deltas in changes.items():
            for field, value in deltas.items():
                flat[f"{nation_name}.{field}"] = float(value)
        return flat
