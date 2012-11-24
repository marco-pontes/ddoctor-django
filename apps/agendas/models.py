from django.db import models

# Create your models here.
class Agenda(models.Model):
    consultas = models.ManyToManyField('consultas.Consulta', blank = True)
    
    class Meta:
        db_table = "agenda"