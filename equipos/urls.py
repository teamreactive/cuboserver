from django.conf.urls import url, include
from rest_framework import routers
from equipos import views


routers = routers.DefaultRouter()
routers.register(r'equipos', views.EquipoViewSet)


equipospatterns = [
	url(r'^', include(routers.urls)),
]