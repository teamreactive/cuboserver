from django.shortcuts import render

from .forms import SolicitudForm


def crear_solicitud(request):
    if request.method == 'POST':
    	form = SolicitudForm(request.POST)
        fecha_requerida = request.POST.get('fecha_requerida')
        form.fecha_requerida = fecha_requerida
        if form.is_valid():
        	form.save()
        	return redirect('/')
        else:
        	form = SolicitudForm(form.cleaned_data)
        	params = { 'form': form, 'fecha_requerida': fecha_requerida }
        	return render(request, 'crear_solicitud.html', params)
    else:
    	form = SolicitudForm()
    	params = { 'form': form }
        return render(request, 'crear_solicitud.html', params)