from django.conf.urls import patterns, url

urlpatterns = patterns('apps.medicos.views',
    url(r'^listar/$', 'listar', name='medico_listar'),
    url(r'^mostrar/(?P<id>\d+)$', 'mostrar', name='medico_mostrar'),
    url(r'^autocompleteNomes', 'autocompleteNomes', name='medico_autocompleteNomes'),
    url(r'^buscaAgendaMedico', 'buscaAgendaMedico', name='medico_buscaAgendaMedico'),
    url(r'^buscaMedicosPorEspecialidade', 'buscaMedicosPorEspecialidade', name='medico_buscaMedicosPorEspecialidade'),
)
