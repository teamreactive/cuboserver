from django.froms import ModelForm
from .models import FamiliaProveedor

from django.forms.widgets import TextInput

class CrearFamiliaProveedorForm(ModelForm):
    class Meta:
        model = FamiliaProveedor
        fields = [
            'nombre',
            #'descripcion',
        ]
        widgets = {
            'nombre': TextInput(attr={'class':'form-control','placeholder':'Nombre'}),
            #'descripcion': TextInput(attr={'class':'form-control','placeholder':'Descripcion'})
        }
