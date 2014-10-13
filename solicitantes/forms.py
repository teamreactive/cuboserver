from django.forms import ModelForm
from .models import Producto, FotosxProducto


class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = (
            'estado',
            'lugar_entrega',
            'fecha_requerida',
            'solicitante',
            'centro_de_costo',
            'equipo',
            'proyecto',
            'productos',
        )