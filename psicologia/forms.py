from django import forms

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

