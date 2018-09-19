from django.urls import path
from . import  views
from .views import EducationPageListView

urlpatterns = [
    path('', EducationPageListView.as_view(), name="education"),
   ] 