from django.contrib import admin

from .models import SignUp
from .forms import SignUpForm
# Register your models here.

class SignUpAdmin(admin.ModelAdmin):
    #This line below just displays timestamp and updated along with the email function on the admin page
    list_display = ["__unicode__", "timestamp", "updated"]
    #This line below just defines what forms are to be inputted
    form = SignUpForm
#    class Meta:
#       model = SignUp

admin.site.register(SignUp, SignUpAdmin)
