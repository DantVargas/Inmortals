from django.urls import path
from . import views

urlspatterns = [
    path('index', views.index, name='index'),
    
]