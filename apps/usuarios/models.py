from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import UserManager

# Create your models here.
class Usuario(User):
    tarefas = models.ManyToManyField('tarefas.Tarefa', null=True, blank=True)
    endereco = models.ForeignKey('enderecos.Endereco')
    documento = models.CharField(max_length=200)
    
    # Use UserManager to get the create_user method, etc.
    objects = UserManager()
    
    class Meta:
        db_table = "usuario"