release: python manage.py migrate
web: gunicorn server.wsgi
worker: celery -A app worker -l info --max-tasks-per-child=1 --concurrency=2
beat: celery -A app beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
