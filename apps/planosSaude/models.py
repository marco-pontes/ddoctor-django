from django.db import models

# Create your models here.
class PlanoSaude(models.Model):
    nome = models.CharField(max_length=200)
    tipo = models.CharField(max_length=200)
    validade = models.DateTimeField()
    numero = models.IntegerField()
    
    class Meta:
        db_table = "plano_saude"