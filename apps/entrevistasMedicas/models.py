from django.db import models

# Create your models here.
class EntrevistaMedica(models.Model):
    problema = models.CharField(max_length=200)
    medicacao = models.CharField(max_length=200)
    observacoes = models.CharField(max_length=200)
    laudoMedico = models.CharField(max_length=200)
    altura = models.CharField(max_length=200)
    peso = models.CharField(max_length=200)
    pressao = models.CharField(max_length=200)

    class Meta:
        db_table = "entrevista_medica"
