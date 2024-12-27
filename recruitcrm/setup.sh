#!/bin/bash

# install dependencies
pip install setuptools
pip install -r requirements.txt

# Run Django
python manage.py makemigrations
python manage.py migrate