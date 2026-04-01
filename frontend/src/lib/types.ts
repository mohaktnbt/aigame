export interface ProbabilityDistribution {
  outcome: string;
  probability: number;
  confidence: number;
}

export interface SentimentData {
  nationId: string;
  targetNationId: string;
  sentiment: number; // -1.0 to 1.0
  timestamp: number;
  coordinates: [number, number];
}

export interface Nation {
  id: string;
  name: string;
  gdp: number;
  militaryPower: number;
  population: number;
  sentiment: Record<string, number>;
  coordinates: [number, number];
  color: string;
}

export interface Agent {
  id: string;
  name: string;
  role: string;
  factionId: string;
  personality: string;
  goals: string[];
}

export interface Faction {
  id: string;
  name: string;
  nations: string[];
  agents: Agent[];
  color: string;
  isPlayerControlled: boolean;
}

export interface Action {
  id: string;
  factionId: string;
  type: string;
  description: string;
  targetId?: string;
  timestamp: number;
  result?: string;
  probabilities?: ProbabilityDistribution[];
}

export interface Event {
  id: string;
  type: "political" | "military" | "economic" | "diplomatic" | "social";
  title: string;
  description: string;
  timestamp: number;
  affectedNations: string[];
  severity: "low" | "medium" | "high" | "critical";
}

export interface WorldState {
  nations: Nation[];
  factions: Faction[];
  globalSentiment: SentimentData[];
  globalGdp: number;
  timestamp: number;
}

export interface GameState {
  id: string;
  name: string;
  scenarioId: string;
  worldState: WorldState;
  events: Event[];
  currentTurn: number;
  maxTurns: number;
  factions: Faction[];
  selectedFaction: string | null;
  status: "lobby" | "active" | "paused" | "completed";
  createdAt: number;
  updatedAt: number;
}
