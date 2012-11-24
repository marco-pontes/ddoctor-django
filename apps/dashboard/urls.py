from django.conf.urls import patterns, url

urlpatterns = patterns('apps.dashboard.views',
    url(r'^index$', 'index', name="dashboard_index"),
    url(r'^atendente$', 'atendente', name="dashboard_atendente"),
    url(r'^medico', 'medico', name="dashboard_medico"),
    url(r'^paciente', 'paciente', name="dashboard_paciente"),
)
