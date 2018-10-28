#!/bin/bash
python manage.py makemigrations && python manage.py migrate && python manage.py makemigrations importdata && python manage.py migrate importdata && python manage.py makemigrations metabase && python manage.py migrate metabase
python3 manage.py runserver 0.0.0.0:${PORT}
