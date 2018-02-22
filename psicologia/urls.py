from django.conf.urls import url

from django.urls import path

from psicologia.views import main, sesiones, facturadas, pendientes, pacientes, autorizaciones, registro, vistaSesion, vistaPaciente, sesion_edit, paciente_edit, sesion_delete, paciente_delete

from django.contrib.auth.views import login

urlpatterns = [
    url(r'^$', main, name='main'),
    url(r'^sesiones/$', sesiones, name='sesiones'),
    url(r'^nuevasesion/$', vistaSesion, name='nueva_sesion'),
    url(r'^sesiones/editarsesion/(?P<id_sesion>\d+)/$', sesion_edit, name='sesion_editar'),
    url(r'^sesiones/eliminarsesion/(?P<id_sesion>\d+)/$', sesion_delete, name='sesion_eliminar'),
    url(r'^facturadas/$', facturadas),
    url(r'^pendientes/$', pendientes),    
    url(r'^pacientes/$', pacientes, name='pacientes'),
    url(r'^nuevopaciente/$', vistaPaciente, name='nuevo_paciente'),
    url(r'^pacientes/editarpaciente/(?P<id_paciente>\d+)/$', paciente_edit, name='paciente_editar'),
    url(r'^pacientes/eliminarpaciente/(?P<id_paciente>\d+)/$', paciente_delete, name='paciente_eliminar'),
    url(r'^autorizaciones/$', autorizaciones),
    path('login/', login, {'template_name': 'formulario_login.html'}, name='login'),
    path('registro/', registro, {'template_name': 'formulario_registro.html'}, name='registro'),
]
