#!/usr/bin/env bash

python manage.py collectstatic --noinput

python -m pip install --upgrade pip
pip install -r requirements.txt
pip install -r dev_requirements.txt

python manage.py makemigrations
python manage.py migrate

python manage.py runserver 0.0.0.0:8000