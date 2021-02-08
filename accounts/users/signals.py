from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.users.models import User

@receiver(post_save, sender=User)
def save_user(sender, instance:User, created:bool, **kwargs):
  if created:
      print(instance)