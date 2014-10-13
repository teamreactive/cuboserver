from .models import Producto
from rest_framework import serializers


class ProductoSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Producto
		fields = ('id',
				  'codigo_onu',
			      'nombre',
			      'descripcion',
			      'referencia',
			      'marca',
			      'servicio',
			      'familia_proveedor',
			      'tiempo_promedio',
			      'cliente',
			      'valido',
			      'contacto_novende',
			      'contacto_vende',
    			 )