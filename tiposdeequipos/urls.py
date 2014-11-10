from django.conf.urls.defaults import *
from tastypie.api import Api
from .api import TipoEquipoResource

v1_api = Api(api_name='v1')
v1_api.register(TipoEquipoResource())

urlpatterns = patterns('',
    (r'^api/', include(v1_api.urls)),
)