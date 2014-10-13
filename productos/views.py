from django.shortcuts import render
from .models import Producto
from rest_framework import viewsets
from .serializers import ProductoSerializer


class ProductoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows solicitudes to be viewed or edited.
    """
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer