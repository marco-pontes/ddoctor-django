from django.db import models
from apps.usuarios.models import Usuario


class Paciente(Usuario):
    historico = models.CharField(max_length=200)
    planoSaude = models.ForeignKey('planosSaude.PlanoSaude')
    
    class Meta:
        db_table = "paciente"