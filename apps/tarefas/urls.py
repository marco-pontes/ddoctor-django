from django.conf.urls import patterns, url

urlpatterns = patterns('apps.tarefas.views',
    url(r'^listar/$', 'listar', name='tarefa_listar'),
    url(r'^mostrar/$', 'mostrar', name='tarefa_mostrar'),
    url(r'^inicializaModalDetalhes', 'inicializaModalDetalhes', name='tarefa_inicializaModalDetalhes'),
)
