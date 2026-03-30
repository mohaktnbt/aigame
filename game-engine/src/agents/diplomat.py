"""Diplomat agent for Project Nexus."""

from __future__ import annotations

import logging

from src.llm.openrouter import OpenRouterClient
from src.llm.prompts import DIPLOMAT_NEGOTIATE, DIPLOMAT_SYSTEM
from src.models.actor import Actor

logger = logging.getLogger(__name__)


class DiplomatAgent:
    """The Diplomat roleplays as a foreign leader during negotiations.

    It stays in character based on the nation's personality, goals, and
    current diplomatic relations.
    """

    def __init__(self, llm_client: OpenRouterClient | None = None) -> None:
        self.llm = llm_client or OpenRouterClient()

    async def negotiate(
        self,
        actor: Actor,
        counterpart: str,
        proposal: str,
        relation_score: float = 0.0,
    ) -> str:
        """Generate a diplomatic response to a negotiation proposal.

        Args:
            actor: The AI diplomat actor.
            counterpart: Name of the counterpart nation.
            proposal: The proposal text to respond to.
            relation_score: Current relation score between the two parties (-1 to 1).

        Returns:
            An in-character diplomatic response string.
        """
        prompt = DIPLOMAT_NEGOTIATE.format(
            nation_name=actor.faction,
            personality=actor.personality,
            goals=", ".join(actor.goals) if actor.goals else "maintain stability",
            relation_score=relation_score,
            counterpart=counterpart,
            proposal=proposal,
        )

        try:
            response = await self.llm.chat_completion(
                messages=[
                    {"role": "system", "content": DIPLOMAT_SYSTEM},
                    {"role": "user", "content": prompt},
                ],
                temperature=0.7,
            )
            return response["choices"][0]["message"]["content"]
        except Exception:
            logger.exception("Failed to generate diplomatic response via LLM")
            return f"[{actor.faction}] We acknowledge your proposal regarding '{proposal[:50]}...' and will respond in due course."
