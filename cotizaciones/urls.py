from django.conf.urls.defaults import *
from tastypie.api import Api
from .api import CotizacionResource

v1_api = Api(api_name='v1')
v1_api.register(CotizacionResource())

urlpatterns = patterns('',
    (r'^api/', include(v1_api.urls)),
)