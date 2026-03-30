"""Advisor agent for Project Nexus."""

from __future__ import annotations

import logging

from src.llm.openrouter import OpenRouterClient
from src.llm.prompts import ADVISOR_BRIEFING, ADVISOR_SYSTEM
from src.models.world_state import WorldState

logger = logging.getLogger(__name__)


class AdvisorAgent:
    """The Advisor provides strategic intelligence briefings to the player.

    It analyzes the world state and recent events to highlight risks,
    opportunities, and recommended courses of action.
    """

    def __init__(self, llm_client: OpenRouterClient | None = None) -> None:
        self.llm = llm_client or OpenRouterClient()

    async def generate_briefing(
        self,
        faction_id: str,
        world_state: WorldState,
    ) -> str:
        """Generate a strategic briefing for the given faction.

        Args:
            faction_id: The player's faction identifier.
            world_state: Current world state.

        Returns:
            A strategic briefing string.
        """
        recent = "\n".join(f"- {e}" for e in world_state.recent_events[-10:]) or "No recent events."

        prompt = ADVISOR_BRIEFING.format(
            world_state=world_state.model_dump_json(indent=2),
            faction_id=faction_id,
            recent_events=recent,
        )

        try:
            response = await self.llm.chat_completion(
                messages=[
                    {"role": "system", "content": ADVISOR_SYSTEM},
                    {"role": "user", "content": prompt},
                ],
                temperature=0.5,
            )
            return response["choices"][0]["message"]["content"]
        except Exception:
            logger.exception("Failed to generate briefing via LLM")
            return f"Intelligence briefing unavailable for faction '{faction_id}'. Please try again."
