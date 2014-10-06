from django.contrib import admin

from .models import Producto
from .models import NombresxProducto
from .models import FotosxProducto
from .models import PrecioxProducto

admin.site.register(Producto)
admin.site.register(NombresxProducto)
admin.site.register(FotosxProducto)
admin.site.register(PrecioxProducto)