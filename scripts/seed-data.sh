#!/bin/bash
# Project Nexus — Seed Data
set -e

echo "=== Seeding Data ==="

# Seed scenarios into database
echo "Seeding scenario templates..."
for file in data/scenarios/templates/**/*.json; do
  echo "  Loading: $file"
  # TODO: Call API endpoint to import scenario
done

# Seed universe rules
echo "Seeding universe rules..."
for file in data/universe_rules/*.json; do
  echo "  Loading: $file"
  # TODO: Call API endpoint to import universe rules
done

# Seed base nation data
echo "Seeding nation data..."
# TODO: Call API endpoint to import nations

echo "=== Seeding Complete ==="
