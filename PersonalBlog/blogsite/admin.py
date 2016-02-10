from django.contrib import admin
from .models import Post, UserProfile
from django.contrib.auth.models import User

class PostAdmin(admin.ModelAdmin):
    list_display=["__unicode__","title","author","content","timestamp"]

class UserProfileAdmin(admin.ModelAdmin):
    list_display =["__unicode__","website","picture"]




admin.site.register(Post)
admin.site.register(UserProfile)

# Register your models here.
