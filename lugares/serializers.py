from .models import Lugar
from rest_framework import serializers


class LugarSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Lugar
		fields = ('nombre','ciudad','seccion','numero_1','numero_2','numero_3','descripcion')