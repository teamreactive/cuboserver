from django.conf.urls.defaults import *
from tastypie.api import Api
from .api import *

v1_api = Api(api_name='v1')
v1_api.register(ProveedorResource())
v1_api.register(ContactoProveedorResource())

urlpatterns = patterns('',
    (r'^api/', include(v1_api.urls)),
)