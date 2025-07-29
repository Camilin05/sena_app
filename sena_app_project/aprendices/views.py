from django.http import HttpResponse
from django.template import loader
from .models import Aprendiz

# Create your views here.
def aprendices (request):
    lista_aprendices = Aprendiz.objects.all().values()
    template = loader.get_template('lista_aprendices.html')
    context = {
        'lista_aprendices': lista_aprendices        
    }
    return HttpResponse(template.render(context, request))

def __str__(self):
    return self.nombre + " " + self.apellido + " - " + self.programa + " - " + self.documento_identidad
def inicio(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())