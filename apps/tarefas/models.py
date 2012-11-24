
from django.db import models
from datetime import datetime
# Create your models here.
class Tarefa(models.Model):
    PENDENTE = "pendente"
    RECUSADA = "recusada"
    ACEITA = "aceita"
    FINALIZADA = "finalizada"
  
    nome = models.CharField(max_length=200)
    descricao = models.CharField(max_length=200)
    dataCriacao = models.DateField()
    status = models.CharField(max_length=200)
    consulta = models.ForeignKey('consultas.Consulta')
    
    class Meta:
        db_table = "tarefa"
    
    # Usada para recuperar as tarefas de um determinado status.
    # @param ddoctor.usuario.Usuario
    # @param {@link ddoctor.StatusTarefa}
    # @return {@link List}<Tarefa>
    @classmethod
    def buscaTarefasPorStatus(cls, usuario, status):
        listaTarefas = Tarefa.objects.filter(status__iexact = status, usuario = usuario.id).order_by("-dataCriacao")[:4]
        return listaTarefas

    
    # Usada para criar uma tarefa de confirmacao de consulta para um atendente.
    # param ddoctor.usuario.Usuario
    # param ddoctor.Consulta
    @classmethod
    def criaTarefaConfirmacaoConsulta(cls, usuario, consulta):
        tarefa = Tarefa()
        tarefa.nome = "Confirmar Nova Consulta"
        tarefa.status = Tarefa.PENDENTE
        tarefa.dataCriacao = datetime.now()
        tarefa.descricao = "Existe uma nova consulta marcada por um paciente e precisa ser confirmada."
        tarefa.consulta = consulta
        tarefa.save()
        usuario.tarefas.add(tarefa)
    
    

    
    
    
