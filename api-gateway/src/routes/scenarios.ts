import type { FastifyInstance, FastifyRequest, FastifyReply } from "fastify";
import { PrismaClient } from "@prisma/client";
import { requireAuth, optionalAuth } from "../middleware/auth.js";
import { rateLimit } from "../middleware/rateLimit.js";

const prisma = new PrismaClient();

interface CreateScenarioBody {
  title: string;
  description: string;
  type: "HISTORICAL" | "SCIFI" | "FANTASY" | "POP_CULTURE";
  universeRules?: Record<string, unknown>;
  mapData?: Record<string, unknown>;
}

interface ListScenariosQuery {
  type?: string;
  page?: string;
  limit?: string;
}

export async function scenarioRoutes(fastify: FastifyInstance) {
  /**
   * GET /api/scenarios
   * List all available scenarios with optional type filtering and pagination.
   */
  fastify.get(
    "/",
    { preHandler: [optionalAuth] },
    async (
      request: FastifyRequest<{ Querystring: ListScenariosQuery }>,
      reply: FastifyReply
    ) => {
      const { type, page = "1", limit = "20" } = request.query;
      const pageNum = Math.max(1, parseInt(page, 10));
      const limitNum = Math.min(50, Math.max(1, parseInt(limit, 10)));
      const skip = (pageNum - 1) * limitNum;

      const where = type
        ? { type: type as CreateScenarioBody["type"] }
        : {};

      const [scenarios, total] = await Promise.all([
        prisma.scenario.findMany({
          where,
          orderBy: { createdAt: "desc" },
          skip,
          take: limitNum,
          select: {
            id: true,
            title: true,
            description: true,
            type: true,
            createdAt: true,
            creator: {
              select: { id: true, username: true },
            },
            _count: {
              select: { games: true },
            },
          },
        }),
        prisma.scenario.count({ where }),
      ]);

      return reply.send({
        scenarios,
        pagination: {
          page: pageNum,
          limit: limitNum,
          total,
          totalPages: Math.ceil(total / limitNum),
        },
      });
    }
  );

  /**
   * GET /api/scenarios/:id
   * Get a single scenario with full details.
   */
  fastify.get(
    "/:id",
    { preHandler: [optionalAuth] },
    async (
      request: FastifyRequest<{ Params: { id: string } }>,
      reply: FastifyReply
    ) => {
      const { id } = request.params;

      const scenario = await prisma.scenario.findUnique({
        where: { id },
        include: {
          creator: {
            select: { id: true, username: true },
          },
          _count: {
            select: { games: true },
          },
        },
      });

      if (!scenario) {
        return reply.code(404).send({ error: "Scenario not found" });
      }

      return reply.send({ scenario });
    }
  );

  /**
   * POST /api/scenarios
   * Create a new scenario. Requires authentication.
   */
  fastify.post(
    "/",
    { preHandler: [requireAuth, rateLimit({ max: 10, windowMs: 60_000 })] },
    async (
      request: FastifyRequest<{ Body: CreateScenarioBody }>,
      reply: FastifyReply
    ) => {
      const { title, description, type, universeRules, mapData } = request.body;
      const userId = request.user!.id;

      if (!title || !description || !type) {
        return reply
          .code(400)
          .send({ error: "title, description, and type are required" });
      }

      const validTypes = ["HISTORICAL", "SCIFI", "FANTASY", "POP_CULTURE"];
      if (!validTypes.includes(type)) {
        return reply
          .code(400)
          .send({ error: `type must be one of: ${validTypes.join(", ")}` });
      }

      // TODO: Optionally call AI to generate/enhance universe rules from description

      const scenario = await prisma.scenario.create({
        data: {
          title,
          description,
          type,
          universeRules: universeRules ?? {},
          mapData: mapData ?? {},
          creatorId: userId,
        },
      });

      request.log.info({ scenarioId: scenario.id }, "Scenario created");
      return reply.code(201).send({ scenario });
    }
  );
}
