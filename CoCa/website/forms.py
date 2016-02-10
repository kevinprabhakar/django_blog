from django.contrib.auth.models import User
from django import forms
from models import UserProfile, Post

class UserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model=User
        fields=['username','password','email']

class UserProfileForm(forms.ModelForm):

    class Meta():
        model=UserProfile
        fields=['picture','website']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content', 'author']
