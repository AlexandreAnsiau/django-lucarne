#!/bin/sh

# Wait for postgresql to start before doing migrations
if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

# Here we fix database setup error with nullable values
#python manage.py migrate auth zero --no-input
#python manage.py migrate directors zero --no-input
python manage.py makemigrations --no-input
python manage.py migrate --no-input
python manage.py migrate --run-syncdb

# Fix for static files
python manage.py collectstatic --no-input

# Fix for i18n
python manage.py compilemessages

# This will exec the CMD from your Dockerfile, i.e. "python manage runserver"
exec "$@"