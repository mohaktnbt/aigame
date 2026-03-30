# PROJECT NEXUS: AI-Powered Universal Scenario Simulation Game
## Complete Research, Competitive Intelligence & Claude Code Execution Plan

---

# SECTION A: EXECUTIVE VISION & PRODUCT DIFFERENTIATION

## A.1 Core Concept: From Historical Sandbox to Universal Scenario Engine

Pax Historia has established itself as a pioneering AI-native grand strategy platform, achieving 35,000 daily active users processing 100+ billion tokens weekly across 4.87 million monthly API requests. Its core innovation — natural language action input with AI-generated narrative consequences — has validated market demand for emergent storytelling in strategic gaming. However, Pax Historia's deliberate constraint to historical scenarios creates an artificial ceiling on creative possibility space that our architecture explicitly transcends.

**Project Nexus** treats any narrative framework — historical, fictional, or speculative — as valid simulation substrate. This expansion is technically enabled by MiroFish's multi-agent simulation architecture, which demonstrates that structured text from any domain can seed functional agent populations with coherent behavioral dynamics. The transformation requires three architectural shifts:

1. **Genre-adaptive ontology generation** — recognizing that Dune's spice economics and Cold War diplomacy both reduce to influence networks and resource competition
2. **Archetypal agent persona templates** — the "reluctant leader" and "corrupt advisor" transcending era
3. **Configurable realism validation** — where "the Force" is realistic in Star Wars scenarios and "prescience" is realistic in Dune

The technical foundation inherits Pax Historia's proven infrastructure (Next.js frontend, OpenRouter multi-model routing, Firestore/Supabase hybrid persistence) while extending simulation depth through MiroFish's OASIS-based agent orchestration. The critical differentiator is data-driven scenario generation: where Pax Historia requires manual research and hardcoded historical knowledge, our system constructs dynamic world-models from seed documents, enabling scenario creation in days rather than months.

## A.2 Pop Culture Integration: Universe-Specific Simulation Mechanics

Each exemplar universe carries distinct simulation logics requiring systemic adaptation:

### Star Wars
- **Core Mechanics**: Mystical power systems (Force), asymmetric warfare, destiny-driven narrative
- **Simulation Challenges**: Multi-scale conflict (individual duels to galactic fleet actions), factional politics across planetary/sector/imperial levels
- **MiroFish Adaptation**: Agent utility functions incorporating Force-sensitivity; hyperspace topology for logistics modeling; prophecy as probabilistic future-state visibility

### Dune
- **Core Mechanics**: Resource-constrained desert ecology, political intrigue, prescient planning
- **Simulation Challenges**: Spice economics as network-constrained resource; Butlerian Jihad prohibition on thinking machines; multi-generational Bene Gesserit planning
- **MiroFish Adaptation**: Ecological system modeling with water/spice interdependence; agent reasoning with explicit lookahead for prescient characters; feudal obligation networks

### Back to the Future
- **Core Mechanics**: Temporal paradox, timeline branching, causal loop management
- **Simulation Challenges**: Multiple timeline state maintenance; paradox severity evaluation; consequence propagation delays
- **MiroFish Adaptation**: Directed acyclic graph timeline representation; agent belief states across branches; grandfather paradox detection and resolution strategies

### Additional Universes (Game of Thrones, Lord of the Rings, The Expanse, Foundation, 1984, Hunger Games)
- Each universe's "rules of physics/society" encoded as ontology constraints
- MiroFish knowledge graph construction from seed documents (wiki articles, novels, films) enables rapid scenario instantiation
- Agents maintain internal consistency with source material while enabling player-driven divergence

## A.3 "Narrative Gravity" — Player Agency in Living Famous Narratives

Critical to our approach is the distinction between canonical fidelity and player agency. Our system implements **"narrative gravity"** — famous events exert probabilistic pull without deterministic enforcement.

Example: A player commanding Rebel forces at the Battle of Yavin encounters high probability for Death Star destruction (canon outcome) but can shift distributions through granular intervention: disabling rather than destroying, prioritizing civilian evacuation, or attempting Imperial officer defection. MiroFish's parallel scenario branching explores these possibility spaces, presenting players with probability-weighted option sets rather than binary success/failure.

Strategic granularity example: A player as Rebel Alliance strategist at Yavin might propose actions impossible in traditional interfaces — "redirect resources to evacuate Yavin 4's civilian population, accepting higher military risk" or "attempt to turn Imperial officers through targeted propaganda exploiting Tarkin command-style dissatisfaction." Each triggers MiroFish multi-agent simulation, with Rebel commanders, Imperial officers, and neutral parties responding per their established personas and situational assessments.

The temporal structure of MiroFish simulation rounds (recommended <40 rounds for initial runs, each round representing agent interaction iterations) creates genuine suspense and strategic patience. A player's Round 1 action (sabotaging Imperial communications) may not produce visible outcomes until Round 8 (coordinated Rebel strike exploiting confusion), with intermediate rounds showing incremental developments: increased Imperial security measures, command dispute rumors, conscript desertions. This planting-and-harvest dynamic mirrors real-world decision-making under uncertainty.

---

# SECTION B: PAX HISTORIA — COMPLETE DEEP ANALYSIS

## B.1 What Pax Historia Is

Pax Historia is a browser-based, AI-powered alternate-history sandbox game. YC W26 batch. Players pick a country, a moment in time, and rewrite history via natural language. The AI simulates how other countries/actors respond. 35,000+ DAUs, 20M+ rounds played, 100B+ tokens processed per week, 193B tokens/month through OpenRouter.

## B.2 Core Game Loop: Decisional Pause → Action → Time-Jump → Resolution

```
Phase 1: DECISIONAL PAUSE — Frozen world-state assessment; unlimited player deliberation time
  → Real-time map synchronization; AI advisor consultation; historical event review
Phase 2: PLAYER ACTION — Natural language declaration of strategic intentions  
  → Intent classification; entity extraction; multi-action batching
Phase 3: TIME-JUMP — Forward simulation leap; AI processes all actor behaviors
  → Variable duration (days to years) based on action complexity
Phase 4: EVENT RESOLUTION — Narrative summary with map state updates
  → AI-generated consequence description; territorial visualization; new decision context
```

Time-jump flexibility is strategically significant: shorter skips (1 week) preserve tactical control for precise operations; longer skips enable "autopilot" execution of extended initiatives. The risk-reward dynamic between action detail and skip safety creates strategic depth — detailed planning enables longer jumps without AI "inventing" unrequested operations.

## B.3 Technical Architecture (Reverse-Engineered)

### Frontend
- Browser-based (no downloads)
- Interactive MAP rendering (point-and-polygon abstraction where major entities appear as labeled nodes with territorial influence radiating outward)
- Action panel (text input for player actions)
- Events panel (AI-generated narrative events)
- Timeline panel (turn progression with time-jump controls)
- Diplomacy panel (chat interface with AI nations)
- Preset editor (map editor + context editor for creators)

### Backend & Infrastructure
- Next.js frontend
- OpenRouter as the LLM gateway (routes to 29+ models)
- Firestore/Supabase hybrid persistence
- Token economy system (Stripe payments, crypto payments)
- Preset/scenario storage system (user-generated content)
- Session state management (conversation history per game)
- bear-1.1 token compression in the pipeline (reduces context by ~66%, actually improved quality)

### AI Architecture (3-Agent System from open-source clone analysis)
1. **Game Master Agent** — Validates player actions for plausibility (anachronisms, geographic constraints, historical context)
2. **Strategic Advisor Agent** — Provides strategic counsel to the player (token-hungry — can burn more tokens than entire round of diplomatic negotiations)
3. **Diplomacy Agent** — Handles multi-party diplomatic conversations

### Natural Language Action Processing Pipeline

| Stage | Function | Model Requirements |
|-------|----------|-------------------|
| Syntactic parsing | Action verb identification, target entity recognition, parameter extraction | Fast classification models (Light tier) |
| Semantic analysis | Colloquial expression mapping to game concepts, metaphor interpretation | Context-aware embedding models |
| Contextual validation | Feasibility assessment against current world state | Scenario-knowledgeable models (Pro/Max tier) |
| Consequence generation | Plausible outcome synthesis with narrative rendering | High-capability models (Max tier, thinking tokens) |

Linguistic variety handling: "invade France," "launch military offensive against French Republic," "send armies across the border to seize Paris," and "begin hostile operations against our western neighbor" must all resolve to similar simulation behaviors with nuance preserved in diplomatic perception and casus belli generation.

### Realism Validation: Voiding vs. Backfire Mechanics

| Mechanism | Trigger | Player Experience | Difficulty Modulation |
|-----------|---------|-------------------|----------------------|
| **Voiding** | "Outrageously unrealistic" actions — physically/logically impossible | Action prevented with explanatory narrative | Threshold varies: maximally permissive on Very Easy, strict on Impossible |
| **Backfire** | Marginally feasible actions with inadequate preparation or poor timing | Attempt proceeds but produces opposite-of-intended consequences | Probability and severity scale with difficulty |

### AI Models Used (via OpenRouter)
- Light tier: Grok 4.1 Fast (cheapest, lowest quality)
- Pro tier: Gemini 3.0 Flash (default, best value, 1000 thinking tokens)
- Max tier: Gemini 2.5 Pro (expensive, 10,000 thinking tokens)
- 26 experimental models including: Claude Sonnet 4.5/4.6, Opus 4.6, Haiku 4.5, GPT-5.1, Grok-4.1 Fast, DeepSeek 3/3.1/3.2, GLM 4.6, Kimi k2
- Free models rotate based on provider trial periods
- Patron models: Canopy Wave, Chutes (exclusive)

### Data Architecture (from open-source clone)
- Database-free architecture for game state — all state stored in JSON files
- nations_v2.json — Nation definitions, attributes, capabilities
- historical_roadmaps.json — Historical context per nation per era
- hoi4_map.json — Geographic data (Hearts of Iron 4 map data)
- cities.json — City locations and metadata

## B.4 Monetization Architecture

### Token Economy
- 1 free token on signup, 0.2 tokens/day (cap 1.2, expires if unused)
- Token purchase packs ($6 basic, up to $56/mo subscriptions via Stripe)
- Pax Patron subscription: BYOK via OpenRouter + 5 Creator Reward Tokens/month
- Cryptocurrency accepted for most purchases

### Creator Economy
- Preset authors earn 10% of tokens spent on their presets (if 150+ rounds played)
- Creator Reward Tokens from Patron subscriptions stack and never expire
- Collaborator share ratios chosen by preset owner

### Pax Arena (Model Benchmarking)
- Users vote on AI quality in A/B comparisons, earning 0.03 tokens/vote
- 268,000+ votes accumulated across 27 models
- Desktop only (no mobile voting yet)

### Cost Structure
- Estimated 40-60% blended margin on AI inference resale
- Light tier: fattest margin (Gemini 2.0 Flash at $0.10/M input)
- Max tier: likely breaks even or loses money
- Free models: loss-leaders designed to convert users to paid

## B.5 Pax Historia Strengths
- Massive creative freedom (any scenario imaginable within history)
- Strong community/UGC ecosystem (4,000+ presets with 50+ plays each ≈ 200,000+ player-hours)
- Multi-model support gives users choice of quality vs. cost
- BYOK option for power users
- Creator economy incentivizes content creation
- Browser-based = zero friction onboarding
- Validated YC company with organic growth
- Forking and version history enable collaborative improvement

## B.6 Pax Historia Weaknesses
- **No quantitative simulation** — no GDP numbers, army sizes, population stats. Everything is narrative-only. AI writes "economic ties strengthened" instead of measurable metrics.
- **AI inconsistency** — models sometimes ignore orders, parrot back player words, or are too easily persuaded
- **No persistence/memory** — AI doesn't deeply remember previous turns beyond context window
- **Token costs escalate rapidly** in long games (context grows with each turn)
- **Map is relatively static** — simple border changes, no rich terrain simulation
- **No multiplayer (PvP)** — only player vs. AI
- **No real economic/military/technological simulation layer**
- **No visual combat or tactical layer**
- **Pacing issues** — heavy models cause long wait times
- **Opaque validation** — "unrealistic" rejections with insufficient explanation frustrate players

---

# SECTION C: MIROFISH — SWARM INTELLIGENCE ENGINE

## C.1 What MiroFish Is

MiroFish is an open-source multi-agent swarm intelligence engine for predictive simulation. Built by Guo Hangjiang (college senior, Beijing University of Posts and Telecommunications) in 10 days. Backed by Shanda Group ($4M commitment). 3.9k GitHub stars, 495 forks. Powered by OASIS framework (CAMEL-AI). Can scale to 1 million agents.

## C.2 5-Stage Pipeline Architecture

```
STAGE 1: ONTOLOGY GENERATION
  → LLM analyzes input documents
  → Generates 10 entity types + 10 relationship types
  → Creates custom Pydantic models dynamically
  → Two-tier structure: 8 specific types from content + 2 fallback (Person, Organization)

STAGE 2: GRAPHRAG CONSTRUCTION
  → Documents chunked (500 chars, 50 overlap)
  → Sent to Zep Cloud in batches
  → Entities extracted: people, orgs, events, concepts
  → Knowledge graph built with individual + group memory

STAGE 3: ENVIRONMENT SETUP
  → Entity-relationship extraction from knowledge graph
  → Persona generation (hundreds to thousands of agents)
  → Each agent: unique personality, opinion bias, reaction speed, influence level, activity schedule
  → Environment configuration agent injects simulation parameters
  → Long-term memory per agent via Zep Cloud

STAGE 4: SIMULATION RUN
  → Dual-platform parallel simulation (Twitter-like + Reddit-like)
  → 23 social action types (follow, comment, repost, like, mute, search, etc.)
  → Dynamic time-based agent activation schedules
  → Real-time logging to JSONL files
  → Auto-parsing of prediction requirements
  → Dynamic temporal memory updates
  → Can scale to 1 million agents

STAGE 5: REPORT GENERATION
  → ReportAgent with rich toolset
  → Three-tier retrieval:
    - InsightForge (deep dive into specific aspects)
    - PanoramaSearch (full scope overview)
    - InterviewAgents (real-time agent interrogation)
  → Structured prediction reports
  → Deep interaction: query any agent post-simulation
```

## C.3 Tech Stack
- Backend: Python 3.11-3.12
- Frontend: Vue.js
- Package manager: uv (Python), npm (Node)
- Knowledge Graph: Zep Cloud (or Neo4j in offline fork, or Mem0 Graph Memory)
- LLM: Any OpenAI-compatible API (default: Alibaba DashScope qwen-plus)
- Simulation engine: OASIS (CAMEL-AI) — handles environment logic, recommendation systems, time engine, scalable inference across GPUs
- Memory: Zep Cloud for persistent agent memory with graph support
- Memory patterns: factory pattern (memory_factory.py), batch buffering with retries, IPC-based agent interviews
- Deployment: Docker support, ports 3000 (frontend) / 5001 (backend)

## C.4 Key Engineering Decisions
1. **Async task management** — concurrent simulation across dual platforms
2. **Batch LLM calls with retry** — resilient inference at scale
3. **Dual-platform parallel simulation** — Twitter-like AND Reddit-like simultaneously
4. **Hierarchical key design for storage** — table_name:record_id pattern
5. **Graceful degradation** — simulation continues even if individual agent calls fail
6. **Database isolation** — per-simulation data separation prevents contamination

## C.5 MiroFish Cost Profile
- 40-round runs on Llama-3.3-70B-Instruct: 2-4M tokens
- Regolo.ai pay-as-you-go pricing enables sub-50% cost vs. raw LLM usage
- Cheapest viable model (Qwen-plus or DeepSeek) for agent swarm since we need thousands of calls per turn
- Token compression further reduces costs

## C.6 How MiroFish Transforms Our Game

| Capability | Technical Implementation | Player Experience |
|-----------|------------------------|-------------------|
| **Parallel scenario branching** | Multiple simulation threads explore agent response patterns to candidate actions | Informed risk assessment rather than guesswork about hidden systems |
| **Simulation visibility** | ReportAgent synthesis of agent deliberations and interaction moments | Understanding WHY outcomes occurred; strategic learning from failure |
| **Outcome distribution exploration** | Lightweight simulation for option ranking; full simulation for selected action | Rapid option evaluation without committing; "what if" exploration |
| **Probabilistic realism** | Replaces binary valid/invalid with graduated likelihood estimates | Players understand why actions are risky; can attempt low-probability initiatives with informed consent |
| **Population-level responses** | Instead of one LLM guessing "how France reacts," simulate thousands of French citizens, politicians, military leaders, journalists | Emergent collective behavior rather than scripted narrative |
| **Quantifiable sentiment** | Aggregate agent interactions into measurable metrics | Sentiment scores, polarization indices, influence network graphs on dashboard |
| **God's-eye variable injection** | Mid-simulation parameter changes to explore branching scenarios | "What if we introduce THIS variable?" — live scenario forking |

---

# SECTION D: COMPETITIVE LANDSCAPE & POSITIONING

## D.1 Direct Competitor Analysis

### vs. Pax Historia

| Limitation | Pax Historia Manifestation | Our Solution |
|-----------|--------------------------|-------------|
| Content velocity constraints | Historical research requirements slow scenario development; each preset demands domain expertise | Pop culture scenarios leverage existing fan knowledge; MiroFish GraphRAG from franchise wikis/novels/films accelerates creation |
| Player demographic ceiling | History enthusiasts represent defined segment; educational framing may deter entertainment seekers | Pop culture universes (Star Wars multi-generational recognition) expand addressable market |
| Simulation complexity | Known outcomes constrain creative action space | Fictional contexts enable more dramatic AI responses; "realism within established fiction" as legitimate validation mode |
| Opaque AI decisions | Binary "realistic/unrealistic" rejections frustrate players | Probabilistic approach with graduated likelihood estimates; visible agent reasoning traces |

### vs. Civilization VI

| Civ VI Limitation | Technical Root | Our Response |
|------------------|---------------|-------------|
| Statistical "cheating" | AI incompetence compensated by resource bonuses (+80% production at Deity) | Genuine multi-agent reasoning via MiroFish; difficulty modifies planning horizon and info access, not resource access |
| Rigid historical progression | Fixed tech trees enforce developmental orthodoxy | Emergent technological/social development; knowledge graph enables divergent paths |
| Predefined action constraints | Menu-based interface limits player expression | Natural language input; any conceivable action attemptable; feasibility evaluated by simulation |
| Predictable diplomatic AI | Fixed agenda system with exploitable patterns | Dynamic relationship formation; agents develop trust/grudges through interaction history |

### vs. Humankind

| Humankind Failure Mode | MiroFish-Based Solution |
|-----------------------|------------------------|
| Tactical combat incompetence (scattered attacks) | Agent-based military commanders with distinct doctrines; force concentration from coordinated agent decisions |
| Strategic passivity | Persistent agent goal structures generate proactive behavior; threat assessment triggers coalition formation |
| Culture selection incoherence | Cultural transitions emerge from internal debate among agents with competing visions |
| UI visualization failures | Progressive detail rendering; narrative synthesis reduces map-reading burden; React/Next.js real-time visualization |

### vs. AI Dungeon & Text-Based Competitors

| Product | Type | Strengths | Weaknesses | Our Advantage |
|---------|------|-----------|------------|---------------|
| **AI Dungeon** | AI text adventure | Pioneer, massive user base | Text-only (no map), no geopolitical simulation, quality degraded | Visual map, geopolitical depth, agent realism |
| **DeepGamer** | AI text adventure | Free, multiple genres | Basic, no map, limited AI quality | Full simulation engine, visual layer |
| **GoalSim** | AI life simulator | Branching narratives, character stats | Single-player, limited scope | Multi-actor geopolitical + pop culture simulation |
| **Mythia** | AI interactive fiction | Memory Fragments, Timelines | Fantasy-focused, no geopolitical | Broader scenario types, agent simulation |

## D.2 Our Unfair Advantages (Summary)

1. **MiroFish-powered agent swarm** — No competitor has population-level simulation with emergent behavior
2. **Beyond history** — Pop culture scenarios (Star Wars, Dune, Back to the Future, GoT, etc.), sci-fi, fantasy, anything
3. **Quantitative + Narrative hybrid** — Real numbers (GDP, military strength, population sentiment) PLUS rich narrative
4. **Multi-agent memory** — Persistent agent memory creates continuity across sessions
5. **God's-eye injection** — Mid-game variable changes for scenario branching
6. **Visual simulation layer** — Animated maps, sentiment heatmaps, influence networks, dashboard charts
7. **Probabilistic realism** — Players see probability distributions, not binary outcomes
8. **Narrative gravity** — Famous events exert pull without deterministic enforcement
9. **Natural language diplomacy** — Novel arrangements evaluated against agent goals, not pattern-matched against known treaty types

---

# SECTION E: TECHNICAL ARCHITECTURE

## E.1 System Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                     FRONTEND (Next.js 15 + TypeScript)               │
│  ┌──────────┐ ┌──────────┐ ┌──────────────┐ ┌──────────────────┐  │
│  │ Map View │ │ Action   │ │ Quant        │ │ Scenario Editor  │  │
│  │(MapLibre)│ │ Panel    │ │ Dashboard    │ │ (Map+Context)    │  │
│  └──────────┘ └──────────┘ └──────────────┘ └──────────────────┘  │
│  ┌──────────┐ ┌──────────┐ ┌──────────────┐ ┌──────────────────┐  │
│  │Diplomacy │ │ Agent    │ │ Timeline +   │ │ Scenario         │  │
│  │  Chat    │ │ Network  │ │ Branching    │ │ Marketplace      │  │
│  └──────────┘ └──────────┘ └──────────────┘ └──────────────────┘  │
│  ┌──────────────────────┐ ┌────────────────────────────────────┐  │
│  │ Sentiment Heatmap    │ │ Probability Distribution Viz       │  │
│  │ (deck.gl overlay)    │ │ (outcome likelihood bars)          │  │
│  └──────────────────────┘ └────────────────────────────────────┘  │
└───────────────────────────┬─────────────────────────────────────────┘
                            │ WebSocket + REST API
┌───────────────────────────┴─────────────────────────────────────────┐
│                   API GATEWAY (Node.js / Fastify)                    │
│  Auth (Clerk) │ Rate Limiting │ Token Billing │ Session Mgmt        │
│  WebSocket Hub │ BYOK Key Mgmt (AES-256) │ Stripe Integration      │
└───────────────────────────┬─────────────────────────────────────────┘
                            │
┌───────────────────────────┴─────────────────────────────────────────┐
│                   GAME ENGINE (Python / FastAPI)                      │
│  ┌────────────────┐  ┌────────────────┐  ┌───────────────────────┐ │
│  │ NL Action      │  │ World State    │  │ Turn Processor        │ │
│  │ Parser +       │  │ Manager        │  │ (Orchestrates all     │ │
│  │ Validator      │  │ (Narrative +   │  │  agents per turn)     │ │
│  │ (Game Master)  │  │  Quantitative) │  │                       │ │
│  └────────────────┘  └────────────────┘  └───────────────────────┘ │
│  ┌────────────────┐  ┌────────────────┐  ┌───────────────────────┐ │
│  │ Narrative      │  │ Quantitative   │  │ Diplomacy Engine      │ │
│  │ Generator      │  │ Simulator      │  │ (Treaty eval,         │ │
│  │ (Narrator)     │  │ (GDP, mil,     │  │  multi-party chat)    │ │
│  │                │  │  tech, pop)    │  │                       │ │
│  └────────────────┘  └────────────────┘  └───────────────────────┘ │
│  ┌────────────────┐  ┌────────────────┐  ┌───────────────────────┐ │
│  │ Realism        │  │ Narrative      │  │ Scenario              │ │
│  │ Validator      │  │ Gravity        │  │ Ontology              │ │
│  │ (Void/Backfire)│  │ Engine         │  │ Generator             │ │
│  └────────────────┘  └────────────────┘  └───────────────────────┘ │
└───────────────────────────┬─────────────────────────────────────────┘
                            │
┌───────────────────────────┴─────────────────────────────────────────┐
│             SWARM SIMULATION ENGINE (MiroFish/OASIS Fork)            │
│  ┌────────────────┐  ┌────────────────┐  ┌───────────────────────┐ │
│  │ Agent Pool     │  │ Dual-Platform  │  │ Sentiment             │ │
│  │ Generator      │  │ Social Sim     │  │ Aggregator            │ │
│  │ (personas from │  │ (Twitter +     │  │ (per-faction,         │ │
│  │  knowledge     │  │  Reddit-like)  │  │  per-region)          │ │
│  │  graph)        │  │                │  │                       │ │
│  └────────────────┘  └────────────────┘  └───────────────────────┘ │
│  ┌────────────────┐  ┌────────────────┐  ┌───────────────────────┐ │
│  │ GraphRAG       │  │ Agent Memory   │  │ Report Agent          │ │
│  │ Builder        │  │ (Zep/Neo4j/    │  │ (InsightForge +       │ │
│  │ (ontology →    │  │  Mem0)         │  │  PanoramaSearch +     │ │
│  │  knowledge     │  │                │  │  InterviewAgents)     │ │
│  │  graph)        │  │                │  │                       │ │
│  └────────────────┘  └────────────────┘  └───────────────────────┘ │
│  ┌────────────────┐  ┌────────────────┐                            │
│  │ Parallel       │  │ Probability    │                            │
│  │ Scenario       │  │ Distribution   │                            │
│  │ Branching      │  │ Calculator     │                            │
│  └────────────────┘  └────────────────┘                            │
└───────────────────────────┬─────────────────────────────────────────┘
                            │
┌───────────────────────────┴─────────────────────────────────────────┐
│                         DATA LAYER                                   │
│  ┌────────────────┐  ┌────────────────┐  ┌───────────────────────┐ │
│  │ TimescaleDB    │  │ Neo4j          │  │ Redis + BullMQ        │ │
│  │ (Game state,   │  │ (Knowledge     │  │ (Session cache,       │ │
│  │  time-series   │  │  graphs,       │  │  pub/sub, job         │ │
│  │  metrics)      │  │  agent rels)   │  │  queues)              │ │
│  └────────────────┘  └────────────────┘  └───────────────────────┘ │
│  ┌────────────────┐  ┌────────────────┐  ┌───────────────────────┐ │
│  │ S3/MinIO       │  │ OpenRouter     │  │ Zep Cloud             │ │
│  │ (Assets, maps, │  │ (LLM API       │  │ (Agent long-term      │ │
│  │  scenario data)│  │  gateway)      │  │  memory)              │ │
│  └────────────────┘  └────────────────┘  └───────────────────────┘ │
└─────────────────────────────────────────────────────────────────────┘
```

## E.2 Tech Stack

| Layer | Technology | Rationale |
|-------|-----------|-----------|
| Frontend | Next.js 15 + TypeScript | SSR, API routes, React ecosystem |
| Map Engine | MapLibre GL JS + deck.gl | Open-source tiles + geospatial overlays |
| Charts | Recharts | Quantitative dashboard |
| Realtime | Socket.io (WebSocket) | Live game state updates, multiplayer |
| API Gateway | Node.js + Fastify | High-performance, plugin ecosystem |
| Game Engine | Python + FastAPI | AI/ML ecosystem, async support |
| Swarm Engine | MiroFish/OASIS fork (Python) | Proven multi-agent simulation |
| Knowledge Graph | Neo4j Community | Production graph DB, free |
| Agent Memory | Zep Cloud (primary) / Mem0 (alternative) | Persistent agent memory with graph support |
| Database | TimescaleDB (PostgreSQL ext) | Time-series game state + standard SQL |
| Cache/Queue | Redis + BullMQ | Session caching, job queues, pub/sub |
| LLM Gateway | OpenRouter | 400+ models, single API, auto failover |
| Token Compression | bear-1.1 (The Token Company) | 66% context reduction, quality improvement |
| Object Storage | MinIO (self-hosted S3) | Map assets, scenario data |
| Auth | Clerk | Social login, JWT, session management |
| Payments | Stripe + Crypto (optional) | Token purchases, subscriptions |
| Hosting | Hostinger VPS (168.231.103.49) → AWS Mumbai | Cost-effective start, scale later |
| CI/CD | GitHub Actions | Automated testing and deployment |
| Repo | GitHub (mohaktnbt/project-nexus) | Version control |

## E.3 LLM Strategy

**Multi-tier model approach:**
- Tier 1 (Free/Light): DeepSeek V3 or Qwen-plus — cheapest, basic quality
- Tier 2 (Pro): Gemini 3.0 Flash or Claude Haiku — good balance
- Tier 3 (Max): Claude Sonnet 4.6 or GPT-5.1 — premium quality
- BYOK: Users bring their own OpenRouter API key

**Swarm agent LLM:** Use cheapest viable model (Qwen-plus or DeepSeek) for agent swarm — need thousands of calls per turn.

**Token compression:** bear-1.1 integration reduces context by 66%. Pax Historia's 268K-vote arena showed compressed models scored HIGHER than uncompressed, and A/B tests showed +5% purchase amount lift.

---

# SECTION F: CLAUDE CODE EXECUTION PLAN (45-DAY PHASED BUILD)

## Phase 0: Project Bootstrap (Day 1)

```
TASK 0.1: Create GitHub repository "project-nexus" under mohaktnbt
TASK 0.2: Initialize monorepo structure:
  /frontend        — Next.js 15 + TypeScript
  /api-gateway     — Node.js + Fastify
  /game-engine     — Python + FastAPI
  /swarm-engine    — MiroFish fork/integration
  /shared          — Shared types, configs, constants
  /data            — Map data, scenario templates, seed data
  /scripts         — Deployment, migration, utility scripts
  /docs            — Architecture docs, API specs
  CLAUDE.md        — Persistent context for Claude Code sessions
  TIMELINE.md      — Progress tracking
  AGENTS.md        — Agent architecture reference
  TODO-MANUAL.md   — Manual tasks tracking
  docker-compose.yml
  .env.example

TASK 0.3: Write CLAUDE.md with condensed version of this research document
TASK 0.4: Set up Docker Compose for local dev:
  - TimescaleDB (port 5432)
  - Neo4j Community (ports 7474, 7687)
  - Redis (port 6379)
  - MinIO (port 9000)
TASK 0.5: SSH into Hostinger VPS (168.231.103.49), set up tmux, clone repo
```

## Phase 1: Core Map & Game Shell (Days 2-5)

```
TASK 1.1: Next.js 15 setup with Tailwind + shadcn/ui
TASK 1.2: MapLibre GL map component with world GeoJSON borders
  - Country borders layer (clickable regions, color-coded by faction)
  - City labels, zoom/pan controls
  - deck.gl overlay layer (for future sentiment heatmap)
TASK 1.3: Core game UI layout:
  - Left: Map (60% width)
  - Right: Action input + Events feed (40% width)
  - Bottom: Timeline slider with time-jump controls
  - Top: Token count, model selector, settings
TASK 1.4: Scenario selection/browse screen
TASK 1.5: Basic scenario editor (map region selector, faction creator, context textarea, rules, start date)
```

## Phase 2: Game Engine Core (Days 6-10)

```
TASK 2.1: Python FastAPI game engine service
TASK 2.2: World State Manager schemas:
  - Nation: { name, GDP, military_strength, technology_level, population, happiness_index, alliances[], enemies[], leader, government_type }
  - Actor: { name, personality_traits, goals[], relationships{}, influence_score }
  - Map: { borders_geojson, cities[], points_of_interest[] }
  - Event: { timestamp, type, actors_involved[], description, quantitative_changes{} }
TASK 2.3: Action Validator (Game Master Agent):
  - NL parsing pipeline (syntactic → semantic → contextual → consequence)
  - Void/Backfire/Approve classification with explanatory narrative
  - Difficulty-modulated validation thresholds
TASK 2.4: Turn Processor:
  - Orchestrate: validate action → generate AI responses for all actors → update world state → emit events
TASK 2.5: Narrative Generator:
  - Rich event descriptions from world state changes
  - Model-tier-appropriate writing quality
TASK 2.6: Quantitative Simulator:
  - GDP delta calculations (war = loss, trade = gain, sanctions = gradual loss)
  - Military strength (recruitment, attrition, technology multiplier)
  - Population sentiment (protest probability, coup probability from swarm data)
  - Technology progression (research investment → capability unlocks)
  - Diplomatic relations matrix (trust scores, treaty compliance tracking)
TASK 2.7: OpenRouter integration:
  - Model selector (light/pro/max + experimental list)
  - Streaming response support
  - Token counting and billing middleware
  - Automatic fallback on model failure
  - BYOK support (AES-256 encrypted key storage)
```

## Phase 3: MiroFish Swarm Integration (Days 11-18)

```
TASK 3.1: Fork MiroFish, adapt for game context (Python service at port 5002)
TASK 3.2: Genre-adaptive ontology generator:
  - Historical: Citizen, Leader, Military_Commander, Diplomat, Merchant, Journalist, Rebel
  - Sci-Fi: Crew, Captain, Faction_Leader, Engineer, Scientist, Alien_Ambassador
  - Fantasy: Noble, Knight, Mage, Commoner, Merchant, Spy, Religious_Leader
  - Configurable per-scenario via seed document analysis
TASK 3.3: Agent persona generator:
  - From scenario context + knowledge graph, generate N agents per faction (configurable 50-1000)
  - Each: name, Big Five personality, political stance, occupation, influence_score, activity_schedule
  - Archetypal templates: reluctant_leader, corrupt_advisor, loyal_soldier, idealistic_rebel, pragmatic_merchant
TASK 3.4: Per-turn swarm integration:
  a. Feed world state + latest events to swarm engine
  b. Run mini-simulation (agents react, post, debate on simulated social platforms)
  c. Aggregate: sentiment_scores{}, emerging_narratives[], protest_probability, coup_probability, alliance_shift_probability
  d. Feed back to game engine as context for next turn's AI responses
TASK 3.5: Agent interview system (player can "talk to" any simulated agent in character)
TASK 3.6: Sentiment heatmap overlay (deck.gl on MapLibre, per-region color gradient)
TASK 3.7: Agent influence network visualization (d3.js force-directed graph)
TASK 3.8: Probability distribution display:
  - Before executing action, show: "45% diplomatic protest, 30% military mobilization, 20% economic retaliation, 5% unexpected alliance offer"
  - Player chooses to proceed or modify action
TASK 3.9: Parallel scenario branching:
  - "What if" mode: fork current game state, run lightweight swarm sim, show probable outcomes
  - Player selects preferred branch to continue
```

## Phase 4: Pop Culture & Expanded Scenarios (Days 19-23)

```
TASK 4.1: Scenario template system:
  - Schema: { universe, era, factions[], map_type, rules{}, context_document, realism_mode, narrative_gravity_events[] }
  - map_type: earth_political, earth_fantasy, space_grid, desert_planet, single_city, custom
  - realism_mode: historical_strict, historical_flexible, fiction_canonical, fiction_freeform, speculative

TASK 4.2: Pre-built scenario packs:
  HISTORICAL (10): Fall of Rome, Mongol Europe, WW2 alt, Cold War hot, Colonial era, American Civil War prevention, Napoleonic alt, Chinese Warring States, Ottoman expansion, Indian independence
  MODERN (5): US-China 2030, Middle East peace, EU expansion, India superpower, African Union rise
  POP CULTURE (10): Star Wars Galactic Civil War, Dune Arrakis politics, GoT War of Five Kings, LotR War of the Ring, Back to the Future timeline paradox, The Expanse Belt rebellion, Foundation psychohistory, Hunger Games district revolt, 1984 Oceania resistance, Marvel multiverse
  SCI-FI ORIGINAL (5): First alien contact, AI singularity, Mars colony, Climate apocalypse, Interstellar exploration
  
TASK 4.3: Custom map system:
  - Upload custom GeoJSON for fantasy/sci-fi maps
  - Map editor: draw regions, place cities, define terrain types
  - Template maps: Earth, Space Grid, Fantasy Continent, Desert Planet, Single City, Space Station

TASK 4.4: Narrative gravity engine:
  - For each scenario, define canonical_events[] with base_probability
  - Each turn, calculate adjusted_probability based on player actions and swarm state
  - Events fire probabilistically — "Battle of Yavin" might happen differently or not at all
  - Player sees "narrative tension" indicator when approaching canonical moments

TASK 4.5: Universe rules engine:
  - Per-scenario physics/magic/technology constraints
  - "Force users can influence weak-minded" as valid game mechanic in Star Wars
  - "Prescience shows probable futures" as valid in Dune
  - Validator respects universe rules, not just Earth physics
```

## Phase 5: Diplomacy, Multiplayer & Social (Days 24-30)

```
TASK 5.1: Enhanced diplomacy:
  - NL chat with AI nations (evaluated against agent goals, not pattern-matched)
  - Novel treaty proposals: "I will support your claim if you guarantee my trading rights for 30 years"
  - Treaty storage in game state, enforced by game engine
  - AI nations can break treaties based on swarm sentiment shifts
  - Trust scores evolve through interaction history

TASK 5.2: Multiplayer foundation:
  - Room system (create/join game via link)
  - Turn-based multiplayer (all players submit, then resolve simultaneously)
  - Real-time chat between players
  - AI controls all non-player factions with full swarm agents
  - Spectator mode with delayed state

TASK 5.3: User accounts (Clerk auth, profiles, stats, achievements)
TASK 5.4: Scenario marketplace (publish, browse, rate, play count, creator revenue share)
TASK 5.5: Social features (follow creators, share replays, discussion threads, trending algorithm)
```

## Phase 6: Token Economy & Monetization (Days 31-35)

```
TASK 6.1: Token system:
  - Free tier: X tokens/day (enough for 3-5 turns on light model)
  - Token packs via Stripe
  - Subscriptions:
    Basic ($5/mo): X tokens + Pro models
    Premium ($15/mo): More tokens + Max models + BYOK
    Creator ($25/mo): Everything + priority publishing + analytics

TASK 6.2: BYOK (Bring Your Own Key):
  - OpenRouter API key input, AES-256 encrypted storage
  - Bypass token system with own key

TASK 6.3: Creator economy:
  - Creators earn % of tokens spent on their scenarios
  - Creator dashboard with play analytics
  - Payout system

TASK 6.4: Stripe integration (payments, subscriptions, refunds)
TASK 6.5: Token usage tracking (per-turn cost display, history, budget alerts)
TASK 6.6: Pax Arena equivalent (model quality voting, earn tokens for votes)
```

## Phase 7: Polish, Testing & Launch (Days 36-45)

```
TASK 7.1: Performance:
  - Streaming LLM responses
  - Lazy-load map tiles, cache scenarios
  - Optimize swarm batch sizes
  - bear-1.1 compression integration

TASK 7.2: Mobile responsiveness (responsive layout, touch-friendly map)
TASK 7.3: Onboarding (interactive tutorial scenario, tooltips, quick-start presets)
TASK 7.4: Error handling (LLM timeout, model failure graceful degradation, auto-save, reconnection)
TASK 7.5: SEO & marketing (landing page, blog, Open Graph, Discord community)
TASK 7.6: Analytics (PostHog/Mixpanel: DAU, retention, token consumption, conversion)
TASK 7.7: Load testing (1000 concurrent games, bottleneck identification, scale plan)
```

---

# SECTION G: COMPLETE FILE STRUCTURE

```
project-nexus/
├── CLAUDE.md
├── TIMELINE.md
├── AGENTS.md
├── TODO-MANUAL.md
├── docker-compose.yml
├── .env.example
├── .github/workflows/
│   ├── ci.yml
│   └── deploy.yml
├── frontend/
│   ├── package.json
│   ├── next.config.js
│   ├── tailwind.config.ts
│   └── src/
│       ├── app/
│       │   ├── layout.tsx
│       │   ├── page.tsx                    # Landing
│       │   ├── play/[gameId]/page.tsx      # Game view
│       │   ├── play/new/page.tsx           # New game setup
│       │   ├── explore/page.tsx            # Marketplace
│       │   ├── create/page.tsx             # Scenario editor
│       │   └── profile/page.tsx
│       ├── components/
│       │   ├── map/
│       │   │   ├── GameMap.tsx
│       │   │   ├── MapControls.tsx
│       │   │   ├── SentimentOverlay.tsx
│       │   │   ├── BorderLayer.tsx
│       │   │   └── ProbabilityOverlay.tsx
│       │   ├── game/
│       │   │   ├── ActionPanel.tsx
│       │   │   ├── EventsFeed.tsx
│       │   │   ├── Timeline.tsx
│       │   │   ├── QuantDashboard.tsx
│       │   │   ├── DiplomacyChat.tsx
│       │   │   ├── AgentNetwork.tsx
│       │   │   ├── ProbabilityDisplay.tsx
│       │   │   └── NarrativeGravityIndicator.tsx
│       │   ├── editor/
│       │   │   ├── ScenarioEditor.tsx
│       │   │   ├── MapEditor.tsx
│       │   │   ├── FactionEditor.tsx
│       │   │   └── UniverseRulesEditor.tsx
│       │   ├── marketplace/
│       │   │   ├── ScenarioCard.tsx
│       │   │   ├── ScenarioGrid.tsx
│       │   │   └── SearchFilter.tsx
│       │   └── ui/                         # shadcn
│       ├── hooks/
│       │   ├── useGameSocket.ts
│       │   ├── useGameState.ts
│       │   ├── useTokens.ts
│       │   └── useSwarmData.ts
│       ├── lib/
│       │   ├── api.ts
│       │   ├── socket.ts
│       │   └── types.ts
│       └── stores/
│           ├── gameStore.ts
│           └── userStore.ts
├── api-gateway/
│   ├── package.json
│   └── src/
│       ├── server.ts
│       ├── routes/ (auth, games, scenarios, tokens, users)
│       ├── middleware/ (auth, rateLimit, tokenBilling)
│       ├── services/ (stripe, openrouter, byok)
│       ├── websocket/gameSocket.ts
│       └── prisma/schema.prisma
├── game-engine/
│   ├── pyproject.toml
│   └── src/
│       ├── main.py
│       ├── models/ (world_state, nation, actor, event, scenario)
│       ├── agents/ (game_master, narrator, advisor, diplomat)
│       ├── simulation/ (quantitative, diplomacy, turn_processor, narrative_gravity)
│       ├── llm/ (openrouter, prompts, compression)
│       └── utils/ (map_utils, state_serializer)
├── swarm-engine/
│   ├── pyproject.toml
│   └── src/
│       ├── main.py
│       ├── ontology/ (generator, templates)
│       ├── agents/ (persona_generator, agent_pool, interviewer, archetypes)
│       ├── simulation/ (social_sim, sentiment, emergence, branching)
│       ├── graph/ (neo4j_client, graphrag)
│       ├── memory/ (zep_client, memory_factory)
│       ├── probability/ (distribution_calculator, option_ranker)
│       └── reports/ (report_agent)
├── data/
│   ├── maps/ (world_borders.geojson, world_cities.json, custom/)
│   ├── scenarios/
│   │   ├── templates/ (historical/, modern/, pop_culture/, scifi/)
│   │   └── schema.json
│   ├── universe_rules/ (star_wars.json, dune.json, got.json, etc.)
│   └── seed/ (nations_base.json, historical_context/)
├── scripts/ (setup.sh, deploy.sh, migrate.sh, seed-data.sh)
└── docs/ (architecture.md, api-spec.md, game-design.md, monetization.md)
```

---

# SECTION H: RISKS & MITIGATIONS

| Risk | Impact | Mitigation |
|------|--------|------------|
| LLM costs scale with users | High | Token compression (bear-1.1), tiered models, BYOK, aggressive caching, cheapest model for swarm agents |
| Swarm simulation too slow per turn | High | Batch LLM calls, reduce agents for light tier, pre-compute common scenarios, lightweight sim for "what-if" |
| AI quality inconsistent | Medium | Multi-model fallback, prompt engineering iteration, user model choice, Pax Arena-style voting |
| Copyright issues with pop culture IPs | Medium | "Inspired by" original scenarios, no trademarked names in paid content, user-generated (DMCA safe harbor) |
| Map rendering performance | Medium | Tile caching, progressive loading, simplified geometry for mobile |
| Context window limits for long games | High | bear-1.1 compression, summarization of old turns, sliding context window |
| Agent memory costs (Zep Cloud) | Medium | Free tier for basic, self-hosted Neo4j for advanced, batch memory updates |
| Server costs at scale | Medium | Start on Hostinger VPS, autoscale on AWS Mumbai, edge caching |

---

# SECTION I: SUCCESS METRICS (First 90 Days)

| Metric | Target |
|--------|--------|
| Scenarios published | 100+ |
| Daily Active Users | 1,000 |
| Average session length | 15+ minutes |
| Token purchase conversion | 5% of DAU |
| D7 retention | 25% |
| Community-created scenarios | 50+ |
| Multiplayer games played | 100+ |
| Pop culture scenario plays | 40% of total |
| Agent interview interactions | 500+/day |
| Swarm simulation per-turn latency | <30 seconds |
