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
    # Examples:
    # url(r'^$', 'cubo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'usuarios.views.index', name='index'),
    url(r'^admin/$', include(admin.site.urls)),
    url(r'^inicio_solicitante/$', 'solicitantes.views.inicio_solicitante', name='inicio_solicitante'),
    #url(r'^inicio_comprador/$', 'comprador.views.inicio_comprador', name='inicio_comprador'),
    url(r'^logout/$', 'usuarios.views.logout', name='logout'),
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