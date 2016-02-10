from __future__ import unicode_literals
from django.contrib.auth.models import User
from datetime import datetime

from django.db import models

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username

class Post(models.Model):
    content = models.CharField(max_length=140)
    author = models.CharField(max_length=40, default=User, blank=True)
    timestamp = models.DateTimeField(default=datetime.now, blank=True)

    def __unicode__(self):
        return self.content

# Create your models here.
