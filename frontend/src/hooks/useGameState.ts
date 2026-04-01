"use client";

import { useCallback } from "react";
import { useGameStore } from "@/stores/gameStore";
import { api } from "@/lib/api";
import type { GameState } from "@/lib/types";

export function useGameState() {
  const store = useGameStore();

  const loadGame = useCallback(async (gameId: string) => {
    const game = await api.get<GameState>(`/api/games/${gameId}`);
    store.setGameId(game.id);
    store.setWorldState(game.worldState);
    store.setEvents(game.events);
    store.setCurrentTurn(game.currentTurn);
    store.setFactions(game.factions);
    store.setSelectedFaction(game.selectedFaction);
    store.setStatus(game.status);
  }, [store]);

  const submitAction = useCallback(
    async (description: string) => {
      if (!store.gameId || !store.selectedFaction) return;

      const result = await api.post(`/api/games/${store.gameId}/actions`, {
        factionId: store.selectedFaction,
        description,
      });

      return result;
    },
    [store.gameId, store.selectedFaction]
  );

  return {
    ...store,
    loadGame,
    submitAction,
  };
}
