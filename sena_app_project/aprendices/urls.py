from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("aprendices", views.aprendices, name="aprendices"),
    ]
