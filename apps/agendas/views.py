# Create your views here.
from django.utils.translation import gettext
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from apps.medicos.models import Medico
from django.contrib import messages

def inicializaModal(request):
    medico = Medico.objects.get(id=request.GET['medico_id'])
    if medico.id is None:
        messages.success(request, gettext('default_not_found_message'))
    return render_to_response('agenda/_mostrar.html', {'medico' : medico}, context_instance=RequestContext(request))

