from django.urls import path
from . import  views
from .views import AwardPageListView

urlpatterns = [
    path('', AwardPageListView.as_view(), name="award"),
   ] 