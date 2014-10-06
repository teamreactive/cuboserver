from django.forms import ModelForm
from .models import Solicitud


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