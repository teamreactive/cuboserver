from .models import TipoDeEquipo
from rest_framework import serializers


class TipoDeEquipoSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = TipoDeEquipo
		fields = ('nombre',
				  'descripcion',
				  'cliente',
    			 )