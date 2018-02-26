from django.conf.urls import url

from django.urls import path

from psicologia.views import main, SesionesFacturadas, SesionesPendientes, PacientesList, autorizaciones, registro, \
    PacienteCreate, SesionUpdate, paciente_edit, SesionDelete, paciente_delete, SesionList, SesionCreate

from django.contrib.auth.views import login

urlpatterns = [
    url(r'^$', main, name='main'),
    url(r'^sesiones/$', SesionList.as_view(), name='sesiones'),
    url(r'^nuevasesion/$', SesionCreate.as_view(), name='nueva_sesion'),
    url(r'^sesiones/editarsesion/(?P<pk>\d+)/$', SesionUpdate.as_view(), name='sesion_editar'),
    url(r'^sesiones/eliminarsesion/(?P<pk>\d+)/$', SesionDelete.as_view(), name='sesion_eliminar'),
    url(r'^facturadas/$', SesionesFacturadas.as_view(), name='sesiones_facturadas'),
    url(r'^pendientes/$', SesionesPendientes.as_view(), name='sesiones_pendientes'),    
    url(r'^pacientes/$', PacientesList.as_view(), name='pacientes'),
    url(r'^nuevopaciente/$', PacienteCreate.as_view(), name='nuevo_paciente'),
    url(r'^pacientes/editarpaciente/(?P<id_paciente>\d+)/$', paciente_edit, name='paciente_editar'),
    url(r'^pacientes/eliminarpaciente/(?P<id_paciente>\d+)/$', paciente_delete, name='paciente_eliminar'),
    url(r'^autorizaciones/$', autorizaciones, name='autorizaciones'),
    path('login/', login, {'template_name': 'formulario_login.html'}, name='login'),
    path('registro/', registro, {'template_name': 'formulario_registro.html'}, name='registro'),
]
