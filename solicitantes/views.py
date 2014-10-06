from django.shortcuts import render, redirect

from lugares.forms import LugarForm
from productos.forms import ProductoForm, FotosxProductoForm
from solicitudes.forms import SolicitudForm
from solicitudes.models import Solicitud
from usuarios.models import Usuario
from usuarios.views import get_usuario


def inicio_solicitante(request):
    usuario = get_usuario(request)
    if usuario and usuario.tipo == '3':
        solicitudes = Solicitud.objects.filter(solicitante=usuario)
        if request.method == 'POST':
            solicitud_form = SolicitudForm(request.POST)
            lugar_form = LugarForm()
            producto_form = ProductoForm()
            fotosxproducto_form = FotosxProductoForm()
            if solicitud_form.is_valid():
                solicitud = solicitud_form.save(commit=False)
                solicitud.estado = '1' if len(Usuario.objects.filter(tipo='5')) > 0 else '3'
                solicitud.solicitante = usuario
                solicitud.save()
                return redirect('/inicio_solicitante/')
            else:
                params = {
                    'usuario': usuario,
                    'solicitud_form': solicitud_form,
                    'lugar_form': lugar_form,
                    'producto_form': producto_form,
                    'fotosxproducto_form': fotosxproducto_form,
                    'solicitudes': solicitudes,
                }
                return render(request, 'solicitantes/inicio_solicitante.html', params)
        else:
            solicitud_form = SolicitudForm()
            lugar_form = LugarForm()
            producto_form = ProductoForm()
            fotosxproducto_form = FotosxProductoForm()
            params = {
                'usuario': usuario,
                'solicitud_form': solicitud_form,
                'lugar_form': lugar_form,
                'producto_form': producto_form,
                'fotosxproducto_form': fotosxproducto_form,
                'solicitudes': solicitudes,
            }
            return render(request, 'solicitantes/inicio_solicitante.html', params)
    else:
        request.session.flush()
        return redirect('/')