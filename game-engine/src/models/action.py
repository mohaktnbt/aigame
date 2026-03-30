"""Player action models for Project Nexus."""

from __future__ import annotations

from enum import Enum

from pydantic import BaseModel, Field


class ValidationStatus(str, Enum):
    """Possible statuses for an action validation."""

    VOID = "void"
    BACKFIRE = "backfire"
    APPROVE = "approve"


class PlayerAction(BaseModel):
    """A natural-language action submitted by the player."""

    text: str = Field(description="Free-form natural language action text")
    faction_id: str = Field(description="The faction submitting the action")


class ActionValidation(BaseModel):
    """Result of validating a player action against the game state."""

    status: ValidationStatus = Field(description="Whether the action is void, will backfire, or is approved")
    explanation: str = Field(default="", description="Narrative explanation of the validation result")
    modifiers: dict[str, float] = Field(
        default_factory=dict,
        description="Adjustments to apply if the action proceeds e.g. {'success_probability': 0.7}",
    )
