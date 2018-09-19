from django.urls import path
from . import  views
from .views import PageListView
urlpatterns = [
    path('', views.index, name="home"),
    path('Experiencia', PageListView.as_view(), name="experiences"),    
] 