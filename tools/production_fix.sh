#!/bin/bash

# Install dependencies
echo django-bootstrap3 > requirements_extra.txt
echo django-debug-toolbar >> requirements_extra.txt
cat requirements.txt | xargs -n 1 pip install --user
cat requirements_extra.txt | xargs -n 1 pip install --user

# Ready the database
cd ..
python manage.py migrate
python manage.py makemigrations
python manage.py migrate

# Gather staticfiles
python manage.py collectstatic
