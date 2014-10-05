from django.forms import ModelForm
from .models import Lugar


class LugarForm(ModelForm):
    class Meta:
        model = Lugar
        fields = [
            'nombre', 'seccion', 'numero_seccion',
            'numero_1', 'numero_2', 'user'
        ]