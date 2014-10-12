from django.shortcuts import render, redirect
from usuarios.views import get_usuarios

from proveedor.models import Proveedor
from familiasproveedores import FamiliaProveedor

from proveedor.forms import  CrearProveedorForm
from proveedor.forms import  CrearFamiliasProveedorForm

def inicio_comprador(request):
    usuario = get_usuario(request)

    if usuario and usuario.tipo == '6':
        crear_proveedor_form = CrearProveedorForm()
        crear_fp_form = CrearFamiliasProveedorForm()
        update_proveedor = CrearProveedorForm()
        update_fp = CrearFamiliasProveedorForm()
        params = {
            'usuario':usuario,
            'crear_proveedor_form':crear_proveedor_form,
            'crear_fp_form':crear_fp_form,
            'update_proveedor':update_proveedor,
            'update_fp':update_fp,
        }
        if request.method == 'POST':
            proveedor_submit = request.POST.get('proveedor')
            update_proveedor = request.POST.get('update_proveedor')
            update_fp = request.POST.get('update_fp')
            fp_submit = request.POST.get('familiaproveedor')
            if proveedor_submit:
                crear_proveedor_form = CrearProveedorForm(request.POST)
                if crear_proveedor_form.is_valid():
                    try:
                        crear_proveedor_form.save()
                        return redirect('/inicio_comprador/')
                    except:
                        params['crear_proveedor_form'] = crear_proveedor_form
                        pass
            else if update_proveedor:
                try:
                    proveedor = Proveedor.objects.filter(razon_social=update_proveedor.razon_social)
                    if proveedor:
                        update_proveedor(update_proveedor,proveedor)
                    return redirect('/inicio_comprador/')
            else if crear_fp_form:
                crear_fp_form = CrearFamiliasProveedorForm(request.POST)
                if crear_fp_form.is_valid():
                    try:
                        crear_fp_form.save()
                        return redirect('/inicio_comprador/')
                    except:
                        params['crear_fp_form'] = crear_proveedor_form
                        pass
            else if update_fp:
                try:
                    familiaproveedor = FamiliaProveedor.objects.filter(nombre=update_fp.nombre)
                    if familiaproveedor:
                        update_fp(update_fp,familiaproveedor)
                    return redirect('/inicio_comprador/')
        return render(request,'',params)
    else:
        return redirect('/')

def update_proveedor(update_proveedor,proveedor):
    if update_proveedor.razon_social:
        proveedor.razon_social = update_proveedor.razon_social
    if update_proveedor.sigla:
        proveedor.sigla = update_proveedor.sigla
    if update_proveedor.nit:
        proveedor.nit = update_proveedor.nit
    if update_proveedor.numero_verificacion:
        proveedor.numero_verificacion = update_proveedor.numero_verificacion
    if update_proveedor.lugar:
        proveedor.lugar = update_proveedor.lugar
    if update_proveedor.logo:
        proveedor.logo = update_proveedor.logo

def update_fp(update_fp,familiaproveedor):
    if update_fp.nombre:
        familiaproveedor.nombre = update_fp.nombre
    if update_fp.descripcion:
        familiaproveedor.descripcion = update_fp.descripcion
# Create your views here.
