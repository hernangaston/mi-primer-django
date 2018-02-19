from django import forms

from .models import SesionTerapeutica

class FormularioLogin(forms.Form):
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
		return "%s %s %s" % (email, password, password_confirmation)



class FormularioSesion(forms.ModelForm):

	class Meta:		
		model = SesionTerapeutica

		fields = [
			'paciente',
			'discurso',
			'fecha_sesion',
			'facturada',
			'numero_sesion',
		]

		labels = {
			'paciente': 'Paciente',
			'discurso': 'Anotaciones de la sesion',
			'fecha_sesion': 'Fecha de la sesion',
			'facturada': 'Sesion Facturada o Presentada',
			'numero_sesion': 'Numero de sesion',	
		} 

		widgets = {
			'paciente': forms.Select(attrs={'class':'form-control'}),
			'discurso': forms.Textarea(attrs={'class':'form-control'}),
			'fecha_sesion': forms.DateInput(attrs={'class':'form-control'}),
			'facturada': forms.CheckboxSelectMultiple(),
			'numero_sesion': forms.TextInput(attrs={'class':'form-control'}),
		}