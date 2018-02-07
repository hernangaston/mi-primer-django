from django.shortcuts import render

# Create your views here.
from django.core.paginator import Paginator, InvalidPage, EmptyPage
#from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail

from biblioteca.models import *
from biblioteca.forms import FormularioContactos

def main(request):
	editor = Editor.objects.all()
	autor = Autor.objects.all()
	libro = Libro.objects.all()

	d = dict(editor=editor, autor=autor, libros=libro)
	
	return render(request, "principal.html", d)


def formulario_buscar(request):
	d = dict(req = request)
	return render(request, 'formulario_buscar.html', d)

def buscar(request):
	e = []
	if 'q' in request.GET:
		q = request.GET['q']
		if not q:
			e.append("Por favor introduce un termino de busqueda")
		elif len(q) > 20:
			e.append("Introduce un termino menor a 20 caracteres")
		else:
		    libro = Libro.objects.filter(titulo__icontains=q)
		    d = dict(libros = libro, query = q)
		    return render(request, 'resultados.html', d)
	d = dict(error = e)
	return render(request, 'formulario_buscar.html', d)

def contactos(request):
	if request.method == 'POST':
		form = FormularioContactos(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			send_mail(
				cd['asunto'],
				cd['mensaje'],
				cd.get('email', 'noreply@example.com'),
				['localhost'],
			)
			return HttpResponseRedirect('localhost')
	else:
		form = FormularioContactos()
	d = dict(form = form)
	return render(request, 'formulario_contactos.html', d)