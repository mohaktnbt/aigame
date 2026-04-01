"""
EmergenceDetector — Detects emergent collective behaviours from agent states.

Scans for patterns such as protests, social movements, alliance formation,
and economic shifts that arise organically from individual agent actions.
"""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel

from src.agents.persona_generator import AgentPersona


class EmergentPattern(BaseModel):
    """A detected emergent behaviour."""
    pattern_type: str  # "protest", "movement", "alliance", "economic_shift", "cultural_trend"
    description: str
    severity: float  # 0-1 how significant
    involved_agent_count: int
    involved_factions: list[str]
    involved_regions: list[str]
    metadata: dict[str, Any] = {}


class EmergenceDetector:
    """Detects emergent collective patterns from agent populations.

    The detector runs a suite of heuristic checks each turn, looking for
    statistical anomalies in agent stances, clustering in social graphs,
    and correlated behavioural shifts.

    TODO: Use graph community detection (Louvain) for alliance detection.
    TODO: Use time-series anomaly detection for economic shifts.
    TODO: Integrate with social-sim engagement data for movement detection.
    """

    def _detect_protests(self, agents: list[AgentPersona]) -> list[EmergentPattern]:
        """Detect protest-like clustering of negative sentiment.

        TODO: Threshold calibration based on world-state baseline.
        """
        patterns: list[EmergentPattern] = []
        # Group agents by region
        by_region: dict[str, list[AgentPersona]] = {}
        for a in agents:
            by_region.setdefault(a.region, []).append(a)

        for region, regional_agents in by_region.items():
            negative_count = sum(
                1 for a in regional_agents
                if any(v < -0.5 for v in a.stance.values())
            )
            ratio = negative_count / len(regional_agents) if regional_agents else 0.0
            if ratio > 0.4 and len(regional_agents) >= 5:
                factions = list({a.faction for a in regional_agents if any(v < -0.5 for v in a.stance.values())})
                patterns.append(EmergentPattern(
                    pattern_type="protest",
                    description=f"High negative sentiment in {region} ({ratio:.0%} of agents)",
                    severity=min(ratio, 1.0),
                    involved_agent_count=negative_count,
                    involved_factions=factions,
                    involved_regions=[region],
                ))
        return patterns

    def _detect_movements(self, agents: list[AgentPersona]) -> list[EmergentPattern]:
        """Detect cross-regional social movements.

        TODO: Use topic co-occurrence across regions.
        """
        patterns: list[EmergentPattern] = []
        # Check for shared negative topics across factions
        topic_discontent: dict[str, list[AgentPersona]] = {}
        for a in agents:
            for topic, val in a.stance.items():
                if val < -0.4:
                    topic_discontent.setdefault(topic, []).append(a)

        for topic, discontented in topic_discontent.items():
            factions = list({a.faction for a in discontented})
            regions = list({a.region for a in discontented})
            if len(factions) >= 2 and len(discontented) >= 10:
                patterns.append(EmergentPattern(
                    pattern_type="movement",
                    description=f"Cross-faction discontent on '{topic}' spanning {len(regions)} regions",
                    severity=min(len(discontented) / 50.0, 1.0),
                    involved_agent_count=len(discontented),
                    involved_factions=factions,
                    involved_regions=regions,
                    metadata={"topic": topic},
                ))
        return patterns

    def _detect_alliances(self, agents: list[AgentPersona]) -> list[EmergentPattern]:
        """Detect emergent alliance formations between factions.

        TODO: Use graph analysis to detect tightening inter-faction links.
        """
        # STUB: would analyze social-graph edge density between factions
        return []

    def detect_patterns(self, agents: list[AgentPersona]) -> list[EmergentPattern]:
        """Run all pattern detectors on the current agent population.

        Args:
            agents: Full list of agent states to analyze.

        Returns:
            List of detected emergent patterns, sorted by severity.
        """
        patterns: list[EmergentPattern] = []
        patterns.extend(self._detect_protests(agents))
        patterns.extend(self._detect_movements(agents))
        patterns.extend(self._detect_alliances(agents))
        # Sort by severity descending
        patterns.sort(key=lambda p: p.severity, reverse=True)
        return patterns
