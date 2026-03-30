import type { FastifyRequest, FastifyReply } from "fastify";

interface RateLimitEntry {
  count: number;
  resetAt: number;
}

const store = new Map<string, RateLimitEntry>();

// Clean up expired entries periodically
setInterval(() => {
  const now = Date.now();
  for (const [key, entry] of store) {
    if (entry.resetAt <= now) {
      store.delete(key);
    }
  }
}, 60_000);

export interface RateLimitOptions {
  /** Maximum number of requests in the window */
  max: number;
  /** Window duration in milliseconds */
  windowMs: number;
}

const DEFAULT_OPTIONS: RateLimitOptions = {
  max: 100,
  windowMs: 60_000, // 1 minute
};

/**
 * Creates a rate limiting preHandler for Fastify routes.
 *
 * Uses an in-memory store. For production, replace with Redis-backed
 * rate limiting (e.g., using ioredis).
 *
 * TODO: Replace in-memory store with Redis for multi-instance deployments.
 */
export function rateLimit(opts: Partial<RateLimitOptions> = {}) {
  const options = { ...DEFAULT_OPTIONS, ...opts };

  return async function rateLimitHandler(
    request: FastifyRequest,
    reply: FastifyReply
  ): Promise<void> {
    // Use user ID if authenticated, otherwise fall back to IP
    const key =
      (request.user as { id?: string } | undefined)?.id ??
      request.ip ??
      "unknown";

    const now = Date.now();
    const entry = store.get(key);

    if (!entry || entry.resetAt <= now) {
      store.set(key, { count: 1, resetAt: now + options.windowMs });
      reply.header("X-RateLimit-Limit", options.max);
      reply.header("X-RateLimit-Remaining", options.max - 1);
      return;
    }

    entry.count++;

    if (entry.count > options.max) {
      const retryAfter = Math.ceil((entry.resetAt - now) / 1000);
      reply.header("Retry-After", retryAfter);
      reply.header("X-RateLimit-Limit", options.max);
      reply.header("X-RateLimit-Remaining", 0);
      reply.code(429).send({
        error: "Too many requests",
        retryAfter,
      });
      return;
    }

    reply.header("X-RateLimit-Limit", options.max);
    reply.header("X-RateLimit-Remaining", options.max - entry.count);
  };
}
