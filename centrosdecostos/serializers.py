from .models import CentroDeCosto
from rest_framework import serializers


class CentroDeCostoSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = CentroDeCosto
		fields = ('nombre',
				  'cliente',
				  )