from django.contrib import admin

from .models import Producto
from .models import NombresxProducto
from .models import FotosxProducto
from .models import PrecioxProducto
from .models import ProductoxContactoQueNoVende
from .models import ProductoxContactoQueVende

admin.site.register(Producto)
admin.site.register(NombresxProducto)
admin.site.register(FotosxProducto)
admin.site.register(PrecioxProducto)
admin.site.register(ProductoxContactoQueNoVende)
admin.site.register(ProductoxContactoQueVende)