from django.conf.urls import patterns, url

urlpatterns = patterns('apps.atendimentos.views',
    url(r'^listar/$', 'listar', name='atendimento_listar'),
    url(r'^inicializaModal/$', 'inicializaModal', name='atendimento_inicializaModal'),
    url(r'salvar', 'salvar', name='atendimento_salvar'),
    url(r'^mostrar/(?P<id>\d+)$', 'mostrar', name='atendimento_mostrar'),
    url(r'^buscaAtendimentosPorPaciente', 'buscaAtendimentosPorPaciente', name='atendimento_buscaAtendimentosPorPaciente'),
    url(r'^confirmarChegada', 'confirmarChegada', name='atendimento_confirmarChegada'),
)
