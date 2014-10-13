from django.conf.urls import url, include
from rest_framework import routers
from clientes import views


routers = routers.DefaultRouter()
routers.register(r'clientes', views.ClienteViewSet)


clientespatterns = [
	url(r'^', include(routers.urls)),
]