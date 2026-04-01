# AGENTS.md — Project Nexus Agent Architecture

## Overview

Project Nexus uses a multi-layer agent system combining player-facing AI agents with a population-level swarm simulation.

---

## Player-Facing Agents

### 1. Game Master Agent
**Purpose**: Validates player actions, determines outcomes, enforces universe rules.

**Input**: Player's natural language action + current world state + universe rules
**Output**: Action classification (void/backfire/approve) + explanation + outcome modifiers

**Model**: Gemini 3.0 Flash (Pro tier) / Claude Sonnet 4.6 (Max tier)

**Prompt Strategy**:
- System prompt includes universe rules, current world state summary, faction capabilities
- Few-shot examples of valid/invalid actions for the scenario type
- Chain-of-thought reasoning for action evaluation

### 2. Narrative Generator Agent
**Purpose**: Produces rich, immersive event descriptions after turn resolution.

**Input**: Resolved action outcome + world state changes + affected agents' reactions
**Output**: 2-4 paragraph narrative text + event title + mood tag

**Model**: Same as Game Master

### 3. Strategic Advisor Agent
**Purpose**: Provides intelligence briefings and strategic recommendations to the player.

**Input**: Current world state + recent events + player's faction status
**Output**: Strategic assessment + recommended actions + risk analysis

**Model**: Same as Game Master

### 4. Diplomat Agent
**Purpose**: Roleplays AI-controlled nations in diplomatic negotiations.

**Input**: Diplomatic context + nation personality + relationship history + goals
**Output**: In-character diplomatic response + hidden intent assessment

**Model**: Same as Game Master

---

## Swarm Agents (MiroFish Layer)

### 5. Population Agents (Thousands per scenario)
**Purpose**: Simulate individual citizens, leaders, military, media, merchants, etc.

**Attributes**:
- Big Five personality (Openness, Conscientiousness, Extraversion, Agreeableness, Neuroticism)
- Political stance (0-100 spectrum per issue)
- Influence score (local/regional/national/global)
- Faction loyalty (0-100)
- Schedule (daily activity patterns)
- Memory (via Zep Cloud)

**Behavior**: Each agent reacts to world events based on personality, creating emergent population-level responses.

**Model**: Qwen-plus / DeepSeek V3 (cheapest viable for bulk calls)

### 6. Ontology Generator Agent
**Purpose**: Creates genre-appropriate entity types and relationship schemas from seed documents.

**Input**: Scenario seed document (setting description, key entities, rules)
**Output**: Entity ontology (types, attributes, relationships) compatible with Neo4j schema

### 7. Sentiment Aggregator
**Purpose**: Computes per-faction, per-region sentiment scores from individual agent states.

**Input**: All agent states in a region/faction
**Output**: Aggregated sentiment scores, protest probability, loyalty index, mood distribution

### 8. Probability Distribution Calculator
**Purpose**: Runs lightweight parallel simulations to estimate outcome probabilities.

**Input**: Proposed player action + current world state + agent states
**Output**: Probability distribution over possible outcomes (e.g., 45% diplomatic protest, 30% military response, etc.)

### 9. Report Agent
**Purpose**: Generates intelligence reports combining quantitative data, graph analysis, and agent interviews.

**Sub-components**:
- **InsightForge**: Statistical analysis of game metrics
- **PanoramaSearch**: Graph-based relationship and influence mapping
- **InterviewAgents**: Targeted interviews with key simulated agents

---

## Agent Communication Flow

```
Player Action
    ↓
Game Master Agent (validate)
    ↓
Probability Calculator (preview outcomes)
    ↓ (player confirms)
Turn Processor
    ├→ Quantitative Simulator (update numbers)
    ├→ Swarm Engine (agent reactions)
    │   ├→ Population Agents (individual reactions)
    │   ├→ Sentiment Aggregator (aggregate sentiment)
    │   └→ Social Sim (emergent social dynamics)
    ├→ Narrative Gravity (canonical event check)
    └→ Diplomacy Engine (treaty/relation updates)
    ↓
Narrative Generator (produce story text)
    ↓
Player receives: Narrative + Dashboard + Map Updates + Probability Shifts
```

---

## Memory Architecture

- **Short-term**: Redis (current turn context, recent events)
- **Medium-term**: TimescaleDB (game session history, state snapshots)
- **Long-term**: Zep Cloud (agent persistent memories across sessions)
- **Graph**: Neo4j (entity relationships, influence networks, knowledge graphs)

## Token Optimization

- **bear-1.1 compression**: Applied to all LLM calls (66% context reduction)
- **Batch processing**: Swarm agents processed in parallel batches
- **Tiered models**: Premium models for player-facing, cheap models for swarm
- **Caching**: Common prompt templates cached, only dynamic state injected
