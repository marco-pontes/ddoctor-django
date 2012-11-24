from django.conf.urls import patterns, url

urlpatterns = patterns('apps.auth.views',
    url(r'^login/$', 'logIn', name='auth_login'),
    url(r'^logout/$', 'logOut', name="auth_logout"),
)
