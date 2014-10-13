from .models import Equipo
from rest_framework import serializers


class EquipoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Equipo
        fields = ('id',
        		  'nombre',
                  'descripcion',
                  'cantidad',
                  'tipo_de_equipo',
                  'cliente',
                  )