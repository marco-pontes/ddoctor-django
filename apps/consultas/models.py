from django.db import models
from apps.medicos.models import Medico
from apps.pacientes.models import Paciente
from utils.exceptions import ConsultationLimitException
from apps.mensagens.models import Mensagem
from apps.atendentes.models import Atendente
from apps.tarefas.models import Tarefa
from django.db.models.query_utils import Q
from datetime import datetime
from apps.consultas.forms import ConsultaForm


# Create your models here.
class Consulta(models.Model):
    CONFIRMADA = "confirmada"
    CANCELADA = "cancelada"
    PENDENTE = "pendente"
    FINALIZADA = "finalizada"

    medico = models.ForeignKey('medicos.Medico')
    paciente = models.ForeignKey('pacientes.Paciente')
    data = models.DateTimeField()
    status = models.CharField(max_length=200)
    entrevistaMedica = models.ForeignKey('entrevistasMedicas.EntrevistaMedica', null = True, blank = True)
    
    class Meta:
        db_table = "consulta"

    # Busca todas as consultas de um determinado status.
    # @return Consulta
    @classmethod
    def buscaConsultasPorStatus(cls, status):
        consultas = Consulta.objects.filter(status__iexact=status)
        return consultas
    
    # Cria uma consulta, manda mensagens de aviso e cria tarefas para confirmacao recebendo params.
    # param java.util.Map
    # return ddoctor.Consulta
    @classmethod
    def criaConsulta(cls, form, status, usuario):
        if type(form) is ConsultaForm:
            medicoId = form.cleaned_data['medico']
        else:
            medicoId = form.cleaned_data['idMedico']
        pacienteId = form.cleaned_data['idPaciente']
        consulta = Consulta()
        medico = Medico.objects.get(id=medicoId)
        paciente = Paciente.objects.get(id=pacienteId)
        consulta.medico = medico
        consulta.paciente = paciente
        consulta.status = status
        consulta.data = form.cleaned_data['dataConsulta']
        if Consulta.isConsultaDuplicada(medico, paciente):
            raise ConsultationLimitException, 'O paciente %(nomePaciente)s ja tem uma consulta\
             marcada com o medico %(nomeMedico)s' %{'nomePaciente':paciente.first_name, 'nomeMedico':medico.first_name}
        consulta.save()
        medico.agenda.consultas.add(consulta)
        Mensagem.consultaMarcada(medico, usuario)
        if status == Consulta.PENDENTE:
            Tarefa.criaTarefaConfirmacaoConsulta(medico, consulta)
        for atendente in Atendente.objects.all():
            Mensagem.consultaMarcada(atendente, usuario)
            if status == Consulta.PENDENTE:
                Tarefa.criaTarefaConfirmacaoConsulta(atendente, consulta)
        return consulta

    # Usado para buscar os atendimentos de um paciente e um medico especifico, com status confirmado ou pendente.
    # Usado para evitar a duplicacao de consultas.
    # return List ddoctor.Consulta
    @classmethod
    def buscaConsultas(cls, medico, paciente):
        consultas = Consulta.objects.filter(Q(status__iexact=Consulta.PENDENTE) | Q(status__iexact=Consulta.CONFIRMADA), 
                                            medico__id__exact=medico.id, paciente__id__exact=paciente.id)
        return consultas

    # Usada para verificar se o paciente ja marcou uma consulta com um medico especifico.
    # return Boolean
    @classmethod
    def isConsultaDuplicada(cls, medico, paciente):
        consultasMarcadas = Consulta.buscaConsultas(medico, paciente)
        if len(consultasMarcadas) == 0:
            return False
        else:
            return True

    # Busca todas as consultas de um usuario e status especifico.
    # @return List<ddoctor.Consulta>
    @classmethod
    def buscaConsultasPorUsuario(cls, usuario, status):
        consultas = Consulta.objects.filter(paciente__id__exact=usuario.id, status__iexact=status)
        return consultas
    
    
    
