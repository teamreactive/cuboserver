from django.conf.urls import url, include
from rest_framework import routers
from historiales import views


routers = routers.DefaultRouter()
routers.register(r'historiales', views.HistorialViewSet)


historialespatterns = [
	url(r'^', include(routers.urls)),
]