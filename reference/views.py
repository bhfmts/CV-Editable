from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Reference


#from django.views.generic.base import TemplateView
# Create your views here.



class ReferencePageListView(ListView):
    model = Reference
