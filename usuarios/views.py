from django.http import HttpResponse
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
    template_name = 'usuarios/'

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
        return HttpResponse(status=300)

def get_template(request,template_name):
    if request.usuario.is_authenticated():
        if request.user.tipo == '3':
            return template_name + 'index-solicitante'
#        if request.user.tipo == '6':
#            return template_name + 'index-comprador'
    else:
        return template_name + 'index-login.html'