"""Narrator agent for Project Nexus."""

from __future__ import annotations

import logging

from src.llm.openrouter import OpenRouterClient
from src.llm.prompts import NARRATOR_GENERATE, NARRATOR_SYSTEM
from src.models.event import GameEvent
from src.models.world_state import WorldState

logger = logging.getLogger(__name__)


class NarratorAgent:
    """The Narrator generates rich narrative text for game events.

    It transforms dry quantitative changes into compelling prose that
    immerses the player in the simulation.
    """

    def __init__(self, llm_client: OpenRouterClient | None = None) -> None:
        self.llm = llm_client or OpenRouterClient()

    async def generate_narrative(
        self,
        event: GameEvent,
        world_state: WorldState,
    ) -> str:
        """Generate narrative text for a game event.

        Args:
            event: The event to narrate.
            world_state: Current world state for context.

        Returns:
            A narrative string describing the event.
        """
        prompt = NARRATOR_GENERATE.format(
            world_state=world_state.model_dump_json(indent=2),
            event_type=event.type,
            event_title=event.title,
            changes=event.quantitative_changes,
            factions=", ".join(event.affected_factions),
        )

        try:
            response = await self.llm.chat_completion(
                messages=[
                    {"role": "system", "content": NARRATOR_SYSTEM},
                    {"role": "user", "content": prompt},
                ],
                temperature=0.8,
            )
            return response["choices"][0]["message"]["content"]
        except Exception:
            logger.exception("Failed to generate narrative via LLM")
            return f"[Turn {event.turn}] {event.title}: {event.type} event affecting {', '.join(event.affected_factions)}."
