# Project Nexus — API Specification

## API Gateway (Port 3001)

### Authentication
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /api/auth/webhook | Clerk webhook handler |
| GET | /api/auth/me | Get current user |

### Games
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /api/games | Create new game session |
| GET | /api/games/:id | Get game state |
| POST | /api/games/:id/action | Submit player action |
| POST | /api/games/:id/turn | Process turn |
| GET | /api/games/:id/history | Get game event history |
| POST | /api/games/:id/branch | Create "what if" branch |

### Scenarios
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /api/scenarios | List scenarios (filterable) |
| GET | /api/scenarios/:id | Get scenario details |
| POST | /api/scenarios | Create new scenario |
| PUT | /api/scenarios/:id | Update scenario |
| DELETE | /api/scenarios/:id | Delete scenario |

### Tokens
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /api/tokens/balance | Get token balance |
| POST | /api/tokens/purchase | Create Stripe checkout |
| POST | /api/tokens/webhook | Stripe webhook |

### WebSocket Events
| Event | Direction | Description |
|-------|-----------|-------------|
| join_game | Client → Server | Join a game room |
| leave_game | Client → Server | Leave a game room |
| game_update | Server → Client | World state update |
| turn_result | Server → Client | Turn resolution results |
| probability_update | Server → Client | Probability distribution update |
| chat_message | Bidirectional | Diplomacy chat message |

---

## Game Engine (Port 5001)

### Internal API (called by API Gateway)
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /health | Health check |
| POST | /validate-action | Validate player action |
| POST | /process-turn | Process a game turn |
| POST | /generate-narrative | Generate narrative text |
| GET | /scenario/:id/gravity | Get narrative gravity state |
| POST | /diplomacy/negotiate | Process diplomatic action |

---

## Swarm Engine (Port 5002)

### Internal API (called by Game Engine)
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /health | Health check |
| POST | /simulate | Run swarm simulation for a turn |
| POST | /probability | Calculate outcome probability distribution |
| POST | /branch | Run parallel "what if" simulation |
| POST | /interview | Interview a simulated agent |
| GET | /sentiment/:gameId | Get current sentiment data |
| POST | /ontology/generate | Generate ontology from seed |
| POST | /agents/generate | Generate agent personas |
