from decouple import config

CELERY_TIMEZONE = 'America/Sao_Paulo'
CELERY_BROKER_URL = config('REDIS_URL', default='redis://redis:6379/0')
CELERY_BROKER_BACKEND = config('REDIS_URL', default='redis://redis:6379/0')
CELERY_RESULT_BACKEND = 'django-db'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
DJANGO_CELERY_BEAT_TZ_AWARE = False