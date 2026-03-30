import type { FastifyInstance, FastifyRequest, FastifyReply } from "fastify";
import { PrismaClient } from "@prisma/client";
import { requireAuth } from "../middleware/auth.js";

const prisma = new PrismaClient();

// TODO: Import Clerk webhook verification
// import { Webhook } from "svix";

interface ClerkWebhookBody {
  type: string;
  data: {
    id: string;
    email_addresses: Array<{ email_address: string }>;
    username: string | null;
    first_name: string | null;
    last_name: string | null;
  };
}

export async function authRoutes(fastify: FastifyInstance) {
  /**
   * POST /api/auth/webhook
   * Clerk webhook handler for user.created, user.updated, user.deleted events.
   */
  fastify.post(
    "/webhook",
    async (request: FastifyRequest<{ Body: ClerkWebhookBody }>, reply: FastifyReply) => {
      // TODO: Verify webhook signature with Svix
      // const WEBHOOK_SECRET = process.env.CLERK_WEBHOOK_SECRET;
      // const svixHeaders = {
      //   "svix-id": request.headers["svix-id"],
      //   "svix-timestamp": request.headers["svix-timestamp"],
      //   "svix-signature": request.headers["svix-signature"],
      // };
      // const wh = new Webhook(WEBHOOK_SECRET);
      // const payload = wh.verify(JSON.stringify(request.body), svixHeaders);

      const { type, data } = request.body;

      try {
        switch (type) {
          case "user.created": {
            const email = data.email_addresses[0]?.email_address;
            if (!email) {
              return reply.code(400).send({ error: "No email address found" });
            }

            await prisma.user.create({
              data: {
                clerkId: data.id,
                email,
                username:
                  data.username ??
                  `${data.first_name ?? "user"}_${data.id.slice(-6)}`,
                tokens: 100, // Starting bonus tokens
              },
            });

            request.log.info({ clerkId: data.id }, "User created from webhook");
            break;
          }

          case "user.updated": {
            const updatedEmail = data.email_addresses[0]?.email_address;
            await prisma.user.update({
              where: { clerkId: data.id },
              data: {
                ...(updatedEmail && { email: updatedEmail }),
                ...(data.username && { username: data.username }),
              },
            });
            break;
          }

          case "user.deleted": {
            await prisma.user.delete({
              where: { clerkId: data.id },
            });
            request.log.info({ clerkId: data.id }, "User deleted from webhook");
            break;
          }

          default:
            request.log.warn({ type }, "Unhandled webhook event type");
        }

        return reply.code(200).send({ received: true });
      } catch (error) {
        request.log.error(error, "Webhook processing failed");
        return reply.code(500).send({ error: "Webhook processing failed" });
      }
    }
  );

  /**
   * GET /api/auth/me
   * Returns the authenticated user's profile.
   */
  fastify.get(
    "/me",
    { preHandler: [requireAuth] },
    async (request: FastifyRequest, reply: FastifyReply) => {
      if (!request.user) {
        return reply.code(401).send({ error: "Not authenticated" });
      }

      const user = await prisma.user.findUnique({
        where: { id: request.user.id },
        select: {
          id: true,
          clerkId: true,
          email: true,
          username: true,
          tokens: true,
          createdAt: true,
          _count: {
            select: { games: true },
          },
        },
      });

      return reply.send({ user });
    }
  );
}
