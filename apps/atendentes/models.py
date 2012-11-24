from apps.usuarios.models import Usuario
from django.db import models
class Atendente(Usuario):
    turno = models.CharField(max_length=200)
    
    class Meta:
        db_table = "atendente"
    
    