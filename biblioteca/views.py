from django.shortcuts import render

# Create your views here.
from django.core.paginator import Paginator, InvalidPage, EmptyPage
#from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect


from biblioteca.models import *

def main(request):
	editor = Editor.objects.all()
	autor = Autor.objects.all()
	libro = Libro.objects.all()

	d = dict(editor=editor, autor=autor, libros=libro)
	return render_to_response("principal.html", d)