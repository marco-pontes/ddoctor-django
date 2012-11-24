from django.db import models
class Medicacao(models.Model):
    nome = models.CharField(max_length=200)
    tarja = models.CharField(max_length=200)
    bula = models.CharField(max_length=200)
    quantidade = models.IntegerField(max_length=200)
    unidade = models.CharField(max_length=200)
    fabricante = models.CharField(max_length=200)
    dataCompra = models.DateTimeField()
    
    class Meta:
        db_table = "medicacao"