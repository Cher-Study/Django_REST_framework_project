from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class Author(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    birthday_year = models.PositiveIntegerField()


class User(AbstractBaseUser):
    user_name = models.CharField(max_length=64)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
