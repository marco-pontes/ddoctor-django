from django.conf.urls import patterns, url

urlpatterns = patterns('apps.agendas.views',
    url(r'^inicializaModal', 'inicializaModal', name='agenda_inicializaModal'),
)
