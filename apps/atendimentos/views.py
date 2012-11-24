# Create your views here.
from django.shortcuts import render_to_response
from apps.consultas.models import Consulta
from apps.atendimentos.models import Atendimento
from apps.atendimentos.forms import AtendimentoForm
from django.utils.translation import ugettext as _
from django.contrib import messages
from utils.constantes import Constantes
from django.http import HttpResponse
import json
from utils.exceptions import ConsultationLimitException
from django.template.context import RequestContext
from django.template.loader import render_to_string
from django.core.paginator import PageNotAnInteger
from django.core.paginator import Paginator
from datetime import datetime

def listar(request):
    lista_atendimentos = Atendimento.objects.all()
    paginator = Paginator(lista_atendimentos, 10) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        atendimentos = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        atendimentos = paginator.page(1)
    return render_to_response('atendimento/listar.html', {'atendimentos':atendimentos}, context_instance=RequestContext(request))

def mostrar(request, id):
    atendimento = Atendimento.objects.get(id=id)
    return render_to_response('atendimento/mostrar.html', {'atendimento':atendimento}, context_instance=RequestContext(request))

def inicializaModal(request):
    atendimento = Atendimento()
    consulta = Consulta()
    atendimentoForm = AtendimentoForm()
    return render_to_response('atendimento/_criar.html', 
                              {'atendimento':atendimento, 'consulta':consulta, 'atendimentoForm':atendimentoForm}, context_instance=RequestContext(request))
    
def salvar(request):
    resposta = {}
    consulta = Consulta()
    atendimentoForm = AtendimentoForm(request.POST)
    try:
        if atendimentoForm.is_valid():
            consulta = Consulta.criaConsulta(atendimentoForm, Consulta.CONFIRMADA, request.user)
            Atendimento.criaAtendimento(consulta)
            messages.success(request, _('create_consultation_success_message'))  
            resposta['msg'] = _('create_consultation_success_message')
            resposta['cod'] = Constantes.SUCESSO
        else:
            messages.error(request, _('create_consultation_fail_message'))  
            resposta['msg'] = _('create_consultation_fail_message')
            resposta['cod'] = Constantes.ERRO
    except ConsultationLimitException:
        messages.error(request, _('create_consultation_duplicate_message'))  
        resposta['msg'] = _('create_consultation_duplicate_message')
        resposta['cod'] = Constantes.ERRO
    finally:
        resposta['html'] = render_to_string("atendimento/_criar.html", {'consulta': consulta, 'atendimentoForm':atendimentoForm}, context_instance=RequestContext(request))
        return HttpResponse(json.dumps(resposta), mimetype='application/json')

def buscaAtendimentosPorPaciente(request):
    atendimentosAguardandoChegada = Atendimento.buscaAtendimentosPorPaciente(request.GET["paciente_id"])
    return render_to_response('atendimento/_listaAtendimentos.html', {'atendimentosAguardandoChegada' : atendimentosAguardandoChegada}, context_instance=RequestContext(request))

def confirmarChegada(request):
    atendimento = Atendimento.objects.get(id=request.GET["atendimento_id"])
    resultado =  {}
    atendimento.status = Atendimento.AGUARDANDO_ATENDIMENTO
    atendimento.data = datetime.now()
    #TODO MUDAR TAREFAS RELACIONADAS
    atendimento.save()
    messages.success(request, _('atendimento_confirmado_message'))  
    resultado["status"] = Constantes.SUCESSO
    return HttpResponse(json.dumps(resultado), mimetype='application/json')
    
    