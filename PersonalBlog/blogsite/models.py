from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from datetime import datetime


class Post(models.Model):
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=50, default=User)
    content=models.TextField()
    timestamp=models.DateTimeField(blank=True, default=datetime.now())

    def __unicode__(self):
        return self.title

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username


# Create your models here.
