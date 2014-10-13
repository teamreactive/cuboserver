from django.conf.urls import url, include
from rest_framework import routers
from compras import views


routers = routers.DefaultRouter()
routers.register(r'compras', views.CompraViewSet)


compraspatterns = [
	url(r'^', include(routers.urls)),
]