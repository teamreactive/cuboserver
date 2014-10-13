from django.conf.urls import url, include
from rest_framework import routers
from productos import views


routers = routers.DefaultRouter()
routers.register(r'productos', views.ProductoViewSet)


productospatterns = [
	url(r'^', include(routers.urls)),
]