from .models import Compra
from rest_framework import serializers


class CompraSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Compra
		fields = ('cotizacion',
    			  'fecha_entregado',
    			  'entrega_parcial',
    			  'porcentaje_de_devolucion',
    			 )