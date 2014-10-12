from django.shortcuts import render, redirect
from usuarios.views import get_usuarios


def inicio_comprador(request):
    usuario = get_usuario(request)
    if usuario and usuario.tipo == '6':
        pass
    else:
        return redirect('/')


# Create your views here.
