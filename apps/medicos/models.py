from django.db import models
from apps.usuarios.models import Usuario
from apps.especialidades.models import Especialidade

# Create your models here.
class Medico(Usuario):
    crm = models.IntegerField()
    especialidade = models.ForeignKey('especialidades.Especialidade')
    agenda = models.ForeignKey('agendas.Agenda')
    precoConsulta = models.FloatField()
    biografia = models.CharField(max_length=200)
    
    class Meta:
        db_table = "medico"

    
    @classmethod
    def buscaEspecialidadesComMedicos(cls):
        especialidades = Especialidade.objects.filter(medico__pk__isnull=False).distinct('id', 'nome')
        return especialidades