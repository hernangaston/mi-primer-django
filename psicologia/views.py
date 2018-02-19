from django.shortcuts import render

# Create your views here.
from django.core.paginator import Paginator, InvalidPage, EmptyPage
#from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, render, redirect
from django.http import HttpResponseRedirect, HttpResponse

from psicologia.models import *
from psicologia.forms import *

def main(request):	
	return render(request, "index_psicologia.html")

def sesiones(request):
	
	sesion = SesionTerapeutica.objects.all()
	paciente = Paciente.objects.all()
	autorizacion = Autorizacion.objects.all()
	sesiones_facturadas = SesionTerapeutica.objects.filter(facturada = True)
	sesiones_pendientes = SesionTerapeutica.objects.filter(facturada = False)

	d = dict(sesion=sesion, paciente=paciente, autorizacion=autorizacion)
	
	return render(request, "sesiones.html", d)


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


def vistaSesion(request):
	if request.method == 'POST':
		form = FormularioSesion(request.POST)
		if form.is_valid():
			form.save()
		return redirect('main')
	else:
		form = FormularioSesion()
	d = dict(form= form)
	return  render(request, 'sesion_form.html', d)