@echo off

cd docker || exit /b

REM Create environment file if missing
if not exist .env (
    copy .env.example .env
)

REM Build and start containers
docker compose up --build -d
