import json 

from rest_framework.views import APIView

from django.http import HttpResponse

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy


from usuarios.forms import RegistroForm
from usuarios.serializers import UserSerializer

class RegistroUsuarios(CreateView):
	model = User
	template_name = "registrar.html"
	form_class = RegistroForm
	success_url = reverse_lazy('sesiones')

#-------------------------VISTA PARA DJANGO REST FRAMEWORK-----------------------------
#---------------UNA VEZ HECHA LA VISTA MODIFICAMOS LA URL-------------------------
class UserApi(APIView):
	serializer = UserSerializer

	def get(self, request, format=None):
		lista = User.objects.all()
		response = self.serializer(lista, many=True)

		return HttpResponse(json.dumps(response.data), content_type='application/json')