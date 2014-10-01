from django.contrib import admin

from .models import Producto,
                    NombresxProducto,
                    FotosxProducto,
                    PrecioxProducto,
                    ProductoxContactoQueNoVende,
                    ProductoxContactoQueVende

admin.site.register(Producto)
admin.site.register(NombresxProducto)
admin.site.register(FotosxProducto)
admin.site.register(PrecioxProducto)
admin.site.register(ProductoxContactoQueNoVende)
admin.site.register(ProductoxContactoQueVende)