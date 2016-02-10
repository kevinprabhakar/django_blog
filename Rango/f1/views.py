from django.shortcuts import render
from django.http import HttpResponse
from .forms import SignUpForm, ContactForm
from django.core.mail import send_mail
from django.conf import settings

def index(request):

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    # The context_dict is where you get to define all the dynamic variables and such
    form=SignUpForm()

    context_dict = {
        'boldmessage': "I am bold font from the context",
        'UserName':request.user,
        'form':form
    }

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.

    return render(request, 'f1/index.html', context_dict)

def about(request):

    context_dict={'boldmessage':"WHATS UP BOY"}

    return render(request, 'f1/about.html', context_dict)

def form_practice(request):
    form = SignUpForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)      #basically just stores the data received from the form in an instance
        instance.save()                         #saves the data to the database

    context_dict={
        'form':form,
    }

    return render(request, 'f1/forms_practice.html', context_dict)

def contact(request):

    form=ContactForm(request.POST or None)

    context_dict={

        'form': form,

    }


    if form.is_valid():
        subject = form.cleaned_data.get('subject')
        message = form.cleaned_data.get('message')

        send_mail(subject, message, settings.EMAIL_HOST_USER, ['kevin.surya@gmail.com'], fail_silently=False)

    return render(request, 'f1/contact_form.html', context_dict)

# Create your views here.
