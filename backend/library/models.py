from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class User(AbstractBaseUser):
    user_name = models.CharField(max_length=64)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField(max_length=255, unique=True)


class Project(models.Model):
    project_name = models.CharField(max_length=128)
    repo = models.CharField(max_length=128)
    users = models.ManyToManyField(User)


class Todo(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField(auto_created=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, models.PROTECT)
    is_active = models.BooleanField(default=True)
