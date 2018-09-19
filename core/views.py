from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from .models import Experience
from about.models import About

#from django.views.generic.base import TemplateView
# Create your views here.


class PageListView(ListView):
    model = Experience

# Create your views here.

def index(request):
    abouts = About.objects.all()[:1]
    return render(request,"core/index.html", {'abouts':abouts})
