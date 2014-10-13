from django.shortcuts import render
from .models import CentroDeCosto
from rest_framework import viewsets
from .serializers import CentroDeCostoSerializer


class CentroDeCostoViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows solicitudes to be viewed or edited.
	"""
	queryset = CentroDeCosto.objects.all()
	serializer_class = CentroDeCostoSerializer