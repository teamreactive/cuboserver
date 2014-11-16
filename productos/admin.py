from django.contrib import admin

from .models import *


admin.site.register(Producto)
admin.site.register(NombreProducto)
admin.site.register(FotoProducto)
admin.site.register(UnidadProducto)
admin.site.register(PrecioMesProducto)