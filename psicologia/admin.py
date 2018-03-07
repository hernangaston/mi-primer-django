from django.contrib import admin

from psicologia.models import SesionTerapeutica
from psicologia.models import Paciente
from psicologia.models import ObraSocial
from psicologia.models import Profesional
from psicologia.models import Autorizacion

# Register your models here.
admin.site.register(SesionTerapeutica)
admin.site.register(Paciente)
admin.site.register(ObraSocial)
admin.site.register(Autorizacion)
admin.site.register(Profesional)