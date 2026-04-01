"""
PersonaGenerator — Creates fully-realised agent personas from archetype blueprints.
"""

from __future__ import annotations

import random
import uuid
from typing import Any

from pydantic import BaseModel, Field

from src.agents.archetypes import ALL_ARCHETYPES, ArchetypeDefinition


class BigFivePersonality(BaseModel):
    """OCEAN personality model with 0-1 float scores."""
    openness: float = Field(ge=0.0, le=1.0)
    conscientiousness: float = Field(ge=0.0, le=1.0)
    extraversion: float = Field(ge=0.0, le=1.0)
    agreeableness: float = Field(ge=0.0, le=1.0)
    neuroticism: float = Field(ge=0.0, le=1.0)


class AgentPersona(BaseModel):
    """Complete persona for a simulated agent."""
    agent_id: str
    name: str
    archetype: str
    faction: str
    region: str
    personality: BigFivePersonality
    stance: dict[str, float]  # topic -> sentiment (-1.0 to 1.0)
    influence: float
    schedule: list[str]  # ordered list of daily activity slots
    backstory: str


class PersonaGenerator:
    """Generates diverse agent personas from archetype definitions.

    Uses controlled randomness within archetype-defined ranges so that
    populations exhibit realistic variance while preserving archetype flavour.
    """

    def __init__(self, rng_seed: int | None = None) -> None:
        self._rng = random.Random(rng_seed)

    def _sample_range(self, low: float, high: float) -> float:
        return round(self._rng.uniform(low, high), 3)

    def _generate_personality(self, archetype: ArchetypeDefinition) -> BigFivePersonality:
        return BigFivePersonality(
            openness=self._sample_range(*archetype.openness),
            conscientiousness=self._sample_range(*archetype.conscientiousness),
            extraversion=self._sample_range(*archetype.extraversion),
            agreeableness=self._sample_range(*archetype.agreeableness),
            neuroticism=self._sample_range(*archetype.neuroticism),
        )

    def _generate_stance(self, archetype: ArchetypeDefinition) -> dict[str, float]:
        """Generate initial stances on the archetype's affinity topics.

        TODO: Derive initial stances from world-state context and faction goals.
        """
        return {
            topic: round(self._rng.uniform(-1.0, 1.0), 3)
            for topic in archetype.topic_affinity
        }

    def _generate_schedule(self, archetype: ArchetypeDefinition) -> list[str]:
        """Generate a daily activity schedule.

        TODO: Make schedules region-aware and culturally influenced.
        """
        base_schedule = ["sleep", "morning_routine", "work", "social", "work", "leisure", "social", "sleep"]
        if archetype.name == "Military":
            base_schedule = ["sleep", "drill", "patrol", "briefing", "patrol", "drill", "mess", "sleep"]
        elif archetype.name == "Media":
            base_schedule = ["sleep", "news_scan", "investigate", "write", "broadcast", "social", "write", "sleep"]
        return base_schedule

    def generate_persona(
        self,
        archetype: str,
        faction: str,
        region: str,
        name: str | None = None,
    ) -> AgentPersona:
        """Generate a single agent persona.

        Args:
            archetype: Name of the archetype (must exist in ALL_ARCHETYPES).
            faction: Faction the agent belongs to.
            region: Geographic or administrative region.
            name: Optional explicit name; auto-generated if omitted.

        Returns:
            Fully populated AgentPersona.

        TODO: Use LLM to generate culturally appropriate names.
        TODO: Generate richer backstories based on world lore.
        """
        arch_def = ALL_ARCHETYPES[archetype]
        agent_id = str(uuid.uuid4())
        agent_name = name or f"{archetype}_{agent_id[:8]}"

        return AgentPersona(
            agent_id=agent_id,
            name=agent_name,
            archetype=archetype,
            faction=faction,
            region=region,
            personality=self._generate_personality(arch_def),
            stance=self._generate_stance(arch_def),
            influence=arch_def.base_influence * self._rng.uniform(0.7, 1.3),
            schedule=self._generate_schedule(arch_def),
            backstory=f"A {archetype.lower()} from {region}, aligned with {faction}.",
        )

    def generate_batch(
        self,
        archetype: str,
        faction: str,
        region: str,
        count: int,
    ) -> list[AgentPersona]:
        """Generate multiple personas of the same archetype."""
        return [self.generate_persona(archetype, faction, region) for _ in range(count)]
