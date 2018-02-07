from django.shortcuts import render

# Create your views here.
from django.core.paginator import Paginator, InvalidPage, EmptyPage
#from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect, HttpResponse

from psicologia.models import *

def main(request):
	
	sesion = SesionTerapeutica.objects.all()

	d = dict(sesion=sesion)
	
	return render(request, "main.html", d)