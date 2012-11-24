from django.conf.urls import patterns, url

urlpatterns = patterns('apps.mensagens.views',
    url(r'^listar/$', 'listar', name='mensagem_listar'),
    url(r'^inicializaModalDetalhes', 'inicializaModalDetalhes', name='mensagem_inicializaModalDetalhes'),
    url(r'^apagar/(?P<id>\d+)$', 'apagar', name='mensagem_apagar'),
)
