from django.shortcuts import render
from .forms import LugarForm
from .models import Lugar
from rest_framework import viewsets
from .serializers import LugarSerializer


class LugarViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows solicitudes to be viewed or edited.
    """
    queryset = Lugar.objects.all()
    serializer_class = LugarSerializer


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