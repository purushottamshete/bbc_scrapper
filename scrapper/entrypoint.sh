#!/bin/sh

python manage.py makemigrations --no-input
python manage.py migrate --no-input
gunicorn scrapper.wsgi:application --bind 0.0.0.0:8000