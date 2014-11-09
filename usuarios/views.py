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
from lugares.models import Lugar
from lugares.serializers import LugarSerializer

from django.core.exceptions import ValidationError


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

    template_name = 'usuarios/index-solicitante.html'
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
        # print '#######path_info#######'
        #print request.body
        # print '######scheme########'
        # print request.scheme

        # stream = StringIO(request.body)
        # data = JSONParser().parse(stream)
        # serializer = ProductoSerializer(data=data)
        # print serializer.errors
        if save_lugar(request):
            return HttpResponse(status=200)
        return HttpResponse(status=400)


class HomeView2(View):
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
        # print '#######path_info#######'
        #print request.body
        # print '######scheme########'
        # print request.scheme

        # stream = StringIO(request.body)
        # data = JSONParser().parse(stream)
        # serializer = ProductoSerializer(data=data)
        # print serializer.errors
        if save_lugar(request):
            return HttpResponse(status=200)
        return HttpResponse(status=400)


class HomeView3(View):
    """
    View endpoint that renders the home.
    """

    template_name = 'usuarios/index-comprador.html'
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
        # print '#######path_info#######'
        #print request.body
        # print '######scheme########'
        # print request.scheme

        # stream = StringIO(request.body)
        # data = JSONParser().parse(stream)
        # serializer = ProductoSerializer(data=data)
        # print serializer.errors
        if save_lugar(request):
            return HttpResponse(status=200)
        return HttpResponse(status=400)

class HomeView4(View):
    """
    View endpoint that renders the home.
    """

    template_name = 'usuarios/index-aprobador-de-solicitudes.html'
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
        # print '#######path_info#######'
        #print request.body
        # print '######scheme########'
        # print request.scheme

        # stream = StringIO(request.body)
        # data = JSONParser().parse(stream)
        # serializer = ProductoSerializer(data=data)
        # print serializer.errors
        if save_lugar(request):
            return HttpResponse(status=200)
        return HttpResponse(status=400)
class HomeView5(View):
    """
    View endpoint that renders the home.
    """

    template_name = 'usuarios/index-aprobador-de-compra.html'
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
        # print '#######path_info#######'
        #print request.body
        # print '######scheme########'
        # print request.scheme

        # stream = StringIO(request.body)
        # data = JSONParser().parse(stream)
        # serializer = ProductoSerializer(data=data)
        # print serializer.errors
        if save_lugar(request):
            return HttpResponse(status=200)
        return HttpResponse(status=400)

def get_template(request, template_name):
    """
    Returns the respective template based on the
    logged user type, in case there's no user or
    if the user is invalid, returns the user
    login template.
    """
    template_name = 'usuarios/'
    if request.usuario.is_authenticated():
        if request.usuario.tipo == '2':
            return template_name + 'index-administrador-cliente'
        elif request.usuario.tipo == '3':
            return template_name + 'index-solicitante'
        elif request.usuario.tipo == '4':
            return template_name + 'index-codificador'
        elif request.usuario.tipo == '5':
            return template_name + 'index-aprobador-solicitudes'
        elif request.user.tipo == '6':
            return template_name + 'index-comprador'
        elif request.usuario.tipo == '7':
            return template_name + 'index-aprobador-compra'
        elif request.usuario.tipo == '8':
            return template_name + 'index-almacenista'
    return template_name + 'index-login.html'


def fix_data(data):
    for key in data:
        key = key.encode('utf-8')
        value = data[key].encode('utf-8')
        data[key] = value
    return data


def save_lugar(request):
    stream = StringIO(request.body)
    data = JSONParser().parse(stream)
    print data.pop('telefono')
    lugar_serializer = LugarSerializer(data=data)
    # lugar = Lugar(nombre='nombre',ciudad='q',seccion='1',numero_1=12,numero_2=11,numero_3=12,descripcion='ded',usuario=1)
    # lugar = Lugar(ciudad='qq',seccion='1',numero_1=12,numero_2=11,numero_3=12)
    print 'succes load serializer'
    try:
        
        print lugar_serializer.errors
        lugar_serializer.save()
        
        return True
    except ValidationError:
        print 'error'
    return False
    