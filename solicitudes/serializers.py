from .models import Solicitud
from rest_framework import serializers


class SolicitudSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Solicitud
		fields = ('estado',
				  'lugar_entrega',
				  'fecha_creacion',
				  'fecha_requerida',
				  'solicitante',
				  'consolidador',
				  'aprobador',
				  'centro_de_costo',
				  'equipo',
				  'proyecto',
				  'productos',
				  )