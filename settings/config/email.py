from decouple import config


# Email configurations
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
SERVER_EMAIL = config('SERVER_EMAIL', default='backend@myapp.com')
EMAIL_HOST = config('EMAIL_HOST', default='')
EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='backend@myapp.com')
EMAIL_HOST_PASSWORD = config('EMAIL_PASSWORD', default='')
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL', default='App <suporte@myapp.com>')
NOREPLY_EMAIL = config('NOREPLY_EMAIL', default='naoresponder@myapp.com')