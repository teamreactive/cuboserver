from django.froms import ModelForm
from .models import Proveedor

from django.forms.widgets import TextInput, Select, FileInput

class CrearProveedorForm(ModelForm):
    class Meta:
        model = Proveedor
        fields = [
            'razon_social',
            'sigla',
            'nit',
            'numero_verificacion',
            'lugar',
            'logo',
        ]
        widgets = {
            'razon_social': TextInput(attr={'class':'form-control','placeholder':'Razon Social'}),
            'sigla': TextInput(attr={'class':'form-control','placeholder':'Sigla'}),
            'nit':TextInput(attr={'class':'form-control','placeholder':'NIT')},
            'numero_verificacion':TextInput(attr={'class':'form-control','placeholder':'Numero de Verificacion'}),
            'lugar':Select(attr={'class':'form-control','placeholder':'Lugar'}),
            'logo': FileInput(attr={'class':'form-control','placeholder':'Logo'}),
        }