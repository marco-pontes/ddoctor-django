# Create your views here.
from django.shortcuts import render_to_response
from apps.medicos.models import Medico
from django.http import HttpResponse
import json
from apps.consultas.models import Consulta
from django.utils.translation import ugettext as _
from utils.constantes import Constantes
from django.utils import formats
from django.template.context import RequestContext
from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger
from apps.especialidades.models import Especialidade

def listar(request):
    lista_medicos = Medico.objects.all()
    paginator = Paginator(lista_medicos, 10) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        medicos = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        medicos = paginator.page(1)
    return render_to_response('medico/listar.html', {'medicos':medicos}, context_instance=RequestContext(request))

def mostrar(request, id):
    pass

def autocompleteNomes(request):
    medicos = Medico.objects.filter(first_name__icontains=request.GET['term'])
    listaMedicos = [{'id':m.id, 'nome':m.first_name, 'documento':m.documento} for m in medicos]
    return HttpResponse(json.dumps(listaMedicos), mimetype='application/json')


def buscaAgendaMedico(request):
    medico = Medico.objects.get(id=request.GET["medico_id"])
    resposta = {}
    consultas = []
    for consulta in medico.agenda.consultas.all():
        if consulta.status == Consulta.CONFIRMADA:
            consultas.append({'id':consulta.id,'data':formats.date_format(consulta.data, "SHORT_DATETIME_FORMAT")})
    if len(consultas) > 0:
        resposta['consultas'] = consultas
        resposta['mensagem'] = _('get_agenda_success_message')
        resposta['codigo'] = Constantes.SUCESSO
    else:
        resposta['mensagem'] = _('get_agenda_fail_message')
        resposta['codigo'] = Constantes.SEM_RESULTADOS
    return HttpResponse(json.dumps(resposta), mimetype='application/json')

def buscaMedicosPorEspecialidade(request):
    especialidade = Especialidade.objects.get(id=request.GET["especialidade_id"])
    medicos = [{'id': m.id, 'nome':m.first_name} for m in Medico.objects.filter(especialidade__id__exact=especialidade.id)]
    return HttpResponse(json.dumps(medicos), mimetype='application/json')
