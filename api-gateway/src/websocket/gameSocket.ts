import type { Server, Socket } from "socket.io";

// TODO: Use Redis adapter for multi-instance deployments
// import { createAdapter } from "@socket.io/redis-adapter";
// import { createClient } from "ioredis";

interface JoinGamePayload {
  gameId: string;
  userId: string;
}

interface GameEventPayload {
  gameId: string;
  event: {
    id: string;
    turn: number;
    type: string;
    title: string;
    narrative: string;
    quantitativeChanges: Record<string, unknown>;
  };
}

interface TurnUpdatePayload {
  gameId: string;
  turn: number;
  event: GameEventPayload["event"];
}

/**
 * Set up Socket.io game room management.
 * Handles real-time communication for active game sessions.
 */
export function setupGameSocket(io: Server): void {
  // TODO: Set up Redis adapter for horizontal scaling
  // const pubClient = new Redis(process.env.REDIS_URL);
  // const subClient = pubClient.duplicate();
  // io.adapter(createAdapter(pubClient, subClient));

  io.on("connection", (socket: Socket) => {
    console.log(`Socket connected: ${socket.id}`);

    // TODO: Authenticate socket connection using Clerk token
    // const token = socket.handshake.auth.token;
    // Verify token and attach user info to socket

    /**
     * Join a game room to receive real-time updates.
     */
    socket.on("game:join", (payload: JoinGamePayload) => {
      const { gameId, userId } = payload;
      const roomName = `game:${gameId}`;

      // TODO: Verify user has access to this game via database check

      socket.join(roomName);
      socket.data["userId"] = userId;
      socket.data["gameId"] = gameId;

      console.log(`User ${userId} joined game room ${roomName}`);

      // Notify other players in the room
      socket.to(roomName).emit("game:player_joined", {
        userId,
        socketId: socket.id,
      });
    });

    /**
     * Leave a game room.
     */
    socket.on("game:leave", (payload: { gameId: string }) => {
      const roomName = `game:${payload.gameId}`;
      socket.leave(roomName);

      console.log(`Socket ${socket.id} left game room ${roomName}`);

      socket.to(roomName).emit("game:player_left", {
        userId: socket.data["userId"],
        socketId: socket.id,
      });
    });

    /**
     * Handle disconnection.
     */
    socket.on("disconnect", (reason: string) => {
      const gameId = socket.data["gameId"] as string | undefined;
      if (gameId) {
        const roomName = `game:${gameId}`;
        socket.to(roomName).emit("game:player_left", {
          userId: socket.data["userId"],
          socketId: socket.id,
          reason,
        });
      }

      console.log(`Socket disconnected: ${socket.id} (${reason})`);
    });
  });
}

/**
 * Broadcast a game event to all players in a game room.
 * Call this from route handlers after creating game events.
 */
export function broadcastGameEvent(
  io: Server,
  payload: GameEventPayload
): void {
  io.to(`game:${payload.gameId}`).emit("game:event", payload.event);
}

/**
 * Broadcast a turn update to all players in a game room.
 * Call this from route handlers after advancing a turn.
 */
export function broadcastTurnUpdate(
  io: Server,
  payload: TurnUpdatePayload
): void {
  io.to(`game:${payload.gameId}`).emit("game:turn", {
    turn: payload.turn,
    event: payload.event,
  });
}
