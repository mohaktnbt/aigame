# CLAUDE.md — Project Nexus

## What This Project Is

Project Nexus is an AI-powered universal scenario simulation game that combines:

1. **Pax Historia-style gameplay** — browser-based, map-driven, natural language action input, AI-generated narrative consequences
2. **MiroFish swarm intelligence** — thousands of AI agents with individual personalities, memories, and social behaviors simulating population-level emergent responses
3. **Universal scenarios** — not just history but pop culture (Star Wars, Dune, GoT, Back to the Future), sci-fi, fantasy, and any imaginable scenario
4. **Quantitative + Narrative hybrid** — real dashboard numbers (GDP, military, sentiment scores) alongside rich narrative text
5. **Probabilistic realism** — players see outcome probability distributions, not binary success/fail

## Architecture Summary

```
Frontend (Next.js 15 + TypeScript + MapLibre + deck.gl + shadcn/ui + Recharts)
    ↕ WebSocket + REST
API Gateway (Node.js + Fastify + Prisma + Socket.io)
    ↕
Game Engine (Python + FastAPI)
  - Action Validator (Game Master Agent)
  - Turn Processor
  - Narrative Generator
  - Quantitative Simulator
  - Diplomacy Engine
  - Narrative Gravity Engine
  - Realism Validator
    ↕
Swarm Engine (MiroFish/OASIS fork, Python)
  - Ontology Generator
  - Agent Persona Generator
  - Dual-Platform Social Sim
  - Sentiment Aggregator
  - Probability Distribution Calculator
  - Parallel Scenario Branching
  - Agent Interview System
  - Report Agent
    ↕
Data Layer
  - TimescaleDB (game state, time-series metrics) — port 5432
  - Neo4j Community (knowledge graphs, agent relationships) — ports 7474, 7687
  - Redis + BullMQ (session cache, pub/sub, job queues) — port 6379
  - MinIO (map assets, scenario data) — port 9000
  - Zep Cloud (agent long-term memory)
  - OpenRouter (LLM gateway, 400+ models)
```

## Tech Stack

| Layer | Tech |
|-------|------|
| Frontend | Next.js 15, TypeScript, Tailwind, shadcn/ui, MapLibre GL JS, deck.gl, Recharts, Socket.io-client |
| API Gateway | Node.js, Fastify, Prisma (PostgreSQL), Socket.io |
| Game Engine | Python 3.11+, FastAPI, httpx (OpenRouter calls) |
| Swarm Engine | Python 3.11+, MiroFish/OASIS fork, Neo4j driver, Zep SDK |
| LLM | OpenRouter (multi-model: Gemini Flash default, Claude/GPT premium, DeepSeek/Qwen for swarm agents) |
| Token Compression | bear-1.1 (66% context reduction) |
| Auth | Clerk |
| Payments | Stripe |
| Hosting | Hostinger VPS (initial) → AWS Mumbai (scale) |

## Development Workflow

1. **Always read TIMELINE.md first** — know current phase and task
2. **Gap analysis before coding** — check what exists, don't overwrite working code
3. **Commit frequently** with descriptive messages
4. **Update TIMELINE.md** after completing each task
5. **Test incrementally** — each component should work standalone before integration

## Environment Setup

```bash
# Local dev
docker compose up -d  # TimescaleDB, Neo4j, Redis, MinIO

# Frontend
cd frontend && npm install && npm run dev  # port 3000

# API Gateway
cd api-gateway && npm install && npm run dev  # port 3001

# Game Engine
cd game-engine && uv sync && uv run uvicorn src.main:app --port 5001

# Swarm Engine
cd swarm-engine && uv sync && uv run uvicorn src.main:app --port 5002
```

## Build Phases (45-Day Plan)

| Phase | Days | Focus |
|-------|------|-------|
| 0 | 1 | Bootstrap: repo, Docker, CLAUDE.md, VPS setup |
| 1 | 2-5 | Map + game shell: Next.js, MapLibre, basic UI |
| 2 | 6-10 | Game engine: FastAPI, world state, action validation, turn processing, OpenRouter |
| 3 | 11-18 | MiroFish swarm: ontology, agents, sentiment, probability, branching |
| 4 | 19-23 | Pop culture: scenario templates, narrative gravity, universe rules, custom maps |
| 5 | 24-30 | Diplomacy, multiplayer, marketplace, social |
| 6 | 31-35 | Token economy, BYOK, Stripe, creator revenue |
| 7 | 36-45 | Polish: performance, mobile, onboarding, analytics, launch prep |

## Current State

**Phase**: 0 — Bootstrap
**Current Task**: Repository creation and initial setup
**Blockers**: None
**Notes**: See TIMELINE.md for granular progress

## LLM Model Strategy

- **Game Master/Narrator (player-facing)**: OpenRouter → Gemini 3.0 Flash (Pro tier default), Claude Sonnet 4.6 (Max tier)
- **Swarm agents (bulk internal)**: Qwen-plus or DeepSeek V3 (cheapest viable, thousands of calls/turn)
- **Strategic Advisor**: Same as player-facing tier
- **Token compression**: bear-1.1 in pipeline (66% reduction)

## Critical Design Decisions

1. **Monorepo** — all services in one repo for session continuity
2. **Python for game + swarm engines** — AI/ML ecosystem, MiroFish compatibility
3. **Node.js for API gateway** — WebSocket performance, Stripe/Clerk SDKs
4. **TimescaleDB over plain PostgreSQL** — time-series game state queries are core
5. **Neo4j over Zep-only** — production-grade graph DB for knowledge graphs at scale
6. **OpenRouter over direct API keys** — single integration, 400+ models, auto-failover
7. **MapLibre over Mapbox** — open-source, no usage fees at scale
8. **deck.gl for overlays** — sentiment heatmaps, probability visualizations need GPU-accelerated rendering
9. **Fastify over Express** — 2-3x faster, better TypeScript support
10. **Zustand over Redux** — simpler state management, less boilerplate
