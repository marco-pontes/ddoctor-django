from django.db import models
import datetime

# Create your models here.
class Atendimento(models.Model):

    AGUARDANDO_CHEGADA = "aguardando_chegada"
    AGUARDANDO_ATENDIMENTO = "aguardando_atendimento"
    EM_ATENDIMENTO = "em_atendimento"
    FINALIZADO = "finalizado"
    
    paciente = models.ForeignKey('pacientes.Paciente')
    data = models.DateTimeField(null=True, blank=True) #Data do atendimento na clinica, diferente da data da consulta
    status = models.CharField(max_length=200)
    pago = models.BooleanField()
    precoTotal = models.FloatField()
    consulta = models.ForeignKey('consultas.Consulta')
    exames = models.ManyToManyField('exames.Exame', null=True, blank=True)
    
    class Meta:
        db_table = "atendimento"

    
    @classmethod
    def buscaAtendimentosPorPeriodo(cls, periodo):
        dataInicial = datetime.datetime.now()
        dataFinal = datetime.datetime.now()
        dataFinal = dataFinal.replace(hour=23, minute=59, second=59)
        if periodo == "dia":
            dataFinal = dataFinal + datetime.timedelta(hours=1)
        elif periodo == "semana":
            dataFinal = dataFinal + datetime.timedelta(days=7)
        elif periodo == "mes":
            dataFinal = dataFinal + datetime.timedelta(weeks=4)
        else:
            pass
        atendimentos = Atendimento.objects.filter(data__range=(dataInicial, dataFinal))
        return atendimentos

    #Busca os atendimentos de status especifico.
    @classmethod
    def buscaAtendimentosPorStatus(cls, status):
        atendimentos = Atendimento.objects.filter(status__iexact=status).order_by("-consulta__data")[:4]
        return atendimentos
    
    # Cria um novo atendimento com o status AGUARDANDO_CHEGADA, baseado na consulta recebida.
    # @param ddoctor.Consulta
    # @return ddoctor.Atendimento
    @classmethod
    def criaAtendimento(cls, consulta):
        atendimento = Atendimento()
        atendimento.paciente = consulta.paciente
        atendimento.status = Atendimento.AGUARDANDO_CHEGADA
        atendimento.pago = True #assumir que a consulta so e criada depois de paga.
        atendimento.precoTotal = consulta.medico.precoConsulta
        atendimento.consulta = consulta
        atendimento.save()
        return atendimento

    
    # Busca os atendimentos de um paciente especifico.
    # param String idPaciente
    # return List Atendimento
    @classmethod
    def buscaAtendimentosPorPaciente(cls, idPaciente):
        atendimentos = Atendimento.objects.filter(consulta__paciente__id__exact=idPaciente, status__iexact=Atendimento.AGUARDANDO_CHEGADA).order_by('-consulta__data')[:4]
        return atendimentos

    
    @classmethod
    def buscaAtendimentosMedico(cls, medico, status):
        atendimentos = Atendimento.objects.filter(consulta__medico__id__exact=medico.id, status__iexact=status)
        return atendimentos

    
    # Busca o historico de atendimentos do paciente.
    # @param ddoctor.usuario.Usuario
    # @param org.codehaus.groovy.grails.web.servlet.mvc.GrailsParameterMap
    # @return List<Atendimento>
    @classmethod
    def buscaAtendimentosAnteriores(cls, usuario):
        listaAtendimentos = Atendimento.objects.filter(paciente__id__exact=usuario.id, status__iexact=Atendimento.FINALIZADO).order_by("data")
        return listaAtendimentos
  
    # Agrupa os valores de atendimentos anteriores por dia
    # @param java.util.ArrayList<atendimentos>
    # @return List<ddoctor.Atendimento>
    @classmethod
    def agrupaAtendimentosPorDia(cls, atendimentos):
        atendimentosInfo = []
        datas = []
        for atendimento in atendimentos.all():
            datas.append(atendimento.data.strftime("%d/%m/%Y"))
        atendimentosDia = []
        
        for dia in datas:
            for atendimento in atendimentos:
                if atendimento.data.strftime("%d/%m/%Y") == dia:
                    atendimentosDia.append(atendimento)
        valor = 0.0
        for atendimento in atendimentosDia:
            data = atendimento.data
            valor += atendimento.precoTotal
        atendimentoInfo = {}    
        atendimentoInfo['data'] = data
        atendimentoInfo['valor'] = valor
        atendimentosInfo.append(atendimentoInfo)
        return atendimentosInfo 
