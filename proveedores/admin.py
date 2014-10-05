from django.contrib import admin

from .models import Proveedor
from .models import ContactosxProveedor

admin.site.register(Proveedor)
admin.site.register(ContactosxProveedor)