from django.conf.urls.defaults import *
from tastypie.api import Api
from .api import *

v1_api = Api(api_name='v1')
v1_api.register(ProductoResource())
v1_api.register(NombreProductoResource())
v1_api.register(FotoProductoResource())
v1_api.register(PrecioProductoResource())
v1_api.register(PrecioMesProductoResource())

urlpatterns = patterns('',
    (r'^api/', include(v1_api.urls)),
)