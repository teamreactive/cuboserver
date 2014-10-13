from django.shortcuts import render
from .models import Historial
from rest_framework import viewsets
from .serializers import HistorialSerializer


class HistorialViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows solicitudes to be viewed or edited.
	"""
	queryset = Historial.objects.all()
	serializer_class = HistorialSerializer