from django.shortcuts import render, redirect

from lugares.forms import LugarForm
from productos.forms import ProductoForm
from solicitudes.forms import SolicitudForm
from usuarios.views import get_usuario


def inicio_solicitante(request):
    usuario = get_usuario(request)
    if usuario and usuario.tipo == '3':
        solicitud_form = SolicitudForm()
        lugar_form = LugarForm()
        producto_form = ProductoForm()
        if request.method == 'POST':
            if solicitud_form.is_valid():
                solicitud_form.save()
                return redirect('/inicio_solicitante/')
            else:
                solicitud_form = SolicitudForm(solicitud_form.cleaned_data)
                params = {
                    'usuario': usuario,
                    'solicitud_form': solicitud_form,
                    'lugar_form': lugar_form,
                    'producto_form': producto_form,
                }
        else:
            params = {
                'usuario': usuario,
                'solicitud_form': solicitud_form,
                'lugar_form': lugar_form,
                'producto_form': producto_form,
            }
            return render(request, 'solicitantes/inicio_solicitante.html', params)
    else:
        request.session.flush()
        return redirect('/')