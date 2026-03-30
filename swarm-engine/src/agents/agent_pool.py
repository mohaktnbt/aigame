"""
AgentPool — Manages the full population of simulated agents.

Supports batch processing, lifecycle management, and efficient state lookups.
"""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter
from pydantic import BaseModel

from src.agents.persona_generator import AgentPersona, PersonaGenerator

router = APIRouter()


class SpawnRequest(BaseModel):
    """Request to spawn a batch of agents."""
    archetype: str
    faction: str
    region: str
    count: int = 10


class AgentPool:
    """Manages thousands of agents with batch processing and lifecycle control.

    The pool is the single source of truth for agent state during a simulation
    run.  Agents are keyed by agent_id and can be queried by faction, region,
    archetype, or custom filters.

    TODO: Back the pool with Redis for horizontal scaling.
    TODO: Implement checkpointing (snapshot / restore).
    TODO: Add agent retirement and replacement mechanics.
    """

    def __init__(self) -> None:
        self._agents: dict[str, AgentPersona] = {}
        self._generator = PersonaGenerator()

    @property
    def size(self) -> int:
        return len(self._agents)

    def spawn(self, archetype: str, faction: str, region: str, count: int = 1) -> list[str]:
        """Create *count* new agents and add them to the pool.

        Returns:
            List of newly created agent IDs.
        """
        personas = self._generator.generate_batch(archetype, faction, region, count)
        ids: list[str] = []
        for p in personas:
            self._agents[p.agent_id] = p
            ids.append(p.agent_id)
        return ids

    def get(self, agent_id: str) -> AgentPersona | None:
        """Retrieve a single agent by ID."""
        return self._agents.get(agent_id)

    def query(
        self,
        *,
        faction: str | None = None,
        region: str | None = None,
        archetype: str | None = None,
    ) -> list[AgentPersona]:
        """Filter agents by optional criteria."""
        results = list(self._agents.values())
        if faction:
            results = [a for a in results if a.faction == faction]
        if region:
            results = [a for a in results if a.region == region]
        if archetype:
            results = [a for a in results if a.archetype == archetype]
        return results

    def remove(self, agent_id: str) -> bool:
        """Remove an agent from the pool. Returns True if found."""
        return self._agents.pop(agent_id, None) is not None

    def batch_update(self, updates: dict[str, dict[str, Any]]) -> int:
        """Apply partial updates to multiple agents.

        Args:
            updates: Mapping of agent_id -> dict of fields to update.

        Returns:
            Number of agents successfully updated.

        TODO: Validate field names against AgentPersona schema.
        """
        count = 0
        for aid, patch in updates.items():
            agent = self._agents.get(aid)
            if agent is None:
                continue
            # Pydantic v2: create a new model with merged data
            merged = agent.model_dump()
            merged.update(patch)
            self._agents[aid] = AgentPersona(**merged)
            count += 1
        return count

    def all_ids(self) -> list[str]:
        """Return all agent IDs currently in the pool."""
        return list(self._agents.keys())

    def snapshot(self) -> list[dict[str, Any]]:
        """Serialize entire pool state for checkpointing.

        TODO: Write to persistent storage (Redis / disk).
        """
        return [a.model_dump() for a in self._agents.values()]


# ── Singleton for use across the application ────────────────────────
_pool = AgentPool()


@router.post("/spawn")
async def spawn_agents(req: SpawnRequest) -> dict:
    """Spawn a batch of agents into the pool."""
    ids = _pool.spawn(req.archetype, req.faction, req.region, req.count)
    return {"spawned": len(ids), "agent_ids": ids}


@router.get("/count")
async def agent_count() -> dict:
    """Return total number of agents in the pool."""
    return {"count": _pool.size}


@router.get("/{agent_id}")
async def get_agent(agent_id: str) -> dict:
    """Retrieve a single agent by ID."""
    agent = _pool.get(agent_id)
    if agent is None:
        return {"error": "Agent not found"}
    return agent.model_dump()
