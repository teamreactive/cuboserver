from .models import Historial
from rest_framework import serializers


class HistorialSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Historial
		fields = ('usuario',
				  'fecha',
				  'descripcion',
    			 )