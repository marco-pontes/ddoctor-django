from django.db import models

# Create your models here.
class Especialidade(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.CharField(max_length=200)
    
    class Meta:
        db_table = "especialidade"