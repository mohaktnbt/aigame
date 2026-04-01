"""Actor models for Project Nexus."""

from __future__ import annotations

from pydantic import BaseModel, Field


class Actor(BaseModel):
    """An actor (player or NPC) in the simulation."""

    name: str
    role: str = "leader"
    faction: str = ""
    influence: float = Field(default=1.0, ge=0.0, le=10.0, description="Political influence level")
    personality: str = Field(default="pragmatic", description="Personality archetype e.g. hawkish, dovish, pragmatic")
    goals: list[str] = Field(default_factory=list, description="Current strategic goals")
    relationships: dict[str, float] = Field(default_factory=dict, description="Relationship scores with other actors")
