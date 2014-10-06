from django.forms import ModelForm
from .models import Producto, FotosxProducto


class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = [
            'codigo_onu',
            'nombre',
            'descripcion',
            'referencia',
            'marca',
            'servicio',
            'familia_proveedor',
        ]

class FotosxProductoForm(ModelForm):
    class Meta:
        model = FotosxProducto
        fields = [
            'foto',
        ]