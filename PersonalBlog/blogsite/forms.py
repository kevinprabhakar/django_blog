from django import forms
from .models import Post, UserProfile
from django.contrib.auth.models import User
from datetime import datetime

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model=User
        fields=['username','password','email']

class UserProfileForm(forms.ModelForm):

    class Meta:
        model=UserProfile
        fields=['website','picture']
