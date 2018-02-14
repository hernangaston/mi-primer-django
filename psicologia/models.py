from django.db import models

# Create your models here.
class SesionTerapeutica(models.Model): 
	paciente = models.ForeignKey('Paciente', on_delete=models.PROTECT)
	discurso = models.TextField()
	fecha_sesion = models.DateField()
	facturada = models.BooleanField()
	numero_sesion= models.IntegerField()

	class Meta:
		ordering = ["fecha_sesion"] #establecer orden por defecto
		verbose_name_plural = "Sesiones Terapeuticas" #titulo que muestra la interfaz administrativa  porque agrega ls 's' por defecto 

	def __int__(self):
		return self.numero_sesion


class Paciente(models.Model):
	nombre = models.CharField(max_length=50)
	apellido = models.CharField(max_length=50)
	obra_social = models.ForeignKey('ObraSocial', on_delete=models.PROTECT)
	edad = models.IntegerField()
	telefono = models.IntegerField()
	dni = models.IntegerField()
	historia = models.ForeignKey('Historia', on_delete=models.PROTECT)
	medicacion = models.TextField()

	class Meta:
		ordering = ["apellido"]
		verbose_name_plural = "Pacientes"
	
	def __str__(self):
		return "%s %s" % (self.apellido, self.nombre) 

class ObraSocial(models.Model):
	nombre = models.CharField(max_length=70)

	class Meta:
		ordering = ["nombre"]
		verbose_name_plural = "Obras Sociales"



	def __str__(self):
		return self.nombre

class Historia(models.Model):
	historia_del_paciente = models.TextField()
	anamnesis = models.ForeignKey('Anamnesis', on_delete=models.PROTECT)

	def __str__(self):
		return self.historia_del_paciente

class Anamnesis(models.Model):
	tratamientos = models.TextField()

	class Meta:
		verbose_name_plural = "Anamnesis"

	def __str__(self):
		return self.tratamientos

class Autorizacion(models.Model):
	fecha_autorizacion = models.DateField()
	presentada = models.BooleanField()
	paciente = models.ForeignKey('Paciente', on_delete=models.PROTECT)
	obra_social = models.ForeignKey('ObraSocial', on_delete=models.PROTECT)

	class Meta:
		ordering = ["fecha_autorizacion"]
		verbose_name_plural = "Autorizaciones"

	def __str__(self):
		return self.paciente.nombre

