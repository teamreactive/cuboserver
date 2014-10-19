from django.forms import ModelForm

from .models import Lugar


class LugarForm(ModelForm):
    class Meta:
        model = Lugar
        fields = [
            'nombre',
            'descripcion',
            'contactos',
        ]