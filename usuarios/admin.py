from django.contrib import admin

from .models import Usuario,
                    ConsolidadorxSolicitante,
                    SolicitantexCodificador,
                    AprobadorSolicitudesxSolicitante,
                    AprobadorSolicitudesxComprador,
                    CompradorxAprobadorCompras,
                    AprobadorCompraxAlmacenista


admin.site.register(Usuario)
admin.site.register(ConsolidadorxSolicitante)
admin.site.register(SolicitantexCodificador)
admin.site.register(AprobadorSolicitudesxSolicitante)
admin.site.register(AprobadorSolicitudesxComprador)
admin.site.register(CompradorxAprobadorCompras)
admin.site.register(AprobadorCompraxAlmacenista)