from django.conf.urls import patterns, url

urlpatterns = patterns('apps.consultas.views',
    url(r'^mostrar/(?P<id>\d+)$', 'mostrar', name="consulta_mostrar"),
    url(r'^confirmar/$', 'confirmar', name="consulta_confirmar"),
    url(r'^cancelar/$', 'cancelar', name="consulta_cancelar"),
    url(r'^inicializaModalConsulta', 'inicializaModalConsulta', name="consulta_inicializaModalConsulta"),
    url(r'^salvar/$', 'salvar', name="consulta_salvar"),
    url(r'^apagar/(?P<id>\d+)$', 'apagar', name="consulta_apagar"),
    url(r'^entrevistaMedica/$', 'entrevistaMedica', name="consulta_entrevistaMedica"),
    url(r'^salvarEntrevista/$', 'salvarEntrevista', name="consulta_salvarEntrevista"),
)
