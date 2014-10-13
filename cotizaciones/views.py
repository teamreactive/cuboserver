from django.shortcuts import render
from .models import Cotizacion
from rest_framework import viewsets
from .serializers import CotizacionSerializer


class CotizacionViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows solicitudes to be viewed or edited.
	"""
	queryset = Cotizacion.objects.all()
	serializer_class = CotizacionSerializer