"""Narrative gravity engine for Project Nexus.

Narrative gravity is the force that pulls the simulation toward canonical
(pre-scripted) events, even as the player makes divergent choices. This
creates a tension between player agency and historical/narrative inevitability.
"""

from __future__ import annotations

import logging
from typing import Any

from src.models.event import GameEvent
from src.models.world_state import WorldState

logger = logging.getLogger(__name__)


class NarrativeGravityEngine:
    """Manages the pull toward canonical events in the simulation.

    Canonical events are story beats that the scenario author considers
    important. The gravity engine adjusts probabilities and can inject
    events to steer the narrative without completely overriding player
    agency.
    """

    def __init__(
        self,
        canonical_events: list[GameEvent] | None = None,
        gravity_strength: float = 0.3,
    ) -> None:
        """Initialize the narrative gravity engine.

        Args:
            canonical_events: Ordered list of canonical events for the scenario.
            gravity_strength: How strongly to pull toward canonical outcomes
                              (0.0 = no pull, 1.0 = deterministic).
        """
        self.canonical_events: list[GameEvent] = canonical_events or []
        self.gravity_strength: float = max(0.0, min(1.0, gravity_strength))
        self._triggered: set[int] = set()  # indices of already-triggered events

    def check_canonical_events(self, world_state: WorldState) -> list[GameEvent]:
        """Check whether any canonical events should fire on this turn.

        Events are triggered when the current turn matches or exceeds
        the canonical event's turn and the event has not yet been triggered.

        Args:
            world_state: The current world state.

        Returns:
            List of canonical events that should fire this turn.
        """
        triggered: list[GameEvent] = []

        for idx, event in enumerate(self.canonical_events):
            if idx in self._triggered:
                continue

            if world_state.turn >= event.turn:
                # TODO: Add condition checking beyond simple turn number.
                #       Evaluate world-state prerequisites (e.g. tension > 0.7)
                #       to decide if the event is contextually appropriate.
                triggered.append(event)
                self._triggered.add(idx)
                logger.info(
                    "Canonical event triggered: '%s' on turn %d",
                    event.title,
                    world_state.turn,
                )

        return triggered

    def calculate_adjusted_probability(
        self,
        base_probability: float,
        world_state: WorldState,
        action_text: str,
    ) -> float:
        """Adjust an action's success probability based on narrative gravity.

        If the player's action aligns with the next canonical event, gravity
        increases its probability. If it diverges, gravity decreases it.

        Args:
            base_probability: The original success probability (0.0 to 1.0).
            world_state: Current world state.
            action_text: The player's action text (used for alignment check).

        Returns:
            Adjusted probability clamped to [0.05, 0.95].
        """
        # Find the next un-triggered canonical event
        next_event = self._get_next_canonical(world_state.turn)

        if next_event is None:
            # No upcoming canonical events; no gravity adjustment
            return base_probability

        # TODO: Use semantic similarity (embeddings) to determine alignment
        #       between the player action and the canonical event narrative.
        alignment = self._estimate_alignment(action_text, next_event)

        # Gravity pulls probability toward 1.0 if aligned, toward 0.0 if divergent
        if alignment > 0:
            adjusted = base_probability + self.gravity_strength * alignment * (1.0 - base_probability)
        else:
            adjusted = base_probability + self.gravity_strength * alignment * base_probability

        clamped = max(0.05, min(0.95, adjusted))

        logger.debug(
            "Narrative gravity: base=%.3f alignment=%.3f adjusted=%.3f",
            base_probability,
            alignment,
            clamped,
        )
        return clamped

    def _get_next_canonical(self, current_turn: int) -> GameEvent | None:
        """Find the next canonical event that hasn't been triggered.

        Args:
            current_turn: The current game turn.

        Returns:
            The next canonical event or None.
        """
        for idx, event in enumerate(self.canonical_events):
            if idx not in self._triggered and event.turn >= current_turn:
                return event
        return None

    def _estimate_alignment(self, action_text: str, canonical_event: GameEvent) -> float:
        """Estimate how aligned a player action is with a canonical event.

        Args:
            action_text: The player's action text.
            canonical_event: The canonical event to compare against.

        Returns:
            Alignment score from -1.0 (directly opposed) to 1.0 (perfectly aligned).
        """
        # TODO: Replace with embedding-based semantic similarity.
        #       For now, use naive keyword overlap as a placeholder.
        action_words = set(action_text.lower().split())
        event_words = set(canonical_event.title.lower().split()) | set(
            canonical_event.narrative.lower().split()
        )

        if not event_words:
            return 0.0

        overlap = len(action_words & event_words)
        similarity = overlap / max(len(action_words), 1)

        # Map from [0, 1] to [-0.5, 1.0] -- low overlap slightly negative
        return min(1.0, similarity * 2.0 - 0.3)

    def set_canonical_events(self, events: list[GameEvent]) -> None:
        """Replace the canonical event list (e.g. when loading a new scenario).

        Args:
            events: New list of canonical events.
        """
        self.canonical_events = events
        self._triggered.clear()
        logger.info("Loaded %d canonical events", len(events))
