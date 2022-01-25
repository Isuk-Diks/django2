#!/bin/sh

python manage.py migrate

python manage.py collectstatic --noinput
rm celery*.pid
celery multi start 1 -A super_news -B

gunicorn -b 0.0.0.0:8000 --reload -w 4 super_news.wsgi