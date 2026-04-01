"""
ScenarioBrancher — Lightweight parallel simulation for "what if" analysis.

Given the current world state and a hypothetical action, the brancher
forks a lightweight copy of the simulation and runs it forward N turns
to project likely outcomes.
"""

from __future__ import annotations

import copy
from typing import Any

from pydantic import BaseModel

from src.agents.persona_generator import AgentPersona


class WorldState(BaseModel):
    """Snapshot of the simulation world state."""
    turn: int
    agents: list[dict[str, Any]]
    global_params: dict[str, Any] = {}


class BranchResult(BaseModel):
    """Result of a branched what-if simulation."""
    hypothesis: str
    turns_simulated: int
    projected_sentiment: float
    projected_stability: float
    key_events: list[str]
    risk_factors: list[str]
    confidence: float  # 0-1


class ScenarioBrancher:
    """Forks lightweight parallel sims for hypothesis testing.

    The brancher creates a shallow copy of the world state, applies the
    hypothetical action, then runs a simplified simulation loop to project
    outcomes.  This is intentionally less detailed than the full sim to
    keep latency manageable.

    TODO: Use a simplified agent decision model for fast-forward.
    TODO: Monte Carlo ensemble (run N branches, aggregate).
    TODO: Cache branch results for similar hypotheses.
    """

    def _apply_action(
        self,
        world_state: WorldState,
        action: dict[str, Any],
    ) -> WorldState:
        """Apply the hypothetical action to a copy of the world state.

        TODO: Implement action types (policy change, military action,
              economic sanction, etc.) with concrete state mutations.
        """
        modified = world_state.model_copy(deep=True)
        # STUB: apply action effects
        modified.global_params["last_hypothetical_action"] = action
        return modified

    def _fast_forward(
        self,
        world_state: WorldState,
        num_turns: int,
    ) -> tuple[WorldState, list[str]]:
        """Run a simplified simulation forward N turns.

        Returns:
            Tuple of (final_state, list_of_key_events).

        TODO: Implement simplified agent decision loop.
        TODO: Track key events (threshold crossings, emergent patterns).
        """
        events: list[str] = []
        current = world_state.model_copy(deep=True)
        for t in range(num_turns):
            current.turn += 1
            # STUB: simplified turn processing
            events.append(f"Turn {current.turn}: simulated (stub)")
        return current, events

    def branch(
        self,
        world_state: WorldState,
        hypothetical_action: dict[str, Any],
        num_turns: int = 5,
    ) -> BranchResult:
        """Fork a parallel sim and project outcomes.

        Args:
            world_state: Current world snapshot.
            hypothetical_action: Dict describing the action to test.
            num_turns: How many turns to simulate forward.

        Returns:
            BranchResult with projected metrics and events.

        TODO: Replace stub projections with actual simulation outputs.
        """
        hypothesis_desc = hypothetical_action.get("description", "Unknown action")

        modified_state = self._apply_action(world_state, hypothetical_action)
        final_state, events = self._fast_forward(modified_state, num_turns)

        return BranchResult(
            hypothesis=hypothesis_desc,
            turns_simulated=num_turns,
            projected_sentiment=0.5,   # TODO: compute from final agent states
            projected_stability=0.6,   # TODO: compute from final world params
            key_events=events,
            risk_factors=["stub_risk: no real simulation ran"],
            confidence=0.1,  # low confidence until real sim is implemented
        )
