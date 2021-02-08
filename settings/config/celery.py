from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.signals import task_failure
from django.core.mail import mail_admins

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings.prod')
app = Celery('settings')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
  print('Request: {0!r}'.format(self.request))

@task_failure.connect()
def celery_task_failure_email(**kwargs):

  subject = u"[Celery] Task error in {sender.name}".format(**kwargs)

  message = u"""Task {sender.name} with id {task_id} raised exception:
{exception!r}


Task was called with args: {args} kwargs: {kwargs}.

The contents of the full traceback was:

{einfo}
  """.format(**kwargs)

  mail_admins(subject, message)
