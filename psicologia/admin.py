from django.contrib import admin

from psicologia.models import SesionTerapeutica
from psicologia.models import Paciente
from psicologia.models import ObraSocial
from psicologia.models import Historia
from psicologia.models import Anamnesis
from psicologia.models import Autorizacion

# Register your models here.
admin.site.register(SesionTerapeutica)
admin.site.register(Paciente)
admin.site.register(ObraSocial)
admin.site.register(Historia)
admin.site.register(Anamnesis)
admin.site.register(Autorizacion)