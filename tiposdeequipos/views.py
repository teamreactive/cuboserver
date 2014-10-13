from django.shortcuts import render
from .models import TipoDeEquipo
from rest_framework import viewsets
from .serializers import TipoDeEquipoSerializer


class TipoDeEquipoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows solicitudes to be viewed or edited.
    """
    queryset = TipoDeEquipo.objects.all()
    serializer_class = TipoDeEquipoSerializer