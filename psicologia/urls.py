from django.conf.urls import url

from django.urls import path

from psicologia.views import main, sesiones, facturadas, pendientes, pacientes, autorizaciones, registro

from django.contrib.auth.views import login

urlpatterns = [
    url(r'^$', main, name='main'),
    url(r'^sesiones/$', sesiones),
    url(r'^facturadas/$', facturadas),
    url(r'^pendientes/$', pendientes),
    url(r'^pacientes/$', pacientes),
    url(r'^autorizaciones/$', autorizaciones),
    path('login/', login, {'template_name': 'formulario_login.html'}, name='login'),
    path('registro/', registro, {'template_name': 'formulario_registro.html'}, name='registro'),
]
