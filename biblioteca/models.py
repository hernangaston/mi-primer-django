from django.db import models

# Create your models here.

class Editor(models.Model):
	nombre = models.CharField(max_length=30)
	domicilio = models.CharField(max_length=50)
	ciudad = models.CharField(max_length=60)
	provincia = models.CharField(max_length=30)
	pais = models.CharField(max_length=50)
	website = models.URLField()
	#definimos unaclase meta dentro de otra clase
	#sirve para definir cuestiones especificas en un modelo
	class Meta:
		ordering=['nombre']
		verbose_name_plural = "Editores" 

	def __str__(self):
		return self.nombre

class Autor(models.Model):
	nombre = models.CharField(max_length=30)
	apellidos = models.CharField(max_length=40)
	email = models.EmailField('e-mail', blank=True)#se puede hacer tambien agregando verbose_name='e-mail' despues de blank
	#blank=True sidnifica que le decimos que el campo email no sea obligatorio podes dejarlo vacio por defecto todos tienen blank=False

	class Meta:
		ordering=['nombre']
		verbose_name_plural = "Autores"

	def __str__(self):
		return '%s %s' % (self.nombre, self.apellidos)#en la interfaz admin se mostraran nombre y apellidos del autor



class Libro(models.Model):
	titulo = models.CharField(max_length=100)
	autores = models.ManyToManyField(Autor)
	editor = models.ForeignKey('Editor', on_delete=models.PROTECT)
	fecha_publicacion = models.DateField(blank=True, null=True)#por defecto son blan y null False. En numeros y fechas para que django permita dejarlos vacios hay que especificar blank y null
	portada = models.ImageField(upload_to='portadas')

	class Meta:
		ordering=['titulo']
		verbose_name_plural = "Libros"

	def __str__(self):
		return self.titulo

