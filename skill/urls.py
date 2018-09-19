from django.urls import path
from . import  views
from .views import SkillPageListView

urlpatterns = [
    path('', SkillPageListView.as_view(), name="skill"),
   ] 