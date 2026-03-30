import type { FastifyInstance, FastifyRequest, FastifyReply } from "fastify";
import { PrismaClient } from "@prisma/client";
import { requireAuth } from "../middleware/auth.js";
import { rateLimit } from "../middleware/rateLimit.js";
import { createCheckoutSession } from "../services/stripe.js";

const prisma = new PrismaClient();

interface PurchaseBody {
  packageId: string;
}

// Token packages available for purchase
const TOKEN_PACKAGES = {
  starter: { tokens: 100, priceInCents: 499, name: "Starter Pack" },
  standard: { tokens: 500, priceInCents: 1999, name: "Standard Pack" },
  premium: { tokens: 1500, priceInCents: 4999, name: "Premium Pack" },
} as const;

export async function tokenRoutes(fastify: FastifyInstance) {
  /**
   * GET /api/tokens/balance
   * Get the authenticated user's current token balance and transaction history.
   */
  fastify.get(
    "/balance",
    { preHandler: [requireAuth] },
    async (request: FastifyRequest, reply: FastifyReply) => {
      const userId = request.user!.id;

      const [user, recentTransactions] = await Promise.all([
        prisma.user.findUnique({
          where: { id: userId },
          select: { tokens: true },
        }),
        prisma.tokenTransaction.findMany({
          where: { userId },
          orderBy: { createdAt: "desc" },
          take: 20,
          select: {
            id: true,
            amount: true,
            type: true,
            metadata: true,
            createdAt: true,
          },
        }),
      ]);

      return reply.send({
        balance: user?.tokens ?? 0,
        recentTransactions,
      });
    }
  );

  /**
   * POST /api/tokens/purchase
   * Initiate a token purchase via Stripe checkout.
   */
  fastify.post(
    "/purchase",
    { preHandler: [requireAuth, rateLimit({ max: 10, windowMs: 60_000 })] },
    async (
      request: FastifyRequest<{ Body: PurchaseBody }>,
      reply: FastifyReply
    ) => {
      const { packageId } = request.body;
      const userId = request.user!.id;

      const pkg = TOKEN_PACKAGES[packageId as keyof typeof TOKEN_PACKAGES];
      if (!pkg) {
        return reply.code(400).send({
          error: "Invalid package",
          availablePackages: Object.keys(TOKEN_PACKAGES),
        });
      }

      try {
        const session = await createCheckoutSession({
          userId,
          email: request.user!.email,
          packageId,
          packageName: pkg.name,
          priceInCents: pkg.priceInCents,
          tokens: pkg.tokens,
        });

        return reply.send({
          checkoutUrl: session.url,
          sessionId: session.id,
        });
      } catch (error) {
        request.log.error(error, "Failed to create checkout session");
        return reply
          .code(500)
          .send({ error: "Failed to initiate purchase" });
      }
    }
  );
}
