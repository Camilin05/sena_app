from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('aprendices/', views.aprendices, name='aprendices'),
    ]
