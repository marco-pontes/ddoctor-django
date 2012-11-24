from django.db import models

# Create your models here.
class Endereco(models.Model):
    rua = models.CharField(max_length=200)
    cep = models.CharField(max_length=200)
    numero = models.IntegerField()
    complemento = models.CharField(max_length=200)
    cidade = models.CharField(max_length=200)
    estado = models.CharField(max_length=200)
    
    class Meta:
        db_table = "endereco"
    
