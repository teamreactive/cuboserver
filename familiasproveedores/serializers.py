from .models import FamiliaProveedor
from rest_framework import serializers


class FamiliaProveedorSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = FamiliaProveedor
		fields = ('nombre',
				  'cliente',
				  'contactos',
    			 )