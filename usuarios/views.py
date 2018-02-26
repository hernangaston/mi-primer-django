from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy


from usuarios.forms import RegistroForm

class RegistroUsuarios(CreateView):
	model = User
	template_name = "registrar.html"
	form_class = RegistroForm
	success_url = reverse_lazy('sesiones')
