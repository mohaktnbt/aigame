import "dotenv/config";
import Fastify from "fastify";
import cors from "@fastify/cors";
import websocket from "@fastify/websocket";
import { Server } from "socket.io";
import { authRoutes } from "./routes/auth.js";
import { gameRoutes } from "./routes/games.js";
import { scenarioRoutes } from "./routes/scenarios.js";
import { tokenRoutes } from "./routes/tokens.js";
import { setupGameSocket } from "./websocket/gameSocket.js";

const PORT = Number(process.env.PORT) || 3001;
const HOST = process.env.HOST || "0.0.0.0";

async function buildServer() {
  const fastify = Fastify({
    logger: {
      level: process.env.LOG_LEVEL || "info",
    },
  });

  // Register CORS
  await fastify.register(cors, {
    origin: process.env.CORS_ORIGIN || "http://localhost:3000",
    credentials: true,
  });

  // Register WebSocket support
  await fastify.register(websocket);

  // Health check
  fastify.get("/health", async () => {
    return { status: "ok", timestamp: new Date().toISOString() };
  });

  // Register route modules
  await fastify.register(authRoutes, { prefix: "/api/auth" });
  await fastify.register(gameRoutes, { prefix: "/api/games" });
  await fastify.register(scenarioRoutes, { prefix: "/api/scenarios" });
  await fastify.register(tokenRoutes, { prefix: "/api/tokens" });

  // Set up Socket.io on the underlying HTTP server
  const io = new Server(fastify.server, {
    cors: {
      origin: process.env.CORS_ORIGIN || "http://localhost:3000",
      credentials: true,
    },
  });

  setupGameSocket(io);

  // Decorate fastify instance with io for use in routes
  fastify.decorate("io", io);

  return fastify;
}

async function main() {
  const server = await buildServer();

  try {
    await server.listen({ port: PORT, host: HOST });
    server.log.info(`Project Nexus API Gateway running on ${HOST}:${PORT}`);
  } catch (err) {
    server.log.error(err);
    process.exit(1);
  }
}

main();
