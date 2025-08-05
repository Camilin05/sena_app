from django.http import HttpResponse
from django.template import loader
from .models import Aprendiz, Curso
from django.shortcuts import get_object_or_404

# Create your views here.
def aprendices (request):
    lista_aprendices = Aprendiz.objects.all().values()
    template = loader.get_template('lista_aprendices.html')
    context = {
        'lista_aprendices': lista_aprendices,
        'total_aprendices': lista_aprendices.count(),
    }
    return HttpResponse(template.render(context, request))

def __str__(self):
    return self.nombre + " " + self.apellido + " - " + self.programa + " - " + self.documento_identidad
def inicio(request):
    total_aprendices = Aprendiz.objects.count()
    total_cursos = Curso.objects.count()
    cursos_activos = Curso.objects.filter(estado__in=['INI', 'EJE']).count()
    template = loader.get_template('index.html')
    context = {
        'total_aprendices': total_aprendices,
        'total_cursos': total_cursos,
        'cursos_activos': cursos_activos,
    }
    return HttpResponse(template.render(context, request))

def lista_cursos(request):
    lista_cursos = Curso.objects.all().order_by('-fecha_inicio')
    template = loader.get_template('lista_curso.html')
    context = {
        'lista_cursos': lista_cursos,
        'total_cursos': lista_cursos.count(),
        'titulo': 'Lista de Cursos',
    }
    return HttpResponse(template.render(context, request))

def detalle_curso(request, curso_id):
    curso = get_object_or_404(Curso, pk=curso_id)
    aprendices_curso = curso.aprendizcurso_set.all()
    instructoqres_curso = curso.instructores.all()
    template = loader.get_template('detalle_curso.html')
    context = {
        'curso': curso,
        'aprendices_curso': aprendices_curso,
        'instructoqres_curso': instructoqres_curso,
        'titulo': 'Detalle del Curso',
    }
    return HttpResponse(template.render(context, request))
