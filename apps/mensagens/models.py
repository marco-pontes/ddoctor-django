from django.db import models
from django.contrib.auth.models import User
from django.utils import formats
from datetime import datetime

# Create your models here.
class Mensagem(models.Model):
    SUCESSO = "sucesso"
    INFO = "info"
    ATENCAO = "atencao"
    ERRO = "erro"
    destinatario = models.ForeignKey(User, related_name='mensagem_destinatario')
    remetente = models.ForeignKey(User, related_name='mensagem_remetente')
    assunto = models.CharField(max_length=200)
    tipo = models.CharField(max_length=200)
    corpo = models.CharField(max_length=500)
    dataEnvio = models.DateField()
    
    class Meta:
        db_table = "mensagem"
    
    # Metodo chamado para buscar mensagens de um usuario.
    # param User
    # return List Atendimento
    @classmethod
    def buscaMensagens(cls, usuario):
        mensagens = Mensagem.objects.filter(destinatario_id__exact=usuario.id)[:4]
        return mensagens
    
    # Metodo usado para criar uma mensagem para informar o usuario
    # sobre a confirmacao de uma consulta.
    # @param {@link ddoctor.Consulta} consulta
    @classmethod
    def consultaConfirmada(cls, consulta, usuario):
        mensagem = Mensagem()
        mensagem.destinatario = consulta.paciente
        mensagem.remetente = usuario
        mensagem.assunto = "A Sua Consulta Foi Confirmada!"
        mensagem.tipo = Mensagem.INFO
        dataFormatada = formats.date_format(consulta.data, "DATE_FORMAT")
        horaFormatada = formats.date_format(consulta.data, "TIME_FORMAT")
        mensagem.corpo = 'A consulta marcada para o dia  %(data)s \
                      foi confirmada no sistema! \
                      Compareca na clinica no dia %(data)s as %(hora)s \
                      para realizar a consulta com o medico %(nomeMedico)s.' %{"data": dataFormatada, "hora": horaFormatada, "nomeMedico": consulta.medico.first_name}
                      
        mensagem.dataEnvio  = datetime.now()
        mensagem.save()

    
    # Metodo usado para criar uma mensagem para informar o usuario
    # sobre o cancelamento de uma consulta.
    # @param {@link ddoctor.Consulta} consulta
    @classmethod
    def consultaCancelada(cls, consulta, usuario):
        mensagem = Mensagem()
        mensagem.destinatario = consulta.paciente
        mensagem.remetente = usuario
        mensagem.assunto = "Consulta nao confirmada"
        mensagem.tipo = Mensagem.INFO
        dataFormatada = formats.date_format(consulta.data, "DATE_FORMAT")
        mensagem.corpo = 'A consulta marcada para o dia  %(data)s \
                      foi cancelada no sistema!\
                      Marque a consulta em uma outra data ou ligue para a clinica para agendar um novo horario.'%{"data": dataFormatada}
        mensagem.dataEnvio  = datetime.now()
        mensagem.save()

    
    # Metodo usado para criar uma mensagem para avisar o atendente
    # de que uma nova consulta foi marcada por um usuario.
    # @param {@link ddoctor.usuario.Usuario} destinatario
    @classmethod
    def consultaMarcada(cls, destinatario, usuario):
        mensagem = Mensagem()
        mensagem.destinatario = destinatario
        mensagem.remetente = usuario
        mensagem.assunto = "Nova Consulta Marcada"
        mensagem.tipo = Mensagem.INFO
        mensagem.corpo = "Nova consulta incluida no sistema"
        mensagem.dataEnvio  = datetime.now()
        mensagem.save()