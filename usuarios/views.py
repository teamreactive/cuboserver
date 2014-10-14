from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View
from rest_framework import viewsets
from StringIO import StringIO
from rest_framework.parsers import JSONParser

import json
from .models import Usuario
from productos.serializers import ProductoSerializer
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
    template_name = 'usuarios/index-codificador.html'
    # TODO -> REPLACE WITH THE GET_TEMPLATE FUNCTION #

    def get(self, request, *args, **kwargs):
        """
        Define the response of a HTTP GET request.
        Renders the home page with the given template name.
        """
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        """
        Define the response of a HTTP POST request.
        Validate and submit the corresponding form,
        and return the respective HTTP status code.
        """
        stream = StringIO(request.body)
        data = JSONParser().parse(stream)
        print request.body
        #serializer = ProductoSerializer(data=data)
        return HttpResponse(status=200)

def get_template(request, template_name):
    """
    Returns the respective template based on the
    logged user type, in case there's no user or
    if the user is invalid, returns the user
    login template.
    """
    template_name = 'usuaios/'
    if request.usuario.is_authenticated():
        if request.user.tipo == '3':
            return template_name + 'index-solicitante'
#       if request.user.tipo == '6':
#           return template_name + 'index-comprador'
    else:
        return template_name + 'index-login.html'