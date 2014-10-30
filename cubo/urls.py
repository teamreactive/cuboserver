from django.conf.urls import patterns, include, url
from django.contrib import admin

from centrosdecostos.urls import centrosdecostospatterns
from clientes.urls import clientespatterns
from compras.urls import compraspatterns
from contactos.urls import contactospatterns
from cotizaciones.urls import cotizacionespatterns
from equipos.urls import equipospatterns
from familiasproveedores.urls import familiasproveedorespatterns
from historiales.urls import historialespatterns
from lugares.urls import lugarespatterns
from productos.urls import productospatterns
from proveedores.urls import proveedorespatterns
from solicitudes.urls import solicitudespatterns
from tiposdeequipos.urls import tiposdeequipospatterns
from usuarios.urls import usuariospatterns


urlpatterns = patterns('',
    url(r'^admin/$', include(admin.site.urls)),
)

urlpatterns += centrosdecostospatterns
urlpatterns += clientespatterns
urlpatterns += compraspatterns
urlpatterns += contactospatterns
urlpatterns += cotizacionespatterns
urlpatterns += equipospatterns
urlpatterns += familiasproveedorespatterns
urlpatterns += historialespatterns
urlpatterns += lugarespatterns
urlpatterns += productospatterns
urlpatterns += proveedorespatterns
urlpatterns += solicitudespatterns
urlpatterns += tiposdeequipospatterns
urlpatterns += usuariospatterns