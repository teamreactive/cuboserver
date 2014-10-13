from django.conf.urls import url, include
from rest_framework import routers
from centrosdecostos import views


routers = routers.DefaultRouter()
routers.register(r'centrosdecostos', views.CentroDeCostoViewSet)


centrosdecostospatterns = [
	url(r'^', include(routers.urls)),
]