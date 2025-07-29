#!/bin/bash
echo "=== Migrate database ==="
python manage.py migrate --noinput

echo "=== Collect static files ==="
python manage.py collectstatic --noinput

echo "=== Starting Gunicorn ==="
gunicorn phong.wsgi:application

#trang này dùng để cho chạy databese trên server