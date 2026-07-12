#!/bin/bash

cd docker || exit

if [ ! -f .env ]; then
  cp .env.example .env
fi

docker compose up --build -d
