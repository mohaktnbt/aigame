#!/bin/bash
# Project Nexus — Development Environment Setup
set -e

echo "=== Project Nexus Setup ==="

# Check prerequisites
command -v docker >/dev/null 2>&1 || { echo "Docker is required. Install it first."; exit 1; }
command -v node >/dev/null 2>&1 || { echo "Node.js is required. Install v20+."; exit 1; }
command -v python3 >/dev/null 2>&1 || { echo "Python 3.11+ is required."; exit 1; }

# Copy env file if not exists
if [ ! -f .env ]; then
  cp .env.example .env
  echo "Created .env from .env.example — fill in your API keys"
fi

# Start infrastructure
echo "Starting Docker services..."
docker compose up -d

# Wait for services to be ready
echo "Waiting for services to be healthy..."
sleep 10

# Frontend setup
echo "Setting up frontend..."
cd frontend
npm install
cd ..

# API Gateway setup
echo "Setting up API Gateway..."
cd api-gateway
npm install
npx prisma generate
npx prisma db push
cd ..

# Game Engine setup
echo "Setting up Game Engine..."
cd game-engine
if command -v uv >/dev/null 2>&1; then
  uv sync
else
  python3 -m pip install -e .
fi
cd ..

# Swarm Engine setup
echo "Setting up Swarm Engine..."
cd swarm-engine
if command -v uv >/dev/null 2>&1; then
  uv sync
else
  python3 -m pip install -e .
fi
cd ..

echo "=== Setup Complete ==="
echo ""
echo "Start services:"
echo "  Frontend:     cd frontend && npm run dev"
echo "  API Gateway:  cd api-gateway && npm run dev"
echo "  Game Engine:  cd game-engine && uv run uvicorn src.main:app --port 5001 --reload"
echo "  Swarm Engine: cd swarm-engine && uv run uvicorn src.main:app --port 5002 --reload"
