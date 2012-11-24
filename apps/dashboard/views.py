# Create your views here.
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from apps.atendimentos.models import Atendimento
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from apps.consultas.models import Consulta
from apps.tarefas.models import Tarefa
from apps.mensagens.models import Mensagem
from django.shortcuts import redirect

@login_required
def index(request):
    request.session['django_language'] = "pt-br"
    if request.user.groups.all()[0].name == "ROLE_ATENDENTE":
        return redirect('dashboard_atendente')
    if request.user.groups.all()[0].name == "ROLE_MEDICO":
        return redirect("dashboard_medico")
    if request.user.groups.all()[0].name == "ROLE_PACIENTE":
        return redirect("dashboard_paciente")
    
@login_required   
@user_passes_test(lambda u: u.groups.all()[0].name == "ROLE_ATENDENTE")    
def atendente(request):
    atendimentosMes = Atendimento.buscaAtendimentosPorPeriodo("mes")
    atendimentosHoje = Atendimento.buscaAtendimentosPorPeriodo("dia")
    atendimentosAguardandoChegada = Atendimento.buscaAtendimentosPorStatus(Atendimento.AGUARDANDO_CHEGADA)
    consultasAguardandoConfirmacao = Consulta.buscaConsultasPorStatus(Consulta.PENDENTE)
    listaMensagens = []
    listaTarefas = []
    if request.user.id != None:
        listaMensagens = Mensagem.buscaMensagens(request.user)  
        listaTarefas = Tarefa.buscaTarefasPorStatus(request.user, Tarefa.PENDENTE)
    return render_to_response('dashboard/atendente.html', {'atendimentosMes':atendimentosMes, 'atendimentosHoje':atendimentosHoje, 
                                'atendimentosAguardandoChegada':atendimentosAguardandoChegada, 'consultasAguardandoConfirmacao':consultasAguardandoConfirmacao, 
                                'listaMensagens':listaMensagens, 'listaTarefas':listaTarefas}, context_instance=RequestContext(request))

@login_required   
@user_passes_test(lambda u: u.groups.all()[0].name == "ROLE_MEDICO")    
def medico(request):
    consultasFinalizadas = Atendimento.buscaAtendimentosMedico(request.user, Atendimento.FINALIZADO)
    proximosAtendimentos = Atendimento.buscaAtendimentosMedico(request.user, Atendimento.AGUARDANDO_ATENDIMENTO)
    listaMensagens = Mensagem.buscaMensagens(request.user)
    if request.user.id != None:
        listaMensagens = Mensagem.buscaMensagens(request.user)  
    
    return render_to_response('dashboard/medico.html', 
                              {'listaMensagens':listaMensagens, 'consultasFinalizadas':consultasFinalizadas, 'proximosAtendimentos':proximosAtendimentos}, 
                              context_instance=RequestContext(request))

@login_required   
@user_passes_test(lambda u: u.groups.all()[0].name == "ROLE_PACIENTE")    
def paciente(request):
    consultasNaoConfirmadas = Consulta.buscaConsultasPorUsuario(request.user, Consulta.PENDENTE)
    proximasConsultas = Consulta.buscaConsultasPorUsuario(request.user, Consulta.CONFIRMADA)
    atendimentosAnteriores = Atendimento.buscaAtendimentosAnteriores(request.user)
    graficoAtendimentosAnteriores =  Atendimento.agrupaAtendimentosPorDia(atendimentosAnteriores)
    listaMensagens = Mensagem.buscaMensagens(request.user)

    
    return render_to_response('dashboard/paciente.html',  {'consultasNaoConfirmadas':consultasNaoConfirmadas, 
                            'proximasConsultas':proximasConsultas, 'atendimentosAnteriores':atendimentosAnteriores, 
                            'graficoAtendimentosAnteriores':graficoAtendimentosAnteriores,'listaMensagens':listaMensagens}, 
                              context_instance=RequestContext(request))
