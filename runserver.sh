#!/bin/bash
python manage.py makemigrations && python manage.py migrate && python manage.py makemigrations API && python manage.py migrate API
python3 manage.py runserver 0.0.0.0:${PORT}
