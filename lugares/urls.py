from django.conf.urls import url, include
from rest_framework import routers
from lugares import views


routers = routers.DefaultRouter()
routers.register(r'lugares', views.LugarViewSet)


lugarespatterns = [
	url(r'^', include(routers.urls)),
]