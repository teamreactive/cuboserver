from django.shortcuts import render

from .forms import ProductoForm


def crear_producto(request):
    if request.method == 'POST':
    	form = ProductoForm(request.POST)
        if form.is_valid():
        	form.save()
        	return redirect('/')
        else:
        	form = ProductoForm(form.cleaned_data)
        	params = { 'form': form }
        	return render(request, 'crear_producto.html', params)
    else:
    	form = ProductoForm()
    	params = { 'form': form }
        return render(request, 'crear_producto.html', params)