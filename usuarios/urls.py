#---------PASAMOS EL LA VISTA A LA URL PARA QUE MUESTRE EL JSON YA GENERADO------------

from django.conf.urls import url

from usuarios.views import RegistroUsuarios, UserApi

urlpatterns = [
    url(r'^registrar', RegistroUsuarios.as_view(), name="registrar"),
    url(r'^api', UserApi.as_view(), name="api")
]
