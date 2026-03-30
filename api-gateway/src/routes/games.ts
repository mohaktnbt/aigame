import type { FastifyInstance, FastifyRequest, FastifyReply } from "fastify";
import { PrismaClient } from "@prisma/client";
import { requireAuth } from "../middleware/auth.js";
import { rateLimit } from "../middleware/rateLimit.js";

const prisma = new PrismaClient();

interface CreateGameBody {
  scenarioId: string;
}

interface GameActionBody {
  action: string;
  parameters?: Record<string, unknown>;
}

export async function gameRoutes(fastify: FastifyInstance) {
  /**
   * POST /api/games
   * Create a new game from a scenario.
   */
  fastify.post(
    "/",
    { preHandler: [requireAuth, rateLimit({ max: 20, windowMs: 60_000 })] },
    async (
      request: FastifyRequest<{ Body: CreateGameBody }>,
      reply: FastifyReply
    ) => {
      const { scenarioId } = request.body;
      const userId = request.user!.id;

      const scenario = await prisma.scenario.findUnique({
        where: { id: scenarioId },
      });

      if (!scenario) {
        return reply.code(404).send({ error: "Scenario not found" });
      }

      // TODO: Deduct tokens for game creation if applicable

      const game = await prisma.game.create({
        data: {
          scenarioId,
          userId,
          status: "ACTIVE",
          worldState: scenario.universeRules,
          currentTurn: 0,
        },
        include: {
          scenario: {
            select: { id: true, title: true, type: true },
          },
        },
      });

      // Create initial game event
      await prisma.gameEvent.create({
        data: {
          gameId: game.id,
          turn: 0,
          type: "GAME_START",
          title: "Game Started",
          narrative: `A new game has begun in the "${scenario.title}" scenario.`,
          quantitativeChanges: {},
        },
      });

      request.log.info({ gameId: game.id, scenarioId }, "Game created");
      return reply.code(201).send({ game });
    }
  );

  /**
   * GET /api/games/:id
   * Get game details including recent events.
   */
  fastify.get(
    "/:id",
    { preHandler: [requireAuth] },
    async (
      request: FastifyRequest<{ Params: { id: string } }>,
      reply: FastifyReply
    ) => {
      const { id } = request.params;
      const userId = request.user!.id;

      const game = await prisma.game.findUnique({
        where: { id },
        include: {
          scenario: true,
          events: {
            orderBy: { createdAt: "desc" },
            take: 20,
          },
        },
      });

      if (!game) {
        return reply.code(404).send({ error: "Game not found" });
      }

      if (game.userId !== userId) {
        return reply.code(403).send({ error: "Access denied" });
      }

      return reply.send({ game });
    }
  );

  /**
   * POST /api/games/:id/action
   * Submit a player action within the current turn.
   */
  fastify.post(
    "/:id/action",
    { preHandler: [requireAuth, rateLimit({ max: 30, windowMs: 60_000 })] },
    async (
      request: FastifyRequest<{
        Params: { id: string };
        Body: GameActionBody;
      }>,
      reply: FastifyReply
    ) => {
      const { id } = request.params;
      const { action, parameters } = request.body;
      const userId = request.user!.id;

      const game = await prisma.game.findUnique({ where: { id } });

      if (!game) {
        return reply.code(404).send({ error: "Game not found" });
      }
      if (game.userId !== userId) {
        return reply.code(403).send({ error: "Access denied" });
      }
      if (game.status !== "ACTIVE") {
        return reply.code(400).send({ error: "Game is not active" });
      }

      // TODO: Send action to AI service via BullMQ job queue for processing
      // TODO: The AI service should evaluate the action against universe rules
      // and return narrative + quantitative changes

      const event = await prisma.gameEvent.create({
        data: {
          gameId: id,
          turn: game.currentTurn,
          type: "PLAYER_ACTION",
          title: action,
          narrative: `Player action: ${action}`, // TODO: Replace with AI-generated narrative
          quantitativeChanges: parameters ?? {},
        },
      });

      // TODO: Broadcast event via Socket.io to game room
      // const io = fastify.io;
      // io.to(`game:${id}`).emit("game:event", event);

      return reply.send({ event });
    }
  );

  /**
   * POST /api/games/:id/turn
   * Advance the game to the next turn. Triggers AI world simulation.
   */
  fastify.post(
    "/:id/turn",
    { preHandler: [requireAuth, rateLimit({ max: 10, windowMs: 60_000 })] },
    async (
      request: FastifyRequest<{ Params: { id: string } }>,
      reply: FastifyReply
    ) => {
      const { id } = request.params;
      const userId = request.user!.id;

      const game = await prisma.game.findUnique({
        where: { id },
        include: {
          scenario: true,
          events: {
            where: { turn: { gte: 0 } },
            orderBy: { createdAt: "desc" },
            take: 10,
          },
        },
      });

      if (!game) {
        return reply.code(404).send({ error: "Game not found" });
      }
      if (game.userId !== userId) {
        return reply.code(403).send({ error: "Access denied" });
      }
      if (game.status !== "ACTIVE") {
        return reply.code(400).send({ error: "Game is not active" });
      }

      // TODO: Deduct tokens for turn advancement
      // TODO: Enqueue AI simulation job via BullMQ
      // The job should:
      //   1. Gather current world state + recent events
      //   2. Call OpenRouter LLM to simulate world response
      //   3. Parse AI response into narrative + quantitative changes
      //   4. Update worldState
      //   5. Broadcast results via Socket.io

      const nextTurn = game.currentTurn + 1;

      const updatedGame = await prisma.game.update({
        where: { id },
        data: {
          currentTurn: nextTurn,
          updatedAt: new Date(),
        },
      });

      const turnEvent = await prisma.gameEvent.create({
        data: {
          gameId: id,
          turn: nextTurn,
          type: "TURN_ADVANCE",
          title: `Turn ${nextTurn}`,
          narrative: `The world advances to turn ${nextTurn}.`, // TODO: Replace with AI-generated narrative
          quantitativeChanges: {},
        },
      });

      // TODO: Broadcast turn update via Socket.io
      // const io = fastify.io;
      // io.to(`game:${id}`).emit("game:turn", { turn: nextTurn, event: turnEvent });

      return reply.send({ game: updatedGame, event: turnEvent });
    }
  );
}
