from django.conf.urls import url, include
from rest_framework import routers
from cotizaciones import views


routers = routers.DefaultRouter()
routers.register(r'cotizaciones', views.CotizacionViewSet)


cotizacionespatterns = [
	url(r'^', include(routers.urls)),
]