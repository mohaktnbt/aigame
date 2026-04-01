"""
ZepMemoryClient — Interface to Zep for agent long-term memory.

Zep provides temporal knowledge graphs and semantic search over agent
memories, enabling agents to recall past events, conversations, and
experiences with appropriate decay and relevance weighting.
"""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel


class Memory(BaseModel):
    """A single memory record."""
    memory_id: str
    agent_id: str
    content: str
    turn_created: int
    importance: float  # 0-1
    tags: list[str] = []
    metadata: dict[str, Any] = {}


class ZepMemoryClient:
    """Client for the Zep memory service.

    Provides store, retrieve, and search operations for agent long-term
    memory.  Memories are keyed by agent_id and support both temporal
    and semantic retrieval.

    TODO: Connect to actual Zep service via httpx.
    TODO: Implement memory importance scoring.
    TODO: Add memory consolidation (merge similar memories).
    TODO: Implement forgetting curve / decay.
    """

    def __init__(self, base_url: str = "http://localhost:8000") -> None:
        self._base_url = base_url
        # In-memory stub storage
        self._store: dict[str, list[Memory]] = {}

    async def store_memory(
        self,
        agent_id: str,
        content: str,
        turn: int,
        importance: float = 0.5,
        tags: list[str] | None = None,
    ) -> Memory:
        """Store a new memory for an agent.

        Args:
            agent_id: The agent this memory belongs to.
            content: Natural language memory content.
            turn: Simulation turn when the memory was formed.
            importance: How important this memory is (0-1).
            tags: Optional tags for categorization.

        Returns:
            The created Memory record.

        TODO: Call Zep API to persist memory.
        """
        import uuid
        memory = Memory(
            memory_id=str(uuid.uuid4()),
            agent_id=agent_id,
            content=content,
            turn_created=turn,
            importance=importance,
            tags=tags or [],
        )
        self._store.setdefault(agent_id, []).append(memory)
        return memory

    async def retrieve_memories(
        self,
        agent_id: str,
        limit: int = 10,
        min_importance: float = 0.0,
    ) -> list[Memory]:
        """Retrieve recent memories for an agent.

        Args:
            agent_id: The agent whose memories to retrieve.
            limit: Maximum number of memories to return.
            min_importance: Filter out memories below this importance.

        Returns:
            List of Memory records, most recent first.

        TODO: Call Zep API with temporal ordering.
        """
        memories = self._store.get(agent_id, [])
        filtered = [m for m in memories if m.importance >= min_importance]
        return sorted(filtered, key=lambda m: m.turn_created, reverse=True)[:limit]

    async def search_memories(
        self,
        agent_id: str,
        query: str,
        limit: int = 5,
    ) -> list[Memory]:
        """Semantic search over an agent's memories.

        Args:
            agent_id: The agent whose memories to search.
            query: Natural language search query.
            limit: Maximum results.

        Returns:
            List of semantically relevant Memory records.

        TODO: Use Zep's built-in vector search.
        TODO: Fallback to simple keyword matching.
        """
        # STUB: return most recent memories as placeholder
        return await self.retrieve_memories(agent_id, limit=limit)
