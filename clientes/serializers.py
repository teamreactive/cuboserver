from .models import Cliente
from rest_framework import serializers


class ClienteSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Cliente
		fields = ('nit',
    			  'codigo_verificacion',
    			  'razon_social',
    			  'sigla',
    			  'logo'
    			 )