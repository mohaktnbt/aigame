#!/bin/bash
# Project Nexus — Database Migration
set -e

echo "=== Running Database Migrations ==="

# Prisma migrations (TimescaleDB)
echo "Running Prisma migrations..."
cd api-gateway
npx prisma migrate dev --name "$1"
cd ..

echo "=== Migrations Complete ==="
