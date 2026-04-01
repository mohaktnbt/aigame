"""Project Nexus Game Engine - FastAPI application entry point."""

from __future__ import annotations

import logging
from contextlib import asynccontextmanager
from typing import AsyncIterator

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.llm.openrouter import OpenRouterClient

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Shared resources
# ---------------------------------------------------------------------------
llm_client: OpenRouterClient | None = None


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    """Manage startup and shutdown of shared resources."""
    global llm_client

    # -- Startup --
    logger.info("Starting Project Nexus Game Engine")

    # TODO: Initialize async database connection pool (asyncpg / SQLAlchemy async)
    # TODO: Initialize Redis connection for caching / pub-sub
    llm_client = OpenRouterClient()
    logger.info("LLM client initialised")

    yield

    # -- Shutdown --
    logger.info("Shutting down Project Nexus Game Engine")
    if llm_client is not None:
        await llm_client.close()
    # TODO: Close database pool
    # TODO: Close Redis connection


# ---------------------------------------------------------------------------
# Application
# ---------------------------------------------------------------------------
app = FastAPI(
    title="Project Nexus Game Engine",
    version="0.1.0",
    description="AI-driven geopolitical simulation engine",
    lifespan=lifespan,
)

# -- CORS middleware --
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # TODO: Restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ---------------------------------------------------------------------------
# Health check
# ---------------------------------------------------------------------------
@app.get("/health")
async def health_check() -> dict[str, str]:
    """Return service health status."""
    return {"status": "ok", "service": "nexus-game-engine"}


# ---------------------------------------------------------------------------
# Route modules
# ---------------------------------------------------------------------------
# TODO: Create and include dedicated routers as the API surface grows, e.g.:
#   from src.routes import actions, scenarios, turns
#   app.include_router(actions.router, prefix="/api/v1/actions", tags=["actions"])
#   app.include_router(scenarios.router, prefix="/api/v1/scenarios", tags=["scenarios"])
#   app.include_router(turns.router, prefix="/api/v1/turns", tags=["turns"])
