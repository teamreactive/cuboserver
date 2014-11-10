from django.contrib import admin

from .models import *


admin.site.register(Usuario)
admin.site.register(ConsolidadorSolicitante)
admin.site.register(SolicitanteCodificador)
admin.site.register(AprobadorSolicitudesSolicitante)
admin.site.register(AprobadorSolicitudesComprador)
admin.site.register(CompradorAprobadorCompras)
admin.site.register(AprobadorComprasAlmacenista)