from django.shortcuts import render

from .forms import SolicitudForm


def crear_solicitud(request):
    if request.method == 'POST':
    	form = SolicitudForm(request.POST)
        if form.is_valid():
        	form.save()
        	return redirect('/')
        else:
        	form = SolicitudForm(form.cleaned_data)
        	params = { 'form': form }
        	return render(request, 'crear_solicitud.html', params)
    else:
    	form = SolicitudForm()
    	params = { 'form': form }
        return render(request, 'crear_solicitud.html', params)