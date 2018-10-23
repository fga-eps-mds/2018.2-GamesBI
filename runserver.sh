#!/bin/bash
python manage.py makemigrations && python manage.py migrate
python3 manage.py runserver 0.0.0.0:${PORT}
