from django import forms
from .models import Programa

class ProgramaForm(forms.Form):
    codigo = forms.CharField(max_length=20, unique=True, Label="Código del Programa", help_text="Ingrese el número del código.")
    nombre = forms.CharField(max_length=200, Label="Nombre del Programa", help_text="Ingrese el nombre del programa.")
    nivel_formacion = forms.ChoiceField(max_length=3, choices=Programa.NIVEL_FORMACION_CHOICES, Label="Nivel de Formación", help_text="Seleccione el nivel de formación.")
    modalidad = forms.ChoiceField(max_length=3, choices=Programa.MODALIDAD_CHOICES, default='PRE', Label="Modalidad", help_text="Seleccione la modalidad del programa.")
    duracion_meses = forms.CharField(Label="Duración en Meses", help_text="Ingrese la duración del programa en meses.")
    duracion_horas = forms.CharField(Label="Duración en Horas", help_text="Ingrese la duración del programa en horas.")
    descripcion = forms.CharField(Label="Descripción del Programa", help_text="Ingrese una descripción del programa.")
    competencias = forms.CharField(Label="Competencias a Desarrollar",  help_text="Ingrese las competencias que se desarrollarán en el programa.")
    perfil_egreso = forms.CharField(Label="Perfil de Egreso", help_text="Ingrese el perfil de egreso del programa.")
    requisitos_ingreso = forms.CharField(Label="Requisitos de Ingreso", help_text="Ingrese los requisitos de ingreso del programa.")
    centro_formacion = forms.CharField(max_length=200, Label="Centro de Formación", help_text="Ingrese el centro de formación del programa.")
    regional = forms.CharField(max_length=100, Label="Regional", help_text="Ingrese la regional del programa.")
    estado = forms.ChoiceField(max_length=3,choices=Programa.ESTADO_CHOICES, default='ACT', Label="Estado", help_text="Seleccione el estado del programa.")
    fecha_creacion = forms.DateField(Label="Fecha de Creación del Programa", help_text="Ingrese la fecha de creación del programa.")
    fecha_registro = forms.DateTimeField(auto_now_add=True, Label="Fecha de Registro", help_text="Fecha de registro del programa en el sistema.")