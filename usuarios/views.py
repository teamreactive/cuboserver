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
        data = fix_data(data)
        print data
        return HttpResponse(status=200)

def get_template(request, template_name):
    """
    Returns the respective template based on the
    logged user type, in case there's no user or
    if the user is invalid, returns the user
    login template.
    """
    template_name = 'usuarios/'
    if request.usuario.is_authenticated():
#         if request.usuario.tipo == '2':
#             return template_name + 'index-administrador-cliente'
        if request.usuario.tipo == '3':
            return template_name + 'index-solicitante'
        if request.usuario.tipo == '4':
            return template_name + 'index-codificador'
#         if request.usuario.tipo == '5':
#             return template_name + 'index-aprovador-solicitudes'
        if request.user.tipo == '6':
           return template_name + 'index-comprador'
#         if request.usuario.tipo == '7':
#             return template_name + 'index-aprovador-compra'
#         if request.usuario.tipo == '8':
#             return template_name + 'index-almacenista'
    return template_name + 'index-login.html'


def fix_data(data):
    for key in data:
        key = key.encode('utf-8')
        value = data[key].encode('utf-8')
        data[key] = value
    return data