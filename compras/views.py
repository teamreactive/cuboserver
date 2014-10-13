from django.shortcuts import render
from .models import Compra
from rest_framework import viewsets
from .serializers import CompraSerializer


class CompraViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows solicitudes to be viewed or edited.
	"""
	queryset = Compra.objects.all()
	serializer_class = CompraSerializer