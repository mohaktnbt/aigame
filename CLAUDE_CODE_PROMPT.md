# CLAUDE.md — Project Nexus

## What This Project Is

Project Nexus is an AI-powered universal scenario simulation game that surpasses Pax Historia (YC W26, 35K DAU, 193B tokens/month) by combining:

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
  - Action Validator (Game Master Agent) — NL parsing → void/backfire/approve
  - Turn Processor — orchestrates all agents per turn
  - Narrative Generator — rich event text
  - Quantitative Simulator — GDP, military, tech, sentiment calculations
  - Diplomacy Engine — treaty evaluation against agent goals
  - Narrative Gravity Engine — canonical events exert probabilistic pull
  - Realism Validator — configurable per universe (Force is real in Star Wars)
    ↕
Swarm Engine (MiroFish/OASIS fork, Python)
  - Ontology Generator — genre-adaptive entity/relationship types from seed docs
  - Agent Persona Generator — Big Five personality, stance, influence, schedule
  - Dual-Platform Social Sim — Twitter-like + Reddit-like parallel simulation
  - Sentiment Aggregator — per-faction, per-region sentiment scores
  - Probability Distribution Calculator — outcome likelihood for player actions
  - Parallel Scenario Branching — "what if" lightweight sims before committing
  - Agent Interview System — player talks to any simulated agent in character
  - Report Agent — InsightForge + PanoramaSearch + InterviewAgents
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
| Hosting | Hostinger VPS 168.231.103.49 (initial) → AWS Mumbai (scale) |
| Repo | GitHub mohaktnbt/project-nexus |

## File Structure

```
project-nexus/
├── CLAUDE.md                          ← YOU ARE HERE
├── TIMELINE.md                        ← Check before every session
├── AGENTS.md                          ← Agent architecture reference
├── TODO-MANUAL.md                     ← Manual tasks
├── docker-compose.yml
├── .env.example
├── frontend/                          ← Next.js 15
│   └── src/
│       ├── app/                       ← Pages (layout, play/[gameId], explore, create, profile)
│       ├── components/
│       │   ├── map/                   ← GameMap, SentimentOverlay, BorderLayer, ProbabilityOverlay
│       │   ├── game/                  ← ActionPanel, EventsFeed, Timeline, QuantDashboard, DiplomacyChat, AgentNetwork, ProbabilityDisplay
│       │   ├── editor/               ← ScenarioEditor, MapEditor, FactionEditor, UniverseRulesEditor
│       │   └── marketplace/          ← ScenarioCard, ScenarioGrid, SearchFilter
│       ├── hooks/                     ← useGameSocket, useGameState, useTokens, useSwarmData
│       ├── lib/                       ← api, socket, types
│       └── stores/                    ← gameStore, userStore (zustand)
├── api-gateway/                       ← Node.js + Fastify
│   └── src/
│       ├── routes/                    ← auth, games, scenarios, tokens, users
│       ├── middleware/                ← auth, rateLimit, tokenBilling
│       ├── services/                  ← stripe, openrouter, byok
│       └── websocket/                 ← gameSocket
├── game-engine/                       ← Python + FastAPI
│   └── src/
│       ├── models/                    ← world_state, nation, actor, event, scenario
│       ├── agents/                    ← game_master, narrator, advisor, diplomat
│       ├── simulation/                ← quantitative, diplomacy, turn_processor, narrative_gravity
│       └── llm/                       ← openrouter, prompts, compression
├── swarm-engine/                      ← MiroFish/OASIS fork
│   └── src/
│       ├── ontology/                  ← generator, templates (historical, scifi, fantasy)
│       ├── agents/                    ← persona_generator, agent_pool, interviewer, archetypes
│       ├── simulation/                ← social_sim, sentiment, emergence, branching
│       ├── graph/                     ← neo4j_client, graphrag
│       ├── memory/                    ← zep_client, memory_factory
│       ├── probability/               ← distribution_calculator, option_ranker
│       └── reports/                   ← report_agent
├── data/
│   ├── maps/                          ← world_borders.geojson, world_cities.json, custom/
│   ├── scenarios/templates/           ← historical/, modern/, pop_culture/, scifi/
│   ├── universe_rules/                ← star_wars.json, dune.json, got.json
│   └── seed/                          ← nations_base.json, historical_context/
├── scripts/                           ← setup.sh, deploy.sh, migrate.sh, seed-data.sh
└── docs/                              ← architecture.md, api-spec.md, game-design.md
```

## Core Game Loop

```
1. Player selects SCENARIO (preset) — "Star Wars: Battle of Yavin" or "What if USSR never collapsed"
2. Player chooses FACTION to control
3. Player types ACTION in natural language — "Redirect resources to evacuate Yavin 4 civilians"
4. GAME MASTER validates action (void/backfire/approve) with explanation
5. SWARM ENGINE simulates agent reactions:
   → Thousands of agents (citizens, leaders, military, media) react independently
   → Emerge: sentiment shifts, protest likelihood, coup probability, alliance changes
   → Calculate PROBABILITY DISTRIBUTION of outcomes
6. Player sees: "45% diplomatic protest, 30% military mobilization, 20% economic retaliation, 5% surprise alliance"
7. Player confirms or modifies action
8. TURN RESOLVES:
   → NARRATIVE: Rich AI-generated text describing events
   → QUANTITATIVE: Dashboard updates (GDP, military, tech, sentiment charts)
   → MAP: Borders shift, sentiment heatmap updates, new markers appear
   → AGENT NETWORK: Influence graph updates
9. Player can:
   → TIME-JUMP forward (variable: days to years)
   → CHAT with AI nations (diplomacy)
   → INTERVIEW any simulated agent
   → Fork into "WHAT-IF" branch
10. Repeat
```

## Key Differentiating Concepts

### Narrative Gravity
Famous canonical events exert probabilistic pull but don't deterministically fire. Each turn, `adjusted_probability = base_probability * player_action_modifier * swarm_sentiment_modifier`. Players see a "narrative tension" indicator when approaching canonical moments. They can push against gravity (prevent the Battle of Yavin) or ride it (accelerate it under different terms).

### Configurable Realism Validation
Each scenario defines `universe_rules` that the Game Master Agent respects:
- Historical: Earth physics + documented capabilities of the era
- Star Wars: Force is real, hyperspace travel exists, lightsabers work
- Dune: Prescience is valid, shields attract worms, spice enables interstellar travel
- Speculative: Broader latitude, physics-based constraints only

### Dual-Layer Game State
Every turn produces BOTH:
- **Narrative output**: "The Senate erupted in protest as your trade embargo took effect. Senator Organa led a coalition demanding sanctions reversal..."
- **Quantitative output**: `{ gdp_change: -2.3%, military_readiness: +5%, public_sentiment: -12%, diplomatic_relations.coruscant: -18 }`

### Probability-Before-Commitment
Before executing an action, player sees outcome probability distribution from lightweight swarm simulation. Player can modify action based on this intelligence, or proceed accepting the risks. This replaces Pax Historia's opaque "unrealistic" rejections with transparent probabilistic assessment.

## Development Workflow

1. **Always read TIMELINE.md first** — know current phase and task
2. **Work in tmux sessions** for persistence on VPS
3. **Run `printf '\e[?2004l'`** to disable bracketed paste in terminal
4. **Gap analysis before coding** — check what exists, don't overwrite working code
5. **Commit frequently** with descriptive messages
6. **Update TIMELINE.md** after completing each task
7. **Test incrementally** — each component should work standalone before integration

## Environment Setup

```bash
# VPS access
ssh mohak@168.231.103.49

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

## Environment Variables (.env)

```
# LLM
OPENROUTER_API_KEY=
OPENROUTER_BASE_URL=https://openrouter.ai/api/v1

# Database
DATABASE_URL=postgresql://nexus:nexus@localhost:5432/nexus
NEO4J_URI=bolt://localhost:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=nexus

# Redis
REDIS_URL=redis://localhost:6379

# Agent Memory
ZEP_API_KEY=

# Auth
CLERK_SECRET_KEY=
NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY=

# Payments
STRIPE_SECRET_KEY=
STRIPE_WEBHOOK_SECRET=

# Storage
MINIO_ENDPOINT=localhost:9000
MINIO_ACCESS_KEY=nexus
MINIO_SECRET_KEY=nexus123
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
- **Token compression**: bear-1.1 in pipeline (66% reduction, quality improvement validated by Pax Historia's 268K-vote arena)

## Critical Design Decisions

1. **Monorepo** — all services in one repo for Claude Code session continuity
2. **Python for game + swarm engines** — AI/ML ecosystem, MiroFish compatibility
3. **Node.js for API gateway** — WebSocket performance, Stripe/Clerk SDKs
4. **TimescaleDB over plain PostgreSQL** — time-series game state queries are core
5. **Neo4j over Zep-only** — production-grade graph DB for knowledge graphs at scale
6. **OpenRouter over direct API keys** — single integration, 400+ models, auto-failover
7. **MapLibre over Mapbox** — open-source, no usage fees at scale
8. **deck.gl for overlays** — sentiment heatmaps, probability visualizations need GPU-accelerated rendering
9. **Fastify over Express** — 2-3x faster, better TypeScript support
10. **Zustand over Redux** — simpler state management, less boilerplate

## Pax Historia Intelligence (For Competitive Reference)

- Uses OpenRouter as LLM gateway, 29 models, Gemini 3.0 Flash as Pro default
- Processes 193B tokens/month, bear-1.1 compression improved quality AND reduced cost
- Token economy: 0.2 tokens/day free, purchase via Stripe/crypto, BYOK via Patron subscription
- Creator economy: 10% token commission on presets with 150+ rounds
- Database-free game state (JSON files) — we use TimescaleDB for richer querying
- 3-agent system: Game Master, Advisor, Diplomat — we extend with swarm layer
- No quantitative simulation, no multiplayer, no pop culture — our key advantages

## MiroFish Intelligence (For Integration Reference)

- 5-stage pipeline: Ontology → GraphRAG → Environment → Simulation → Report
- OASIS engine handles env logic, recommendation systems, time engine, GPU inference distribution
- 23 social action types across dual platforms (Twitter-like + Reddit-like)
- Zep Cloud for agent memory (factory pattern, batch buffering, IPC interviews)
- 40-round run ≈ 2-4M tokens on 70B model
- Key: use cheapest model for swarm, save premium models for player-facing output
