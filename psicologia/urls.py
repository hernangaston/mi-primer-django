from django.conf.urls import url

from django.urls import path

from psicologia.views import main, SesionesFacturadas, SesionesPendientes, PacientesList, autorizaciones, registro, \
    PacienteCreate, SesionUpdate, paciente_edit, SesionDelete, paciente_delete, SesionList, SesionCreate

#decorador de urls para ocultarlas a usuarios no logueados
from django.contrib.auth.decorators import login_required

from django.contrib.auth.views import login, logout_then_login, password_reset, password_reset_done, password_reset_confirm, password_reset_complete

urlpatterns = [
    url(r'^$', main, name='main'),
    url(r'^sesiones/$', login_required(SesionList.as_view()), name='sesiones'),
    url(r'^nuevasesion/$', login_required(SesionCreate.as_view()), name='nueva_sesion'),
    url(r'^sesiones/editarsesion/(?P<pk>\d+)/$', login_required(SesionUpdate.as_view()), name='sesion_editar'),
    url(r'^sesiones/eliminarsesion/(?P<pk>\d+)/$', login_required(SesionDelete.as_view()), name='sesion_eliminar'),
    url(r'^facturadas/$', login_required(SesionesFacturadas.as_view()), name='sesiones_facturadas'),
    url(r'^pendientes/$', login_required(SesionesPendientes.as_view()), name='sesiones_pendientes'),    
    url(r'^pacientes/$', login_required(PacientesList.as_view()), name='pacientes'),
    url(r'^nuevopaciente/$', login_required(PacienteCreate.as_view()), name='nuevo_paciente'),
    url(r'^pacientes/editarpaciente/(?P<id_paciente>\d+)/$', paciente_edit, name='paciente_editar'),
    url(r'^pacientes/eliminarpaciente/(?P<id_paciente>\d+)/$', paciente_delete, name='paciente_eliminar'),
    url(r'^autorizaciones/$', autorizaciones, name='autorizaciones'),
    url(r'^login/$', login, {'template_name': 'formulario_login.html'}, name='login'),
    url(r'^logout/$', logout_then_login, name='logout'),
    url(r'^reset/password_reset/$', password_reset, {'template_name': 'registracion/password_reset_form.html',
     'email_template_name': 'registracion/password_reset_email.html'}, name='password_reset'),
    url(r'^reset/password_reset_done/$', password_reset_done, {'template_name': 'registracion/password_reset_done.html'}, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', password_reset_confirm, {'template_name': 'registracion/password_reset_confirm.html'}, name='password_reset_confirm'),
    url(r'^reset/done', password_reset_complete, {'template_name': 'registracion/password_reset_complete.html'}, name='password_reset_complete'),
    url(r'^registro/$', registro, {'template_name': 'formulario_registro.html'}, name='registro'),
]
