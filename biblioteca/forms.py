from django import forms

class FormularioContactos(forms.Form):
	asunto = forms.CharField(max_length=100)
	email = forms.EmailField(required=False, label="Ingresa tu correo electronico")
	mensaje = forms.CharField(widget=forms.Textarea)
	
	def clean_mensaje(self):#esta funcion se llama sola si esta definida el framework la llama automaticamente
		mensaje = self.cleaned_data['mensaje']
		num_palabras = len(mensaje.split())
		if num_palabras < 4:
			raise forms.ValidationError("Se requieren 4 palabras!!")
		return mensaje
