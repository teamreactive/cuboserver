from django.shortcuts import render

from .forms import LugarForm


def crear_lugar(request):
    if request.method == 'POST':
    	form = LugarForm(request.POST)
        if form.is_valid():
        	form.save()
        	return redirect('/')
        else:
        	form = LugarForm(form.cleaned_data)
        	params = { 'form': form }
        	return render(request, 'crear_lugar.html', params)
    else:
    	form = LugarForm()
    	params = { 'form': form }
        return render(request, 'crear_lugar.html', params)