#!/bin/sh
set -e

MANAGE_PY=$(find / -type f -name manage.py -print -quit)
if [ -z "$MANAGE_PY" ]; then
  echo "Error: manage.py not found under /" >&2
  exit 1
fi
cd "$(dirname "$MANAGE_PY")"

su-exec "$USER" python manage.py migrate --noinput

su-exec "$USER" python manage.py collectstatic --noinput

USER_EXISTS_CMD="from django.contrib.auth import get_user_model; U = get_user_model(); exit(0) if U.objects.exists() else exit(1)"
if su-exec "$USER" python manage.py shell -c "$USER_EXISTS_CMD"; then
  echo "Superuser already exists"
else
  su-exec "$USER" python manage.py createsuperuser --noinput \
    --username "$DJANGO_SUPERUSER_USERNAME" \
    --email "$DJANGO_SUPERUSER_EMAIL"
fi

nginx

if [ "$1" = "--debug" ]; then
  exec su-exec "$USER" python manage.py runserver "0.0.0.0:${DJANGO_DEV_SERVER_PORT:-8000}"
else
  exec su-exec "$USER" gunicorn "${PROJECT_NAME}.wsgi:application" \
       --bind "0.0.0.0:${GUNICORN_PORT:-8000}" \
       --workers "${GUNICORN_WORKERS:-3}" \
       --timeout "${GUNICORN_TIMEOUT:-30}" \
       --log-level "${GUNICORN_LOG_LEVEL:-info}"
fi
