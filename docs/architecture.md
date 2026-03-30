# Project Nexus — Architecture

## System Overview

Project Nexus is a distributed system with four main services communicating via REST APIs and WebSockets.

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│   Frontend   │◄───►│ API Gateway  │◄───►│ Game Engine  │
│  (Next.js)   │     │  (Fastify)   │     │  (FastAPI)   │
│  Port 3000   │     │  Port 3001   │     │  Port 5001   │
└──────────────┘     └──────┬───────┘     └──────┬───────┘
                            │                     │
                            │              ┌──────▼───────┐
                            │              │ Swarm Engine │
                            │              │  (FastAPI)   │
                            │              │  Port 5002   │
                            │              └──────┬───────┘
                            │                     │
                     ┌──────▼─────────────────────▼──────┐
                     │          Data Layer               │
                     │  TimescaleDB │ Neo4j │ Redis │    │
                     │  MinIO │ Zep Cloud │ OpenRouter   │
                     └───────────────────────────────────┘
```

## Service Responsibilities

### Frontend (Next.js 15)
- Map rendering (MapLibre GL JS + deck.gl overlays)
- Game UI (action panel, events feed, dashboards)
- Real-time updates via WebSocket
- Scenario marketplace and editor
- Auth (Clerk) and payments (Stripe)

### API Gateway (Fastify)
- Authentication and authorization
- WebSocket management for game sessions
- Token billing and rate limiting
- Request routing to backend services
- Database operations (Prisma + TimescaleDB)

### Game Engine (FastAPI)
- Game Master AI agent (action validation)
- Narrative generation
- Quantitative simulation (GDP, military, tech, sentiment)
- Diplomacy engine
- Turn processing orchestration
- Narrative gravity calculations

### Swarm Engine (FastAPI)
- Population-level agent simulation (MiroFish/OASIS)
- Ontology generation for different universes
- Social simulation (dual-platform)
- Sentiment aggregation
- Probability distribution calculation
- Scenario branching ("what if" analysis)
- Agent interviews
- Knowledge graph management (Neo4j)

## Data Flow

1. Player submits action → API Gateway → Game Engine
2. Game Engine validates with Game Master Agent
3. Game Engine requests probability distribution from Swarm Engine
4. Player sees probabilities, confirms action
5. Game Engine processes turn:
   - Updates quantitative state
   - Requests swarm simulation from Swarm Engine
   - Checks narrative gravity
   - Generates narrative
6. Results broadcast via WebSocket to frontend
7. Frontend updates map, dashboard, events feed

## Database Schema

- **TimescaleDB**: Game sessions, world state snapshots, events, user data, token transactions
- **Neo4j**: Entity relationships, influence networks, knowledge graphs
- **Redis**: Session cache, pub/sub for real-time events, BullMQ job queues
- **MinIO**: Map assets, scenario data files, custom content
- **Zep Cloud**: Agent long-term memory (personality, past interactions)
