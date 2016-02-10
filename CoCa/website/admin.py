from django.contrib import admin
from .models import Post, UserProfile

class PostAdmin(admin.ModelAdmin):
    list_display = ['__unicode__', 'message', 'author', 'timestamp']

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['__unicode__', 'picture', 'website']

admin.site.register(Post)
admin.site.register(UserProfile)
# Register your models here.
