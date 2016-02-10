from __future__ import unicode_literals

from django.db import models

class SignUp(models.Model):
    email = models.EmailField()
    fullname = models.CharField(max_length=30, blank=False, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated= models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self): #__str__ instead for python 3
        return str(self.email)

class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    subject = models.CharField(max_length=30)
    message = models.TextField(max_length=None)

    def __unicode__(self):
        return self.name


# Create your models here.
