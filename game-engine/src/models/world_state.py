"""World state models for Project Nexus."""

from __future__ import annotations

from pydantic import BaseModel, Field


class Resource(BaseModel):
    """A resource available in the game world."""

    name: str
    quantity: float = 0.0
    production_rate: float = 0.0
    consumption_rate: float = 0.0
    strategic_value: float = Field(default=1.0, ge=0.0, le=10.0)


class Territory(BaseModel):
    """A territory or region on the game map."""

    id: str
    name: str
    controller: str | None = None
    resources: list[Resource] = Field(default_factory=list)
    population: int = 0
    stability: float = Field(default=1.0, ge=0.0, le=1.0)
    terrain_type: str = "plains"


class Nation(BaseModel):
    """A nation or state actor in the simulation."""

    name: str
    gdp: float = 0.0
    military: float = Field(default=0.0, ge=0.0, description="Military strength index")
    tech_level: float = Field(default=1.0, ge=0.0)
    sentiment: float = Field(default=0.0, ge=-1.0, le=1.0, description="Public sentiment from -1 (hostile) to 1 (supportive)")
    population: int = 0
    leader: str = "Unknown"
    government_type: str = "republic"
    resources: list[Resource] = Field(default_factory=list)
    territories: list[str] = Field(default_factory=list)
    allies: list[str] = Field(default_factory=list)
    rivals: list[str] = Field(default_factory=list)


class WorldState(BaseModel):
    """The complete state of the game world at a point in time."""

    turn: int = 0
    nations: list[Nation] = Field(default_factory=list)
    territories: list[Territory] = Field(default_factory=list)
    global_tension: float = Field(default=0.0, ge=0.0, le=1.0)
    global_economy: float = Field(default=1.0, description="Global economic multiplier")
    active_treaties: list[str] = Field(default_factory=list)
    recent_events: list[str] = Field(default_factory=list)
