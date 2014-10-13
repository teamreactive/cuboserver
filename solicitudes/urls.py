from django.conf.urls import url, include
from rest_framework import routers
from solicitudes import views


routers = routers.DefaultRouter()
routers.register(r'solicitudes', views.SolicitudViewSet)


solicitudespatterns = [
	url(r'^', include(routers.urls)),
]