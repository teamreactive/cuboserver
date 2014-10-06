from django.shortcuts import render

from cubo.settings import SECRET_KEY
import hashlib
from .models import Usuario


def index(request):
    return render(request, 'index.html')

def get_usuario(request):
    nombre = request.session.get('nombre')
    nombre_check = request.session.get('nombre_check')
    cliente = request.session.get('cliente')
    cliente_check = request.session.get('cliente_check')
    if encriptar(nombre) == nombre_check and cliente == cliente_check:
        try:
            return Usuario.objects.get(nombre=nombre, cliente=cliente)
        except Usuario.DoesNotExist:
            return None
    else:
        return None

def encriptar(valor):
    if SECRET_KEY and valor:
        return hashlib.sha512(SECRET_KEY + valor).hexdigest()
    else:
        return None