from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from accounts.users.manager import CustomUserManager as UserManager


class BaseUser(AbstractUser):
  
  username = models.EmailField(_('email address'), unique=True)

  @property
  def email(self):
    return self.username

  EMAIL_FIELD = 'username'
  REQUIRED_FIELDS = []
  objects = UserManager()

  def clean(self):
    try:
      super().clean()
    except:
      ...

  


class User(BaseUser):
  class Meta(AbstractUser.Meta):
    swappable = 'AUTH_USER_MODEL'
