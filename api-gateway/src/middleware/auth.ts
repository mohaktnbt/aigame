import type { FastifyRequest, FastifyReply } from "fastify";
import { PrismaClient } from "@prisma/client";

// TODO: Replace with actual Clerk SDK verification once @clerk/fastify is configured
// import { clerkClient } from "@clerk/fastify";

const prisma = new PrismaClient();

export interface AuthenticatedUser {
  id: string;
  clerkId: string;
  email: string;
  username: string;
  tokens: number;
}

declare module "fastify" {
  interface FastifyRequest {
    user?: AuthenticatedUser;
  }
}

/**
 * Clerk authentication middleware for Fastify.
 * Verifies the session token and attaches the user to the request.
 */
export async function requireAuth(
  request: FastifyRequest,
  reply: FastifyReply
): Promise<void> {
  try {
    const authHeader = request.headers.authorization;

    if (!authHeader?.startsWith("Bearer ")) {
      reply.code(401).send({ error: "Missing or invalid authorization header" });
      return;
    }

    const token = authHeader.slice(7);

    // TODO: Verify token with Clerk SDK
    // const session = await clerkClient.sessions.verifySession(sessionId, token);
    // const clerkUser = await clerkClient.users.getUser(session.userId);

    // Stub: decode token to get clerkId (replace with real Clerk verification)
    const clerkId = token; // Placeholder

    const user = await prisma.user.findUnique({
      where: { clerkId },
    });

    if (!user) {
      reply.code(401).send({ error: "User not found" });
      return;
    }

    request.user = {
      id: user.id,
      clerkId: user.clerkId,
      email: user.email,
      username: user.username,
      tokens: user.tokens,
    };
  } catch (error) {
    request.log.error(error, "Authentication failed");
    reply.code(401).send({ error: "Authentication failed" });
  }
}

/**
 * Optional auth middleware - attaches user if token present, but doesn't reject.
 */
export async function optionalAuth(
  request: FastifyRequest,
  _reply: FastifyReply
): Promise<void> {
  try {
    const authHeader = request.headers.authorization;
    if (!authHeader?.startsWith("Bearer ")) return;

    const token = authHeader.slice(7);
    const clerkId = token; // TODO: Replace with Clerk verification

    const user = await prisma.user.findUnique({
      where: { clerkId },
    });

    if (user) {
      request.user = {
        id: user.id,
        clerkId: user.clerkId,
        email: user.email,
        username: user.username,
        tokens: user.tokens,
      };
    }
  } catch {
    // Silently continue without auth
  }
}
