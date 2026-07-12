#!/bin/bash

cd src || exit

python manage.py migrate

read -p "Enter port (default 8000): " PORT
PORT=${PORT:-8000}

python manage.py runserver 0.0.0.0:$PORT
