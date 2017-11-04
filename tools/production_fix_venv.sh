#!/bin/bash

# Install dependencies
cd ..
echo django-bootstrap3 > requirements_extra.txt
echo django-debug-toolbar >> requirements_extra.txt
cat requirements.txt | xargs -n 1 pip install
cat requirements_extra.txt | xargs -n 1 pip install

# Ready the database
python manage.py migrate
python manage.py makemigrations
python manage.py migrate

# Gather staticfiles
python manage.py collectstatic

#REMINDER: activate virtual environment after script-run
