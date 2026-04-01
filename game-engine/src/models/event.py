"""Event models for Project Nexus."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field


class GameEvent(BaseModel):
    """An event that occurs during the simulation."""

    turn: int
    type: str = Field(description="Event type e.g. political, military, economic, diplomatic, social")
    title: str
    narrative: str = Field(default="", description="Rich narrative text describing the event")
    quantitative_changes: dict[str, float] = Field(
        default_factory=dict,
        description="Numeric changes keyed by metric name e.g. {'gdp_delta': -0.05}",
    )
    affected_factions: list[str] = Field(default_factory=list)
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    severity: float = Field(default=0.5, ge=0.0, le=1.0, description="Event severity/impact magnitude")
