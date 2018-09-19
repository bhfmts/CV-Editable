from django.shortcuts import render
from .models import About

# Create your views here.

def about(request):
    abouts = About.objects.all()[:1]
    return render(request,"about/about.html", {'abouts':abouts})

    