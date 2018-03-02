#----RESTFRAMEWORK MODELSERIALIZER--------
#---------CREAMOS UN SERIALIZER  O SEA UNA CLASE QUE SERIALIZA UN MODELO---------------


from rest_framework.serializers import ModelSerializer 

from django.contrib.auth.models import User

class UserSerializer(ModelSerializer):

	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email')