from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ddoctor.views.home', name='home'),
    # url(r'^ddoctor/', include('ddoctor.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^dashboard/', include('apps.dashboard.urls')),
    url(r'^medico/', include('apps.medicos.urls')),
    url(r'^paciente/', include('apps.pacientes.urls')),
    url(r'^atendimento/', include('apps.atendimentos.urls')),
    url(r'^consulta/', include('apps.consultas.urls')),
    url(r'^tarefa/', include('apps.tarefas.urls')),
    url(r'^mensagem/', include('apps.mensagens.urls')),
    url(r'^agenda/', include('apps.agendas.urls')),
    url(r'^', include('apps.auth.urls')),
)
