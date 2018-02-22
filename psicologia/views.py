from django.shortcuts import render

# Create your views here.
from django.core.paginator import Paginator, InvalidPage, EmptyPage
#from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, render, redirect
from django.http import HttpResponseRedirect, HttpResponse

from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

from psicologia.models import *
from psicologia.forms import *

def main(request):	
	return render(request, "index_psicologia.html")

#vista basada en funciones
"""def sesiones(request):
	
	sesion = SesionTerapeutica.objects.all()
	paciente = Paciente.objects.all()
	autorizacion = Autorizacion.objects.all()
	sesiones_facturadas = SesionTerapeutica.objects.filter(facturada = True)
	sesiones_pendientes = SesionTerapeutica.objects.filter(facturada = False)

	d = dict(sesion=sesion, paciente=paciente, autorizacion=autorizacion)
	
	return render(request, "sesiones.html", d)"""
#misma vista que la de arriba pero basa en clases estoy usando esta
class SesionList(ListView):
	model = SesionTerapeutica
	template_name = "sesiones.html"




def facturadas(request):

	sesion = SesionTerapeutica.objects.filter(facturada = True)

	d = dict(sesion=sesion)

	return render(request, "sesiones.html", d)

def pendientes(request):

	sesion = SesionTerapeutica.objects.filter(facturada = False)

	d = dict(sesion=sesion)

	return render(request, "sesiones.html", d)

def autorizaciones(request):
	
	sesion = SesionTerapeutica.objects.all()
	paciente = Paciente.objects.all()
	autorizacion = Autorizacion.objects.all()

	d = dict(sesion=sesion, paciente=paciente, autorizacion=autorizacion)
	
	return render(request, "autorizaciones.html", d)

def pacientes(request):
	
	sesion = SesionTerapeutica.objects.all()
	paciente = Paciente.objects.all()
	autorizacion = Autorizacion.objects.all()

	d = dict(sesion=sesion, paciente=paciente, autorizacion=autorizacion)
	
	return render(request, "pacientes.html", d)

"""def login(request):
	email = request.POST.get('username','')
	password = request.POST.get('password','')
	form = FormularioLogin(request.POST.get('email'), request.POST.get('password',''))
	d = dict(form=form)
	return render(request, 'formulario_login.html', d)"""

def registro(request):
	form = FormularioRegsitro()
	d = dict(form = form)
	return render(request, 'formulario_registro.html', d)

"""Vista que renderiza el formulario para crear la sesion hecha como funcion
def vistaSesion(request):
	if request.method == 'POST':
		form = FormularioSesion(request.POST)
		if form.is_valid():
			form.save()
		return redirect('main')
	else:
		form = FormularioSesion()
	d = dict(form= form)
	return  render(request, 'sesion_form.html', d)"""


#Vista que renderiza el formulario para crear la sesion hecha como clase (hace lo mismo que la de arriba)
class SesionCreate(CreateView):
	model = SesionTerapeutica
	form_class = FormularioSesion
	template_name = 'sesion_form.html'
	success_url = reverse_lazy('sesiones')
	

def vistaPaciente(request):
	if request.method == 'POST':
		form = FormularioPaciente(request.POST)
		if form.is_valid():
			form.save()
		return redirect('main')
	else:
		form = FormularioPaciente()
	d = dict(form= form)
	return  render(request, 'paciente_form.html', d)


def sesion_edit(request, id_sesion):
	sesion = SesionTerapeutica.objects.get(id=id_sesion)
	if request.method == 'GET':
		form = FormularioSesion(instance = sesion)
	else:
		form = FormularioSesion(request.POST, instance=sesion)
		if form.is_valid():
			form.save()
		return redirect('sesiones')
	d = dict(form= form)
	return render(request, 'sesion_form.html', d)

def paciente_edit(request, id_paciente):
	paciente = Paciente.objects.get(id=id_paciente)
	if request.method == 'GET':
		form = FormularioPaciente(instance = paciente)
	else:
		form = FormularioPaciente(request.POST, instance=paciente)
		if form.is_valid():
			form.save()
		return redirect('pacientes')
	d = dict(form= form)
	return render(request, 'paciente_form.html', d)

def sesion_delete(request, id_sesion):
	sesion = SesionTerapeutica.objects.get(id=id_sesion)
	if request.method == 'POST':
		sesion.delete()
		return redirect('sesiones')
	d = dict(sesion=sesion)
	return render(request, 'sesion_delete.html', d)

def paciente_delete(request, id_paciente):
	paciente = Paciente.objects.get(id=id_paciente)
	if request.method == 'POST':
		paciente.delete()
		return redirect('pacientes')
	d = dict(paciente=paciente)
	return render(request, 'paciente_delete.html', d)


