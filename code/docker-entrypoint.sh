#!/bin/sh
# vim:sw=4:ts=4:et

set -e

su-exec "$USER" python manage.py migrate --noinput

exec "$@"
