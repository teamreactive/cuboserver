from django.conf.urls import url, include
from rest_framework import routers
from proveedores import views


routers = routers.DefaultRouter()
routers.register(r'proveedores', views.ProveedorViewSet)


proveedorespatterns = [
	url(r'^', include(routers.urls)),
]