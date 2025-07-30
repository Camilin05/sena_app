from .models import Instructor
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def instructores(request):
    lista_instructores = Instructor.objects.all().values()
    template = loader.get_template('lista_instructores.html')
    context = {
        'lista_instructores': lista_instructores,
        'total_instructores': lista_instructores.count(),
    }
    return HttpResponse(template.render(context, request))

def __str__(self):
    return self.nombre + " " + self.apellido + " - " + self.especialidad + " - " + self.documento_identidad

def inicio(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())