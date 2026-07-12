#!/bin/bash

# Set database configuration
export DB_DEFAULT_HOST=localhost
export DB_DEFAULT_PORT=5432
export DB_DEFAULT_USER=postgres
export DB_DEFAULT_PASS=postgres
export DB_DEFAULT_NAME=local

cd src || exit

echo "Running tests..."

pytest \
  -v \
  --tb=short \
  --disable-warnings \
  --durations=10
