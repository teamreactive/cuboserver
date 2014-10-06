from django.shortcuts import render, redirect

from cubo.settings import SECRET_KEY
import hashlib
from .models import Usuario


def index(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        contrasena = request.POST.get('contrasena')
        try:
            Usuario.objects.get(nombre=nombre, contrasena=encriptar(contrasena))
            request.session['nombre'] = nombre
            request.session['nombre_check'] = encriptar(nombre)
            return redirect('/inicio_solicitante/')
        except Usuario.DoesNotExist:
            params = {
                'nombre': nombre,
                'contrasena': contrasena,
                'mensaje': 'Error al ingresar, verifica tus datos e intenta nuevamente.'
            }
            return render(request, 'usuarios/index.html', params)
    else:
        usuario = get_usuario(request)
        if usuario:
            if usuario.tipo == '1': pass
            elif usuario.tipo == '2': pass
            elif usuario.tipo == '3': return redirect('/inicio_solicitante/')
            elif usuario.tipo == '4': pass
            elif usuario.tipo == '5': pass
            elif usuario.tipo == '6': pass
            elif usuario.tipo == '7': pass
            elif usuario.tipo == '8': pass
            else: request.session.flush()
        return render(request, 'usuarios/index.html')

def get_usuario(request):
    nombre = request.session.get('nombre')
    nombre_check = request.session.get('nombre_check')
    if encriptar(nombre) == nombre_check:
        try:
            return Usuario.objects.get(nombre=nombre)
        except Usuario.DoesNotExist:
            return None
    else:
        return None

def encriptar(valor):
    if SECRET_KEY and valor:
        return hashlib.sha512(SECRET_KEY + valor).hexdigest()
    else:
        return None

def logout(request):
    request.session.flush()
    return redirect('/')