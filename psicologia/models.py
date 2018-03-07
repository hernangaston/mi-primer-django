# Create your models here.


from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Profesional(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	matricula = models.CharField(max_length=50)

	class Meta:
		ordering = ["matricula"]
		verbose_name_plural = "Profesionales"
	
	def __str__(self):
		return self.matricula 

class SesionTerapeutica(models.Model):
	profesional = models.ForeignKey('Profesional', on_delete=models.CASCADE)
	paciente = models.ForeignKey('Paciente', on_delete=models.CASCADE)
	datos= models.TextField()
	fecha_sesion = models.DateField()
	facturada = models.BooleanField()
	numero_sesion = models.IntegerField()
	

	class Meta:
		ordering = ["fecha_sesion"] #establecer orden por defecto
		verbose_name_plural = "Sesiones Terapeuticas" #titulo que muestra la interfaz administrativa  porque agrega ls 's' por defecto 

	def __str__(self):
		return "%s %s" % (self.paciente.apellido, self.paciente.nombre) 

class Paciente(models.Model):
	profesional = models.ForeignKey('Profesional', on_delete=models.PROTECT)
	nombre = models.CharField(max_length=50)
	apellido = models.CharField(max_length=50)
	obra_social = models.ForeignKey('ObraSocial', on_delete=models.PROTECT)
	edad = models.IntegerField()
	telefono = models.IntegerField()
	dni = models.IntegerField()
	historia = models.TextField()
	medicacion = models.CharField(max_length=70)
	diagnostico = models.TextField()
	inicio_tratamiento = models.DateTimeField(default=timezone.now)

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

class Autorizacion(models.Model):
	fecha_autorizacion = models.DateField()
	presentada = models.BooleanField()
	paciente = models.ForeignKey('Paciente', on_delete=models.PROTECT)
	obra_social = models.ForeignKey('ObraSocial', on_delete=models.PROTECT)
	profesional = models.ForeignKey('Profesional', on_delete=models.CASCADE)

	class Meta:
		ordering = ["fecha_autorizacion"]
		verbose_name_plural = "Autorizaciones"

	def __str__(self):
		return self.paciente.nombre
