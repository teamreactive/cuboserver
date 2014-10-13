from django.conf.urls import url, include
from rest_framework import routers

from usuarios import views


routers = routers.DefaultRouter()
routers.register(r'usuarios', views.UsuarioViewSet)


usuariospatterns = [
	url(r'^', include(routers.urls)),
]