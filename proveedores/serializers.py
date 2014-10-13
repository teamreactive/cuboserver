from .models import Proveedor
from rest_framework import serializers


class ProveedorSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Proveedor
		fields = ('razon_social',
				  'sigla',
				  'nit',
				  'numero_verificacion',
				  'lugar',
				  'logo',
				  'cliente',
				  'calificacion',
				  'cotizacion_defecto',
    			 )