from django.conf.urls import url, include
from rest_framework import routers

from usuarios import views


routers = routers.DefaultRouter()
routers.register(r'usuarios', views.UsuarioViewSet)


usuariospatterns = [
	url(r'^solicitante/$', views.HomeView.as_view()),
	url(r'^codificador/$', views.HomeView2.as_view()),
	url(r'^comprador/$', views.HomeView3.as_view()),
	url(r'^aprobador-de-solicitudes$', views.HomeView4.as_view()),
	url(r'^', include(routers.urls)),
]