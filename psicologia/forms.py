from django import forms

from .models import SesionTerapeutica, Paciente, ObraSocial

"""class FormularioLogin(forms.Form):
	email = forms.EmailField(required=True, label="Ingresa tu correo electronico")
	password = forms.CharField(widget=forms.PasswordInput, required=True)
	
	def clean_mensaje(self):#esta funcion se llama sola si esta definida el framework la llama automaticamente
		#password = self.cleaned_data['password']
		num_caracteres = len(password)
		if num_caracteres < 8:
			raise forms.ValidationError("Se requieren 8 caracteres!!")
		return "%s %s" % (email, password)


class FormularioRegsitro(forms.Form):
	email = forms.EmailField(required=True, label="Ingresa tu correo electronico")
	password = forms.CharField(widget=forms.PasswordInput)
	password_confirmation = forms.CharField(widget=forms.PasswordInput)
	
	def clean_mensaje(self):#esta funcion se llama sola si esta definida el framework la llama automaticamente
		password = self.cleaned_data['password']
		password_confirmation = self.cleaned_data['password_confirmation']
		if password != password_confirmation:
			raise forms.ValidationError("Los passwords no coinciden!!")
		return "%s %s %s" % (email, password, password_confirmation)"""



class FormularioSesion(forms.ModelForm):

	class Meta:		
		model = SesionTerapeutica
		exclude = ('profesional',)
		fields = [
			'paciente',
			'datos',
			'fecha_sesion',
			'facturada',
			'numero_sesion',
		]

		labels = {
			'paciente': 'Paciente',
			'datos': 'Anotaciones de la sesion',
			'fecha_sesion': 'Fecha de la sesion',
			'facturada': 'Sesion Facturada o Presentada',
			'numero_sesion': 'Numero de seion'	
		} 

		widgets = {
			'paciente': forms.Select(attrs={'class':'form-control'}),
			'datos': forms.TextInput(attrs={'class':'form-control'}),
			'fecha_sesion': forms.DateInput(attrs={'class':'form-control'}),
			'facturada': forms.CheckboxInput(),
			'numero_sesion': forms.TextInput(attrs={'class':'form-control'}),
		}


class FormularioPaciente(forms.ModelForm):
	class Meta:
		model = Paciente
		exclude = ('profesional',)
		fields = [
			'nombre',
			'apellido',
			'obra_social',
			'edad',
			'telefono',
			'dni',
			'historia',
			'medicacion',
			'diagnostico',
		]

		labels = {
			'nombre': 'Nombre',
			'apellido': 'Apellido',
			'obra_social': 'Obra Social',
			'edad': 'Edad',
			'telefono': 'Telefono',
			'dni': 'D.N.I.',
			'historia': 'Historia Clinica',
			'medicacion': 'Medicacion',
			'diagnostico': 'Diagnostico',
		}

		widgets = {
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'apellido': forms.TextInput(attrs={'class':'form-control'}),
			'obra_social': forms.Select(attrs={'class':'form-control'}),
			'edad': forms.TextInput(attrs={'class':'form-control'}),
			'telefono': forms.TextInput(attrs={'class':'form-control'}),
			'dni': forms.TextInput(attrs={'class':'form-control'}),
			'historia': forms.TextInput(attrs={'class':'form-control'}),
			'medicacion': forms.TextInput(attrs={'class':'form-control'}),
			'diagnostico': forms.TextInput(attrs={'class':'form-control'}),
		}


class FormularioObraSocial(forms.ModelForm):
	class Meta:
		model = ObraSocial
		
		fields = [
			'nombre'
		]

		labels = {
			'nombre': 'Nombre',
		}

		widgets = {
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
		}