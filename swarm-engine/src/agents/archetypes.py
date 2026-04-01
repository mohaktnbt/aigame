"""
Agent archetype definitions.

Each archetype defines baseline personality ranges, typical stances,
influence weights, and daily schedule patterns.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class ArchetypeDefinition:
    """Immutable archetype blueprint."""
    name: str
    description: str
    # Big Five baseline ranges: (min, max) for each trait
    openness: tuple[float, float] = (0.3, 0.7)
    conscientiousness: tuple[float, float] = (0.3, 0.7)
    extraversion: tuple[float, float] = (0.3, 0.7)
    agreeableness: tuple[float, float] = (0.3, 0.7)
    neuroticism: tuple[float, float] = (0.3, 0.7)
    # Default influence weight in the social graph
    base_influence: float = 1.0
    # Typical posting frequency per turn (social-sim posts)
    post_frequency: float = 0.3
    # Topics this archetype gravitates toward
    topic_affinity: list[str] = field(default_factory=list)


CITIZEN = ArchetypeDefinition(
    name="Citizen",
    description="Ordinary member of society; forms the bulk of the population.",
    openness=(0.3, 0.7),
    conscientiousness=(0.3, 0.7),
    extraversion=(0.2, 0.6),
    agreeableness=(0.4, 0.8),
    neuroticism=(0.2, 0.6),
    base_influence=1.0,
    post_frequency=0.2,
    topic_affinity=["daily_life", "economy", "local_news"],
)

LEADER = ArchetypeDefinition(
    name="Leader",
    description="Political or organizational leader with high influence.",
    openness=(0.4, 0.8),
    conscientiousness=(0.6, 0.9),
    extraversion=(0.6, 0.95),
    agreeableness=(0.2, 0.6),
    neuroticism=(0.1, 0.4),
    base_influence=10.0,
    post_frequency=0.5,
    topic_affinity=["policy", "governance", "diplomacy", "vision"],
)

MILITARY = ArchetypeDefinition(
    name="Military",
    description="Armed forces member; disciplined, group-loyal.",
    openness=(0.1, 0.4),
    conscientiousness=(0.7, 0.95),
    extraversion=(0.3, 0.6),
    agreeableness=(0.3, 0.6),
    neuroticism=(0.2, 0.5),
    base_influence=3.0,
    post_frequency=0.1,
    topic_affinity=["security", "duty", "national_defense"],
)

MERCHANT = ArchetypeDefinition(
    name="Merchant",
    description="Trader, business owner, or economic actor.",
    openness=(0.4, 0.7),
    conscientiousness=(0.5, 0.8),
    extraversion=(0.5, 0.8),
    agreeableness=(0.3, 0.6),
    neuroticism=(0.2, 0.5),
    base_influence=4.0,
    post_frequency=0.35,
    topic_affinity=["trade", "economy", "markets", "regulation"],
)

MEDIA = ArchetypeDefinition(
    name="Media",
    description="Journalist, blogger, or media personality.",
    openness=(0.6, 0.9),
    conscientiousness=(0.4, 0.7),
    extraversion=(0.6, 0.9),
    agreeableness=(0.3, 0.6),
    neuroticism=(0.3, 0.6),
    base_influence=7.0,
    post_frequency=0.8,
    topic_affinity=["news", "analysis", "scandal", "opinion"],
)

RELIGIOUS = ArchetypeDefinition(
    name="Religious",
    description="Spiritual leader or devout practitioner.",
    openness=(0.2, 0.5),
    conscientiousness=(0.6, 0.9),
    extraversion=(0.4, 0.7),
    agreeableness=(0.5, 0.9),
    neuroticism=(0.1, 0.4),
    base_influence=5.0,
    post_frequency=0.3,
    topic_affinity=["faith", "morality", "community", "tradition"],
)

ACADEMIC = ArchetypeDefinition(
    name="Academic",
    description="Scholar, researcher, or intellectual.",
    openness=(0.7, 0.95),
    conscientiousness=(0.5, 0.8),
    extraversion=(0.2, 0.5),
    agreeableness=(0.4, 0.7),
    neuroticism=(0.3, 0.6),
    base_influence=4.0,
    post_frequency=0.25,
    topic_affinity=["research", "education", "policy_analysis", "technology"],
)

CRIMINAL = ArchetypeDefinition(
    name="Criminal",
    description="Underworld figure or dissident operating outside the law.",
    openness=(0.3, 0.7),
    conscientiousness=(0.1, 0.4),
    extraversion=(0.3, 0.7),
    agreeableness=(0.1, 0.3),
    neuroticism=(0.4, 0.8),
    base_influence=3.0,
    post_frequency=0.15,
    topic_affinity=["underground", "corruption", "black_market", "dissent"],
)

ALL_ARCHETYPES: dict[str, ArchetypeDefinition] = {
    a.name: a
    for a in [CITIZEN, LEADER, MILITARY, MERCHANT, MEDIA, RELIGIOUS, ACADEMIC, CRIMINAL]
}
