from django.conf.urls import url, include
from rest_framework import routers
from contactos import views


routers = routers.DefaultRouter()
routers.register(r'contactos', views.ContactoViewSet)


contactospatterns = [
	url(r'^', include(routers.urls)),
]