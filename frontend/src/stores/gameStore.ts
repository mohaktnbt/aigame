import { create } from "zustand";
import type { WorldState, Event, Faction } from "@/lib/types";

interface GameStore {
  gameId: string | null;
  worldState: WorldState | null;
  events: Event[];
  currentTurn: number;
  maxTurns: number;
  factions: Faction[];
  selectedFaction: string | null;
  status: "lobby" | "active" | "paused" | "completed";

  setGameId: (id: string) => void;
  setWorldState: (state: WorldState) => void;
  addEvent: (event: Event) => void;
  setEvents: (events: Event[]) => void;
  setCurrentTurn: (turn: number) => void;
  setFactions: (factions: Faction[]) => void;
  setSelectedFaction: (factionId: string | null) => void;
  setStatus: (status: GameStore["status"]) => void;
  reset: () => void;
}

const initialState = {
  gameId: null,
  worldState: null,
  events: [],
  currentTurn: 0,
  maxTurns: 50,
  factions: [],
  selectedFaction: null,
  status: "lobby" as const,
};

export const useGameStore = create<GameStore>((set) => ({
  ...initialState,

  setGameId: (id) => set({ gameId: id }),
  setWorldState: (worldState) => set({ worldState }),
  addEvent: (event) => set((state) => ({ events: [event, ...state.events] })),
  setEvents: (events) => set({ events }),
  setCurrentTurn: (currentTurn) => set({ currentTurn }),
  setFactions: (factions) => set({ factions }),
  setSelectedFaction: (selectedFaction) => set({ selectedFaction }),
  setStatus: (status) => set({ status }),
  reset: () => set(initialState),
}));
