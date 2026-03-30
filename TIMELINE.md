# TIMELINE.md — Project Nexus Development Timeline

## Phase 0: Bootstrap (Day 1)

### Tasks
- [x] Create GitHub repository
- [x] Upload research documents
- [x] Create CLAUDE.md
- [x] Create TIMELINE.md
- [x] Create AGENTS.md
- [x] Create TODO-MANUAL.md
- [x] Set up docker-compose.yml (TimescaleDB, Neo4j, Redis, MinIO)
- [x] Create .env.example
- [x] Scaffold frontend (Next.js 15)
- [x] Scaffold API Gateway (Fastify)
- [x] Scaffold Game Engine (FastAPI)
- [x] Scaffold Swarm Engine (FastAPI)
- [x] Create data directory with seed templates
- [x] Create utility scripts
- [ ] Verify all services start locally

### Status: In Progress
### Started: 2026-03-30
### Completed: —

---

## Phase 1: Map + Game Shell (Days 2-5)

### Tasks
- [ ] MapLibre GL JS integration with world map
- [ ] Basic game UI layout (map + sidebar + action panel)
- [ ] shadcn/ui component library setup
- [ ] Game creation flow (select scenario → choose faction)
- [ ] Action input panel (natural language text box)
- [ ] Events feed component
- [ ] Basic WebSocket connection (frontend ↔ API gateway)
- [ ] Zustand game state store
- [ ] Basic routing (home, play, explore, create, profile)

### Status: Not Started
### Started: —
### Completed: —

---

## Phase 2: Game Engine (Days 6-10)

### Tasks
- [ ] World state model (nations, actors, resources, relationships)
- [ ] Game Master Agent — NL action parsing and validation
- [ ] Turn processor — orchestrate action resolution
- [ ] Narrative Generator — rich event text via OpenRouter
- [ ] Quantitative Simulator — GDP, military, tech, sentiment calculations
- [ ] OpenRouter integration with model routing
- [ ] Turn history and state snapshots
- [ ] API endpoints for game operations

### Status: Not Started
### Started: —
### Completed: —

---

## Phase 3: MiroFish Swarm (Days 11-18)

### Tasks
- [ ] Ontology Generator — genre-adaptive entity/relationship types
- [ ] Agent Persona Generator — Big Five personality, stance, influence
- [ ] Dual-Platform Social Sim (Twitter-like + Reddit-like)
- [ ] Sentiment Aggregator — per-faction, per-region scores
- [ ] Probability Distribution Calculator
- [ ] Parallel Scenario Branching ("what if" sims)
- [ ] Agent Interview System
- [ ] Neo4j knowledge graph integration
- [ ] Zep Cloud agent memory integration
- [ ] Report Agent (InsightForge + PanoramaSearch)

### Status: Not Started
### Started: —
### Completed: —

---

## Phase 4: Pop Culture + Scenarios (Days 19-23)

### Tasks
- [ ] Scenario template system
- [ ] Narrative Gravity Engine
- [ ] Universe rules system (configurable realism)
- [ ] Star Wars scenario + custom map
- [ ] Dune scenario + custom map
- [ ] Game of Thrones scenario + custom map
- [ ] Historical scenario templates (WW2, Cold War, etc.)
- [ ] Custom map editor basics

### Status: Not Started
### Started: —
### Completed: —

---

## Phase 5: Diplomacy + Multiplayer (Days 24-30)

### Tasks
- [ ] Diplomacy Engine — treaty proposals, evaluation
- [ ] AI nation chat interface
- [ ] Multiplayer lobby and session management
- [ ] Scenario marketplace (browse, search, rate)
- [ ] Scenario sharing and publishing
- [ ] Social features (profiles, follows, activity feed)

### Status: Not Started
### Started: —
### Completed: —

---

## Phase 6: Token Economy (Days 31-35)

### Tasks
- [ ] Token billing system
- [ ] Stripe payment integration
- [ ] BYOK (Bring Your Own Key) support
- [ ] Creator revenue system (10% commission)
- [ ] Usage analytics and dashboard
- [ ] Free tier limits and upgrade flow

### Status: Not Started
### Started: —
### Completed: —

---

## Phase 7: Polish + Launch (Days 36-45)

### Tasks
- [ ] Performance optimization (lazy loading, caching, CDN)
- [ ] Mobile responsive design
- [ ] Onboarding tutorial
- [ ] Analytics integration
- [ ] Error handling and monitoring
- [ ] Security audit
- [ ] Load testing
- [ ] Launch checklist and deployment

### Status: Not Started
### Started: —
### Completed: —
