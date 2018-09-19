from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Interest


#from django.views.generic.base import TemplateView
# Create your views here.



class InterestPageListView(ListView):
    model = Interest



