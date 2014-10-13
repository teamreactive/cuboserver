from .models import Cotizacion
from rest_framework import serializers


class CotizacionSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Cotizacion
		fields = ('producto',
    			  'precio_unitario',
    			  'iva',
    			  'referencia',
    			  'validez',
    			  'forma_de_pago',
    			  'proveedor',
    			  'fecha_entrega',
    			 )