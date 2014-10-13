from django.forms import ModelForm
from .models import Solicitud

from django.forms.widgets import Select, DateTimeInput, TextInput, SelectMultiple, HiddenInput
from lugares.models import Lugar


class SolicitudForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(SolicitudForm, self).__init__(*args, **kwargs)
        self.fields['consolidador'].label = "Solicitante"
        self.fields['consolidador'].required = False

    class Meta:
        model = Solicitud
        fields = [
            'lugar_entrega',
            'fecha_requerida',
            'centro_de_costo',
            'equipo',
            'proyecto',
            'productos',
            'consolidador',
        ]
        widgets = {
            'lugar_entrega': Select(attrs={'class': 'form-control', 'required': 'required'}),
            'fecha_requerida': DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Fecha requerida'}),
            'centro_de_costo': Select(attrs={'class': 'form-control'}),
            'equipo': Select(attrs={'class': 'form-control'}),
            'proyecto': TextInput(attrs={'class': 'form-control', 'placeholder': 'Proyecto'}),
            'productos': SelectMultiple(attrs={'class': 'form-control'}),
            'consolidador': Select(attrs={'class': 'form-control', 'placeholder': 'consolidador'})
        }