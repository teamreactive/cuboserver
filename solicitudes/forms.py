from django.forms import ModelForm
from .models import Solicitud


class SolicitudForm(ModelForm):
    class Meta:
        model = Solicitud
        fields = [
            'estado', 'lugar_entrega', 'fecha_requerida',
            'solicitante', 'consolidador', 'aprobador',
            'centro_de_costo', 'equipo', 'emergencia', 'proyecto'
        ]