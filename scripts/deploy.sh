#!/bin/bash
# Project Nexus — Deploy to VPS
set -e

VPS_HOST="${VPS_HOST:-168.231.103.49}"
VPS_USER="${VPS_USER:-mohak}"
DEPLOY_DIR="/opt/project-nexus"

echo "=== Deploying Project Nexus to $VPS_HOST ==="

# Build frontend
echo "Building frontend..."
cd frontend
npm run build
cd ..

# Sync files to VPS
echo "Syncing files..."
rsync -avz --exclude='node_modules' --exclude='.next' --exclude='__pycache__' \
  --exclude='.venv' --exclude='.env' --exclude='*.pyc' \
  ./ "$VPS_USER@$VPS_HOST:$DEPLOY_DIR/"

# Remote setup
echo "Running remote setup..."
ssh "$VPS_USER@$VPS_HOST" << 'EOF'
  cd /opt/project-nexus
  docker compose up -d
  cd frontend && npm install && npm run build
  cd ../api-gateway && npm install && npx prisma db push
  cd ../game-engine && uv sync
  cd ../swarm-engine && uv sync
  echo "Deploy complete!"
EOF

echo "=== Deployment Complete ==="
