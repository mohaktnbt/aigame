"use client";

import { useEffect, useCallback } from "react";
import { connectSocket, disconnectSocket } from "@/lib/socket";
import { useGameStore } from "@/stores/gameStore";
import type { Event, WorldState } from "@/lib/types";

export function useGameSocket(gameId: string | null) {
  const { setWorldState, addEvent, setCurrentTurn, setStatus } = useGameStore();

  useEffect(() => {
    if (!gameId) return;

    const socket = connectSocket(gameId);

    socket.on("world:update", (worldState: WorldState) => {
      setWorldState(worldState);
    });

    socket.on("event:new", (event: Event) => {
      addEvent(event);
    });

    socket.on("turn:advance", (turn: number) => {
      setCurrentTurn(turn);
    });

    socket.on("game:status", (status: "lobby" | "active" | "paused" | "completed") => {
      setStatus(status);
    });

    socket.on("connect_error", (err: Error) => {
      console.error("Socket connection error:", err.message);
    });

    return () => {
      disconnectSocket();
    };
  }, [gameId, setWorldState, addEvent, setCurrentTurn, setStatus]);

  const sendAction = useCallback(
    (action: { type: string; description: string; targetId?: string }) => {
      if (!gameId) return;
      const socket = connectSocket(gameId);
      socket.emit("action:submit", action);
    },
    [gameId]
  );

  return { sendAction };
}
