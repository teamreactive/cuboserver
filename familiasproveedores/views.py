from django.shortcuts import render
from .models import FamiliaProveedor
from rest_framework import viewsets
from .serializers import FamiliaProveedorSerializer


class FamiliaProveedorViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows solicitudes to be viewed or edited.
	"""
	queryset = FamiliaProveedor.objects.all()
	serializer_class = FamiliaProveedorSerializer