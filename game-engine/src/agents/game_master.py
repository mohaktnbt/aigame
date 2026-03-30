"""Game Master agent for Project Nexus."""

from __future__ import annotations

import json
import logging
from typing import Any

from src.llm.openrouter import OpenRouterClient
from src.llm.prompts import GAME_MASTER_SYSTEM, GAME_MASTER_VALIDATE
from src.models.action import ActionValidation, PlayerAction, ValidationStatus
from src.models.world_state import WorldState

logger = logging.getLogger(__name__)


class GameMasterAgent:
    """The Game Master validates player actions against the world state.

    It uses an LLM to parse natural-language actions and determine
    whether they are plausible, risky, or impossible given the current
    scenario rules and world conditions.
    """

    def __init__(self, llm_client: OpenRouterClient | None = None) -> None:
        self.llm = llm_client or OpenRouterClient()

    async def validate_action(
        self,
        action: PlayerAction,
        world_state: WorldState,
    ) -> ActionValidation:
        """Validate a player's natural-language action.

        Args:
            action: The player action to validate.
            world_state: Current world state for context.

        Returns:
            An ActionValidation with status, explanation, and modifiers.
        """
        prompt = GAME_MASTER_VALIDATE.format(
            world_state=world_state.model_dump_json(indent=2),
            faction_id=action.faction_id,
            action_text=action.text,
        )

        try:
            response = await self.llm.chat_completion(
                messages=[
                    {"role": "system", "content": GAME_MASTER_SYSTEM},
                    {"role": "user", "content": prompt},
                ],
                temperature=0.3,
            )
            content = response["choices"][0]["message"]["content"]
            parsed = self._parse_validation(content)
            return parsed
        except Exception:
            logger.exception("Failed to validate action via LLM")
            # TODO: Implement fallback rule-based validation
            return ActionValidation(
                status=ValidationStatus.APPROVE,
                explanation="Validation service unavailable; action tentatively approved.",
                modifiers={},
            )

    def _parse_validation(self, llm_response: str) -> ActionValidation:
        """Parse the LLM JSON response into an ActionValidation.

        Args:
            llm_response: Raw text from the LLM.

        Returns:
            Parsed ActionValidation.
        """
        try:
            data: dict[str, Any] = json.loads(llm_response)
            return ActionValidation(
                status=ValidationStatus(data.get("status", "approve")),
                explanation=data.get("explanation", ""),
                modifiers=data.get("modifiers", {}),
            )
        except (json.JSONDecodeError, ValueError):
            logger.warning("Could not parse LLM validation response, defaulting to approve")
            return ActionValidation(
                status=ValidationStatus.APPROVE,
                explanation=llm_response,
                modifiers={},
            )
