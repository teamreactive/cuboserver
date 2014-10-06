from django.forms import ModelForm
from .models import Solicitud

from django.forms.widgets import Select, DateTimeInput, TextInput, SelectMultiple
from lugares.models import Lugar


class SolicitudForm(ModelForm):
    class Meta:
        model = Solicitud
        fields = [
            'lugar_entrega',
            'fecha_requerida',
            'centro_de_costo',
            'equipo',
            'proyecto',
            'productos',
        ]
        widgets = {
            'lugar_entrega': Select(attrs={'class': 'form-control', 'placeholder': 'Lugar de entrega'}),
            'fecha_requerida': DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Fecha requerida'}),
            'centro_de_costo': Select(attrs={'class': 'form-control', 'placeholder': 'Centro de costosos'}),
            'equipo': Select(attrs={'class': 'form-control', 'placeholder': 'Equipo'}),
            'proyecto': TextInput(attrs={'class': 'form-control', 'placeholder': 'Proyecto'}),
            'productos': SelectMultiple(attrs={'class': 'form-control', 'placeholder': 'Producto/s'}),
        }