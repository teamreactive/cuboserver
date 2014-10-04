from django.contrib import admin

from .models import Usuario
from .models import ConsolidadorxSolicitante
from .models import SolicitantexCodificador
from .models import AprobadorSolicitudesxSolicitante
from .models import AprobadorSolicitudesxComprador
from .models import CompradorxAprobadorCompras
from .models import AprobadorCompraxAlmacenista


admin.site.register(Usuario)
admin.site.register(ConsolidadorxSolicitante)
admin.site.register(SolicitantexCodificador)
admin.site.register(AprobadorSolicitudesxSolicitante)
admin.site.register(AprobadorSolicitudesxComprador)
admin.site.register(CompradorxAprobadorCompras)
admin.site.register(AprobadorCompraxAlmacenista)