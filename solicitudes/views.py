from django.shortcuts import render
from .models import Solicitud
from rest_framework import viewsets
from .serializers import SolicitudSerializer


class SolicitudViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows solicitudes to be viewed or edited.
	"""
	queryset = Solicitud.objects.all()
	serializer_class = SolicitudSerializer