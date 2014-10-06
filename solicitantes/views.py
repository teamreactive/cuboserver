from django.shortcuts import render, redirect

from django.db.models import Q
from lugares.forms import LugarForm
from productos.forms import ProductoForm, FotosxProductoForm
from solicitudes.forms import SolicitudForm
from solicitudes.models import Solicitud
from usuarios.models import Usuario
from usuarios.views import get_usuario


def inicio_solicitante(request):
    usuario = get_usuario(request)
    if usuario and usuario.tipo == '3':
        solicitudes = Solicitud.objects.filter(Q(consolidador=usuario) | Q(solicitante=usuario))
        solicitud_form = SolicitudForm()
        lugar_form = LugarForm()
        producto_form = ProductoForm()
        params = {
            'usuario': usuario,
            'solicitud_form': solicitud_form,
            'lugar_form': lugar_form,
            'producto_form': producto_form,
            'solicitudes': solicitudes,
        }
        if request.method == 'POST':
            solicitud_submit = request.POST.get('solicitud')
            lugar_submit = request.POST.get('lugar')
            producto_submit = request.POST.get('producto')
            if solicitud_submit and not lugar_submit and not producto_submit:
                solicitud_form = SolicitudForm(request.POST)
                if solicitud_form.is_valid():
                    try:
                        solicitud = solicitud_form.save(commit=False)
                        solicitud.estado = '1' if len(Usuario.objects.filter(tipo='5')) > 0 else '3'
                        if solicitud.consolidador:
                            solicitud.consolidador = usuario
                            solicitud.solicitante = solicitud.consolidador
                        else:
                            solicitud.solicitante = usuario
                        solicitud.save()
                        return redirect('/inicio_solicitante/')
                    except:
                        params['solicitud_form'] = solicitud_form
                        pass
                else:
                    params['solicitud_form'] = solicitud_form
            elif not solicitud_submit and lugar_submit and not producto_submit:
                lugar_form = LugarForm(request.POST)
                if lugar_form.is_valid():
                    try:
                        lugar = lugar_form.save(commit=False)
                        lugar.usuario = usuario
                        lugar.save()
                        return redirect('/inicio_solicitante/')
                    except:
                        params['lugar_form'] = lugar_form
                        pass
                else:
                    params['lugar_form'] = lugar_form
            elif not solicitud_submit and not lugar_submit and producto_submit:
                producto_form = ProductoForm(request.POST)
                if producto_form.is_valid():
                    try:
                        producto = producto_form.save(commit=False)
                        producto.cliente = usuario.cliente
                        producto.save()
                        return redirect('/inicio_solicitante/')
                    except:
                        params['producto_form'] = producto_form
                        pass
                else:
                    params['producto_form'] = producto_form
        return render(request, 'solicitantes/inicio_solicitante.html', params)
    else:
        return redirect('/')