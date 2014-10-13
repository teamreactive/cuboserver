from .models import Lugar
from rest_framework import serializers


class LugarSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Lugar
		fields = ('nombre',
				  'direccion',
				  'descripcion',
				  'usuario',
				  'contactos',
    			 )