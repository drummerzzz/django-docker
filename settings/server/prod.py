from .dev import *
from ..config.logger import *
from ..config.restframework import *

DEBUG = False

ALLOWED_HOSTS = ['*']

CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = []

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'