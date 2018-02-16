
from django.conf.urls import url

from biblioteca.views import main, formulario_buscar, buscar, contactos

urlpatterns = [
    url(r'^$', main),
    url(r'^formulario_buscar/$', formulario_buscar),
    url(r'^buscar/$', buscar),
    url(r'^contactos/$', contactos),
]
