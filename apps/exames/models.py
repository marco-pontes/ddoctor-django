from django.db import models

# Create your models here.
class Exame(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.CharField(max_length=200)
    preco = models.FloatField()

    class Meta:
        db_table = "exame"