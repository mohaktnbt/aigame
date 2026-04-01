# Project Nexus

**AI-Powered Universal Scenario Simulation Game**

Project Nexus combines natural language gameplay, population-level AI swarm intelligence, and quantitative simulation to create the ultimate "what if" experience across history, pop culture, sci-fi, and fantasy.

## Features

- **Natural Language Actions** — Type what you want to do, AI validates and resolves it
- **Swarm Intelligence** — Thousands of AI agents simulate population-level reactions
- **Probability Preview** — See outcome distributions before committing to actions
- **Dual Output** — Rich narrative text + quantitative dashboards (GDP, military, sentiment)
- **Universal Scenarios** — WW2, Star Wars, Dune, Game of Thrones, Mars Colony, and more
- **Narrative Gravity** — Canonical events exert probabilistic pull, but players can change history
- **Agent Interviews** — Talk to any simulated agent in-character
- **Interactive Map** — Real-time map updates with sentiment heatmaps and border changes

## Architecture

| Service | Tech | Port |
|---------|------|------|
| Frontend | Next.js 15, TypeScript, MapLibre, deck.gl | 3000 |
| API Gateway | Node.js, Fastify, Prisma, Socket.io | 3001 |
| Game Engine | Python, FastAPI, OpenRouter | 5001 |
| Swarm Engine | Python, FastAPI, Neo4j, Zep | 5002 |

**Data Layer**: TimescaleDB, Neo4j, Redis, MinIO, Zep Cloud, OpenRouter

## Quick Start

```bash
# 1. Clone and setup
git clone https://github.com/mohaktnbt/aigame.git
cd aigame
cp .env.example .env  # Fill in API keys

# 2. Start infrastructure
docker compose up -d

# 3. Setup services
./scripts/setup.sh

# 4. Start development servers
cd frontend && npm run dev          # Port 3000
cd api-gateway && npm run dev       # Port 3001
cd game-engine && uv run uvicorn src.main:app --port 5001 --reload
cd swarm-engine && uv run uvicorn src.main:app --port 5002 --reload
```

## Project Structure

```
project-nexus/
├── frontend/          ← Next.js 15 (map, UI, game interface)
├── api-gateway/       ← Fastify (auth, WebSocket, billing)
├── game-engine/       ← FastAPI (game master, narrative, simulation)
├── swarm-engine/      ← FastAPI (MiroFish swarm, agents, sentiment)
├── data/              ← Scenarios, maps, universe rules, seed data
├── scripts/           ← Setup, deploy, migrate utilities
└── docs/              ← Architecture, API spec, game design
```

## Documentation

- [Architecture](docs/architecture.md) — System design and data flow
- [API Specification](docs/api-spec.md) — REST and WebSocket endpoints
- [Game Design](docs/game-design.md) — Mechanics, scenarios, and player experience
- [Agent Architecture](AGENTS.md) — AI agent system design
- [Timeline](TIMELINE.md) — Development phases and progress

## License

Proprietary — All rights reserved.
