"""Scenario models for Project Nexus."""

from __future__ import annotations

from pydantic import BaseModel, Field

from src.models.event import GameEvent
from src.models.world_state import WorldState


class Scenario(BaseModel):
    """A game scenario that defines the setting, rules, and initial conditions."""

    id: str
    title: str
    description: str = ""
    type: str = Field(default="geopolitical", description="Scenario type e.g. geopolitical, economic, military")
    universe_rules: dict[str, object] = Field(
        default_factory=dict,
        description="Rules and constraints that govern this scenario's universe",
    )
    initial_world_state: WorldState = Field(default_factory=WorldState)
    factions: list[str] = Field(default_factory=list, description="Available factions the player can choose")
    canonical_events: list[GameEvent] = Field(
        default_factory=list,
        description="Pre-scripted events that narrative gravity pulls toward",
    )
