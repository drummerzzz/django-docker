
DEBUG_PROPAGATE_EXCEPTIONS = True

LOGGING = {
  'version': 1,
  'disable_existing_loggers': False,
  'filters': {
    'require_debug_false': {
        '()': 'django.utils.log.RequireDebugFalse'
    }
  },
  'formatters': {
    'verbose': {
      'format': (
          '%(asctime)s [%(process)d] [%(levelname)s] ' +
          'pathname=%(pathname)s lineno=%(lineno)s ' +
          'funcname=%(funcName)s %(message)s'
      ),
      'datefmt': '%Y-%m-%d %H:%M:%S'
    },
    'simple': {
      'format': '%(levelname)s %(message)s'
    }
  },
  'handlers': {
      'null': {
        'level': 'DEBUG',
        'class': 'logging.NullHandler',
      },
      'mail_admins': {
        'level': 'ERROR',
        'filters': ['require_debug_false'],
        'class': 'django.utils.log.AdminEmailHandler'
      },
      'console': {
        'level': 'DEBUG',
        'class': 'logging.StreamHandler',
        'formatter': 'verbose'
      }
  }
}