
# Create your views here.
from django.shortcuts import render_to_response
from apps.pacientes.models import Paciente
import json
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger
from django.template.context import RequestContext

def listar(request):
    lista_pacientes = Paciente.objects.all()
    paginator = Paginator(lista_pacientes, 10) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        pacientes = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        pacientes = paginator.page(1)
    return render_to_response('paciente/listar.html', {'pacientes':pacientes}, context_instance=RequestContext(request))

def mostrar(request, id):
    pass

def autocompleteNomes(request):
    pacientes = Paciente.objects.filter(first_name__icontains=request.GET['term'])
    listaPacientes = [{'id':p.id, 'nome':p.first_name, 'documento':p.documento} for p in pacientes]
    return HttpResponse(json.dumps(listaPacientes), mimetype='application/json')
    