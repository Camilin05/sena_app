from django.urls import path
from . import views

app_name = 'instructores'

urlpatterns = [
    path('instructores/', views.instructores, name='lista_instructores'), 
    path('instructores/insturctor/<int:instructor_id>/', views.detalle_instructor, name='detalle_instructor'),
    path('crear_instructor/', views.InstructorFormView.as_view(), name='crear_instructor'),
    ]