from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cubo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'usuarios.views.index', name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^inicio_solicitante/$', 'solicitantes.views.inicio_solicitante', name='inicio_solicitante'),
    url(r'^inicio_comprador/$', 'comprador.views.inicio_comprador', name='inicio_comprador')
    url(r'^logout/', 'usuarios.views.logout', name='logout')
)
