from django.urls import path 
from . import views

urlpatterns = [
    path("", views.teste, name="test")
]