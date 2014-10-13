from django.conf.urls import url, include
from rest_framework import routers
from tiposdeequipos import views


routers = routers.DefaultRouter()
routers.register(r'tiposdeequipos', views.TipoDeEquipoViewSet)


tiposdeequipospatterns = [
	url(r'^', include(routers.urls)),
]