from django.http import HttpResponse
from django.template import loader
from .models import Aprendiz

# Create your views here.
def aprendices (request):
    lista_aprendices = Aprendiz.objects.all().values()
    template = loader.get_template('aprendices.html')
    context = {
        'lista_aprendices': lista_aprendices        
    }
    return HttpResponse(template.render(context, request))
