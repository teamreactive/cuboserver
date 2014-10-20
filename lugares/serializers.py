from .models import Lugar
from rest_framework import serializers


class LugarSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Lugar
		exclude = ('usuario')