from django.shortcuts import render

def home(request):

    context_dict={



    }

    return render(request, "pages/home.html", context_dict)
# Create your views here.
