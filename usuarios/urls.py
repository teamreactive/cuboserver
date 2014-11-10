from django.conf.urls.defaults import *
from tastypie.api import Api
from .api import *
from .views import *


v1_api = Api(api_name='v1')
v1_api.register(UsuarioResource())
v1_api.register(ConsolidadorSolicitanteResource())
v1_api.register(SolicitanteCodificadorResource())
v1_api.register(AprobadorSolicitudesSolicitanteResource())
v1_api.register(AprobadorSolicitudesCompradorResource())
v1_api.register(CompradorAprobadorComprasResource())
v1_api.register(AprobadorComprasAlmacenistaResource())


urlpatterns = patterns('',
    (r'^api/', include(v1_api.urls)),
    (r'^solicitante/$', views.HomeView.as_view()),
    (r'^codificador/$', views.HomeView2.as_view()),
    (r'^comprador/$', views.HomeView3.as_view()),
    (r'^aprobador-de-solicitudes$', views.HomeView4.as_view()),
    (r'^aprobador-de-compra$', views.HomeView5.as_view())
)