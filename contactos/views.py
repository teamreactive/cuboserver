from django.shortcuts import render
from .models import Contacto
from rest_framework import viewsets
from .serializers import ContactoSerializer


class ContactoViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows solicitudes to be viewed or edited.
	"""
	queryset = Contacto.objects.all()
	serializer_class = ContactoSerializer