#!/bin/bash

cd docker || exit

# Create environment file if missing
if [ ! -f .env ]; then
  cp .env.example .env
fi

# Build and start containers
docker compose up --build -d
