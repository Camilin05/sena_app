from .models import Instructor
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def instructores(request):
    lista_instructores = Instructor.objects.all().order_by('nombre', 'apellido')
    template = loader.get_template('lista_instructores.html')
    context = {
        'lista_instructores': lista_instructores,
        'total_instructores': lista_instructores.count(),
    }
    return HttpResponse(template.render(context, request))


