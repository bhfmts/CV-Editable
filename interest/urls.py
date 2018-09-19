from django.urls import path
from . import  views
from .views import InterestPageListView

urlpatterns = [
    path('', InterestPageListView.as_view(), name="interest"),
   ] 