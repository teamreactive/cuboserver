from django.shortcuts import render, redirect
from django.views.generic import View
from rest_framework import viewsets

from .models import Usuario
from .serializers import UsuarioSerializer


class UsuarioViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows solicitudes to be viewed or edited.
    """
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class HomeView(View):
    """
    View endpoint that renders the home.
    """
    template_name = 'usuarios/index.html'

    def get(self, request, *args, **kwargs):
        """
        Define the response of a HTTP GET request.
        Renters the home page with the given template.
        """
        return render(request, self.template_name)