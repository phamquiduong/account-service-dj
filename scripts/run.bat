@echo off

set DB_DEFAULT_HOST=localhost
set DB_DEFAULT_PORT=5432
set DB_DEFAULT_USER=postgres
set DB_DEFAULT_PASS=postgres
set DB_DEFAULT_NAME=local

cd src || exit /b

python manage.py wait_for_db
python manage.py migrate

set /p PORT=Enter port (default 8000):
if "%PORT%"=="" set PORT=8000

python manage.py runserver 0.0.0.0:%PORT%
