from django.urls import path
from . import  views
from .views import ReferencePageListView

urlpatterns = [
    path('', ReferencePageListView.as_view(), name="reference"),
   ] 