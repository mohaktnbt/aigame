# Project Nexus — Game Design Document

## Core Vision

An AI-powered universal scenario simulation where players shape history, fiction, and speculative futures through natural language commands, experiencing consequences through both rich narrative and hard numbers.

## Player Experience

### Session Flow
1. **Browse** — Explore scenario marketplace (historical, sci-fi, fantasy, pop culture)
2. **Select** — Choose scenario and faction to control
3. **Play** — Type natural language actions, see AI-validated outcomes
4. **Observe** — Watch thousands of simulated agents react, creating emergent consequences
5. **Decide** — See probability distributions before committing to actions
6. **Evolve** — Track quantitative dashboards while reading narrative outcomes
7. **Branch** — Explore "what if" scenarios, interview any simulated agent
8. **Share** — Publish scenarios, earn tokens from popular creations

### Key Mechanics

#### Natural Language Actions
Players type actions in plain English. The Game Master Agent parses, validates against universe rules, and classifies:
- **Approved**: Action proceeds with calculated outcomes
- **Void**: Action impossible given current state (with explanation)
- **Backfire**: Action is possible but may have unintended consequences

#### Probability-Before-Commitment
Before executing, players see outcome distributions:
- "45% diplomatic protest, 30% military mobilization, 20% economic retaliation, 5% surprise alliance"
- Players can modify their action based on this intelligence

#### Dual-Layer Output
Every turn produces:
- **Narrative**: Rich AI-generated text (2-4 paragraphs)
- **Quantitative**: Dashboard updates (GDP, military, tech, sentiment charts)
- **Map**: Visual changes (borders, sentiment heatmap, markers)

#### Narrative Gravity
Canonical events from source material exert probabilistic pull:
- `adjusted_probability = base_probability * player_action_modifier * swarm_sentiment_modifier`
- Players can push against gravity (prevent D-Day) or accelerate it (trigger it earlier)
- "Narrative tension" indicator shows proximity to canonical moments

#### Agent Interviews
Players can talk to any simulated agent in-character:
- "What does the average citizen of Coruscant think about the Death Star?"
- Agent responds based on personality, faction loyalty, and current events

## Scenario Types

| Type | Examples | Realism Level |
|------|----------|---------------|
| Historical | WW2, Cold War, Roman Empire | Earth physics + era capabilities |
| Pop Culture | Star Wars, Dune, GoT, Marvel | Universe-specific rules |
| Sci-Fi | Mars Colony, First Contact | Physics-based + speculative tech |
| Fantasy | Custom worlds | Magic systems defined per scenario |
| Modern | Geopolitical what-ifs | Current real-world constraints |

## Token Economy

- **Free tier**: 0.2 tokens/day
- **Pro tier**: Monthly subscription with token allocation
- **Max tier**: Higher allocation + premium models (Claude Sonnet 4.6)
- **BYOK**: Bring Your Own Key for unlimited usage
- **Creator revenue**: 10% token commission on popular scenarios (150+ rounds played)
