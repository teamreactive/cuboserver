from django.forms import ModelForm
from .models import Producto


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
            'equipo',
            'centro_de_costo',
        ]