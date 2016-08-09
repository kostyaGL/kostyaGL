from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.conf import settings
try:
    from django.contrib.auth import get_user_model
    User = settings.AUTH_USER_MODEL
except ImportError:
    from django.contrib.auth.models import User
from django.db import models


class Forum(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField(blank=True, default='')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(User, blank=True, null=True)

    def __str__(self):
        return '%s' % self.title


class Topic(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField(max_length=10000, blank=True, null=True)
    forum = models.ForeignKey(Forum)
    created = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(User, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    closed = models.BooleanField(blank=True, default=False)

    def __str__(self):
        return "%s" % self.title


class Post(models.Model):
    title = models.CharField(max_length=60)
    created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    topic = models.ForeignKey(Topic)
    body = models.TextField(max_length=10000)
    user_ip = models.GenericIPAddressField(blank=True, null=True)

    def __str__(self):
        return "%s" % self.created.strftime("%b %d, %I:%M %p")


class MyUser(AbstractUser):
    image = models.ImageField(null=True, blank=True)

