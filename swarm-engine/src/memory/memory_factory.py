"""
MemoryFactory — Factory pattern for creating memory backends.

Supports pluggable memory backends so the engine can run with Zep,
Redis, or a simple in-memory store depending on deployment configuration.
"""

from __future__ import annotations

from enum import Enum
from typing import Any, Protocol


class MemoryBackend(Protocol):
    """Protocol that all memory backends must implement."""

    async def store_memory(
        self, agent_id: str, content: str, turn: int, importance: float = 0.5, tags: list[str] | None = None,
    ) -> Any: ...

    async def retrieve_memories(
        self, agent_id: str, limit: int = 10, min_importance: float = 0.0,
    ) -> list[Any]: ...

    async def search_memories(
        self, agent_id: str, query: str, limit: int = 5,
    ) -> list[Any]: ...


class BackendType(str, Enum):
    ZEP = "zep"
    REDIS = "redis"
    IN_MEMORY = "in_memory"


class MemoryFactory:
    """Creates memory backend instances based on configuration.

    Usage:
        factory = MemoryFactory()
        backend = factory.create("zep", base_url="http://zep:8000")

    TODO: Add Redis-backed memory backend.
    TODO: Add persistent SQLite backend for development.
    """

    def create(
        self,
        backend_type: str | BackendType = BackendType.IN_MEMORY,
        **kwargs: Any,
    ) -> MemoryBackend:
        """Create a memory backend instance.

        Args:
            backend_type: Which backend to use.
            **kwargs: Backend-specific configuration.

        Returns:
            An object conforming to the MemoryBackend protocol.

        Raises:
            ValueError: If the backend type is not supported.
        """
        bt = BackendType(backend_type) if isinstance(backend_type, str) else backend_type

        if bt == BackendType.ZEP:
            from src.memory.zep_client import ZepMemoryClient
            return ZepMemoryClient(**kwargs)  # type: ignore[return-value]

        if bt == BackendType.REDIS:
            # TODO: Implement RedisMemoryClient
            raise NotImplementedError("Redis memory backend not yet implemented")

        if bt == BackendType.IN_MEMORY:
            from src.memory.zep_client import ZepMemoryClient
            # ZepMemoryClient stub uses in-memory storage by default
            return ZepMemoryClient(**kwargs)  # type: ignore[return-value]

        raise ValueError(f"Unknown memory backend: {backend_type}")
