#!/bin/bash

# Install dependencies
echo "install dependencies"
pip install -r requirements.txt

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

# Start server
echo "Starting server"
python manage.py runserver 0.0.0.0:8000