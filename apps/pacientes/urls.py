from django.conf.urls import patterns, url

urlpatterns = patterns('apps.pacientes.views',
    url(r'^listar/$', 'listar', name='paciente_listar'),
    url(r'^mostrar/(?P<id>\d+)$', 'mostrar', name='paciente_mostrar'),
    url(r'^autocompleteNomes', 'autocompleteNomes', name='paciente_autocompleteNomes'),
)
