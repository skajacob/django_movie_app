"""Models for users"""

from django.db import models


from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    birthday = models.DateField(blank=True, null=True)