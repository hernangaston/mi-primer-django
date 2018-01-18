from django.contrib import admin

from biblioteca.models import Libro, Autor, Editor

#para crear filtros de busqueda, barras de busqueda, campos de busqueda etc. en la parte de administracion
class AutorAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'apellidos', 'email')
	search_fields = ('nombre', 'apellidos')

class LibroAdmin(admin.ModelAdmin):
	list_display = ('titulo', 'editor', 'fecha_publicacion')
	list_filter = ('fecha_publicacion',)
	date_hieracrhy = 'fecha_publicacion'
	ordering = ('-fecha_publicacion',)#hace lo mismo que la clase interna Meta en los modelos excepto que unicamente usa el primer nombre de una campo en la lista
	#fields = ('titulo', 'autores', 'editor', 'fecha_publicacion')#la forma de editar loslibros se hara de acuerdo a este campo
	#fields = ('titulo', 'autores', 'editor', 'portada') tambien se pueden dejar fuera campos para qque no se puedan editar por los usuarios
	filter_horizontal = ('autores',)#para mejorar el uso de ManyToManyFields asi no osar la tecla control que is hay muchos puede resultar tedioso
	#se recomienda filter_horizontal  para cualquier ManyToManyFields que contenga mas de 10 objetos
	#existe filter_vertical que es lo mismo que horizontal cuestion de gustos
	raw_id_fields = ('editor',)#por si hay muchos (millares) de editores puede tardar mucho en cargarlos asi que mejor los reducimos a una caja de texto


# Register your models here. 

admin.site.register(Libro, LibroAdmin)
admin.site.register(Autor, AutorAdmin)
admin.site.register(Editor)
