"""
Nexus Swarm Engine — FastAPI entry point.

MiroFish/OASIS-derived large-scale agent-based social simulation server.
"""

from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.simulation.social_sim import router as simulation_router
from src.agents.agent_pool import router as agents_router
from src.ontology.generator import router as ontology_router
from src.probability.distribution_calculator import router as probability_router


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    """Manage startup and shutdown lifecycle."""
    # --- Startup ---
    # TODO: Initialize Neo4j connection pool
    # TODO: Initialize Redis connection for agent state caching
    # TODO: Pre-load ontology templates
    # TODO: Initialize agent pool with warm-start if checkpoint exists
    print("[nexus] Swarm Engine starting up")
    yield
    # --- Shutdown ---
    # TODO: Flush agent state to persistent storage
    # TODO: Close Neo4j / Redis connections
    print("[nexus] Swarm Engine shutting down")


app = FastAPI(
    title="Nexus Swarm Engine",
    description="Large-scale agent-based social simulation API (MiroFish/OASIS fork)",
    version="0.1.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # TODO: restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── Routers ──────────────────────────────────────────────────────────
app.include_router(simulation_router, prefix="/simulation", tags=["simulation"])
app.include_router(agents_router, prefix="/agents", tags=["agents"])
app.include_router(ontology_router, prefix="/ontology", tags=["ontology"])
app.include_router(probability_router, prefix="/probability", tags=["probability"])


@app.get("/health")
async def health_check() -> dict:
    """Liveness / readiness probe."""
    return {
        "status": "ok",
        "engine": "nexus-swarm-engine",
        "version": "0.1.0",
    }
