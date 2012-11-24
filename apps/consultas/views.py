# Create your views here.
from apps.tarefas.models import Tarefa
from apps.consultas.models import Consulta
from django.contrib import messages
from django.utils.translation import gettext
from django.shortcuts import redirect
from django.shortcuts import render_to_response
from apps.atendimentos.models import Atendimento
from apps.mensagens.models import Mensagem
from django.template.context import RequestContext
from apps.medicos.models import Medico
from apps.consultas.forms import ConsultaForm
from django.http import HttpResponse
from django.template.loader import render_to_string
from utils.exceptions import ConsultationLimitException
import json
from utils.constantes import Constantes
from django.utils.datastructures import MultiValueDictKeyError
from apps.entrevistasMedicas.models import EntrevistaMedica
from apps.consultas.forms import EntrevistaMedicaForm

def confirmar(request):
    tarefa = Tarefa.objects.get(id=request.GET['tarefa_id'])
    consulta = Consulta.objects.get(id=request.GET['id'])
    consulta.status = Consulta.CONFIRMADA
    tarefa.status = Tarefa.FINALIZADA
    atendimento = Atendimento.criaAtendimento(consulta)
    if atendimento.id is not None:
        tarefa.save()
        consulta.save()
        Mensagem.consultaConfirmada(consulta, request.user)
        messages.success(request, gettext('consultation_confirmed_message'))
        if request.GET['irPara'] == 'dashboard':
            return redirect('dashboard_index')
        else:
            return redirect('consulta_mostrar', id=consulta.id)
        
    messages.success(request, gettext('consultation_confirmation_error'))
    return render_to_response('tarefa/_modalDetalhes.html', {'tarefa' : tarefa})

def cancelar(request):
    try:
        request.GET['tarefa_id']
        tarefa = Tarefa.objects.get(id=request.GET['tarefa_id'])
        tarefa.status = Tarefa.FINALIZADA
        tarefa.save()
    except MultiValueDictKeyError:
        pass
    consulta = Consulta.objects.get(id=request.GET['id'])
    consulta.status = Consulta.CANCELADA
    consulta.save()
    Mensagem.consultaCancelada(consulta, request.user)
    messages.success(request, gettext('consultation_canceled_message'))
    return redirect('consulta_mostrar', id=consulta.id)

def mostrar(request, id):
    tarefa = Tarefa()
    consulta = Consulta.objects.get(id=id)
    try:
        tarefa = Tarefa.objects.get(id=request.GET['tarefa_id'])
    except MultiValueDictKeyError:
        pass   
#    if consulta == None: 
#      return redirect('atendimento_listar')
    return render_to_response('consulta/mostrar.html', {'tarefa':tarefa, 'consulta':consulta}, 
                              context_instance=RequestContext(request))
    
def inicializaModalConsulta(request):
    consultaForm = ConsultaForm()
    consulta = Consulta()
    return render_to_response('consulta/_criar.html', {'consulta' : consulta, 'consultaForm':consultaForm},
                              context_instance=RequestContext(request))
    
def salvar(request):
    resposta = {}
    consulta = Consulta()
    consultaForm = ConsultaForm(request.POST)
    try:
        if consultaForm.is_valid():
            consulta = Consulta.criaConsulta(consultaForm, Consulta.PENDENTE, request.user)
            messages.success(request, gettext('create_consultation_success_message'))  
            resposta['msg'] = gettext('create_consultation_success_message')
            resposta['cod'] = Constantes.SUCESSO
        else:
            messages.error(request, gettext('create_consultation_fail_message'))  
            resposta['msg'] = gettext('create_consultation_fail_message')
            resposta['cod'] = Constantes.ERRO
    except ConsultationLimitException:
        messages.error(request, gettext('create_consultation_duplicate_message'))  
        resposta['msg'] = gettext('create_consultation_duplicate_message')
        resposta['cod'] = Constantes.ERRO
    finally:
        especialidadesMedicosDisponiveis = Medico.buscaEspecialidadesComMedicos()
        resposta['html'] = render_to_string("consulta/_criar.html", {'consulta': consulta, 'consultaForm':consultaForm, 'especialidadesMedicosDisponiveis': especialidadesMedicosDisponiveis}, 
                                            context_instance=RequestContext(request))
    return HttpResponse(json.dumps(resposta), mimetype='application/json')

def entrevistaMedica(request):
    entrevistaForm = EntrevistaMedicaForm()
    atendimento = Atendimento.objects.get(id=request.GET['atendimento_id'])
    if atendimento:
        atendimento.status = Atendimento.EM_ATENDIMENTO
        atendimento.save()
        return render_to_response('consulta/entrevistaMedica.html', 
                           {'atendimentoId':request.GET['atendimento_id'], 
                            'entrevistaForm':entrevistaForm},
                              context_instance=RequestContext(request))
    else:
        redirect("dashboard_medico")
        
def salvarEntrevista(request):
    entrevistaForm = EntrevistaMedicaForm(request.POST)
    atendimento = Atendimento.objects.get(id=request.POST['atendimento_id'])
    atendimento.status = Atendimento.FINALIZADO
    if (entrevistaForm.is_valid()):
        entrevista = entrevistaForm.save()
        atendimento.consulta.entrevistaMedica = entrevista
        atendimento.consulta.status = Consulta.FINALIZADA
        atendimento.save()
        messages.success(request, gettext('default_created_message %(id)i %(model)s')%{'id': entrevista.id,'model':gettext("entrevista_label")})  
        return redirect("dashboard_medico")
    else:
        messages.error(request, gettext('entrevista_validation_fail_message')) 
        return render_to_response('consulta/entrevistaMedica.html', 
                           {'atendimentoId': atendimento.id, 
                            'entrevistaForm':entrevistaForm},
                              context_instance=RequestContext(request)) 

def apagar(request, id):
    pass
