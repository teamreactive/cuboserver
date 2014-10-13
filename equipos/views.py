from django.shortcuts import render
from .models import Equipo
from rest_framework import viewsets
from .serializers import EquipoSerializer


class EquipoViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows solicitudes to be viewed or edited.
	"""
	queryset = Equipo.objects.all()
	serializer_class = EquipoSerializer