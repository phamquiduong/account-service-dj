@echo off

set DB_DEFAULT_HOST=localhost
set DB_DEFAULT_PORT=5432
set DB_DEFAULT_USER=postgres
set DB_DEFAULT_PASS=postgres
set DB_DEFAULT_NAME=local

cd src || exit /b

echo Running tests...

pytest ^
  -v ^
  --tb=short ^
  --disable-warnings ^
  --durations=10
