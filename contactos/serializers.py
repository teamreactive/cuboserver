from .models import Contacto
from rest_framework import serializers


class ContactoSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Contacto
		fields = ('nombre',
    			  'apellido',
    			  'telefono_fijo',
    			  'extension',
    			  'celular',
    			  'correo_electronico',
    			  'cargo',
    			  'perfil',
    			 )