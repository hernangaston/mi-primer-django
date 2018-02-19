from django.conf.urls import url

from django.urls import path

from psicologia.views import main, sesiones, facturadas, pendientes, pacientes, autorizaciones, registro, vistaSesion

from django.contrib.auth.views import login

urlpatterns = [
    url(r'^$', main, name='main'),
    url(r'^sesiones/$', sesiones, name='sesiones'),
    url(r'^facturadas/$', facturadas),
    url(r'^pendientes/$', pendientes),
    url(r'^pacientes/$', pacientes),
    url(r'^autorizaciones/$', autorizaciones),
    url(r'^nuevasesion/$', vistaSesion, name='nueva_sesion'),
    path('login/', login, {'template_name': 'formulario_login.html'}, name='login'),
    path('registro/', registro, {'template_name': 'formulario_registro.html'}, name='registro'),
]
