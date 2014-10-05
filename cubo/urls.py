from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cubo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^crear_solicitud/$', 'solicitudes.views.crear_solicitud', name='crear_solicitud'),
    url(r'^crear_producto/$', 'productos.views.crear_producto', name='crear_producto'),
    url(r'^crear_lugar/$', 'lugares.views.crear_lugar', name='crear_lugar'),
)
