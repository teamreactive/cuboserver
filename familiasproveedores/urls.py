from django.conf.urls import url, include
from rest_framework import routers
from familiasproveedores import views


routers = routers.DefaultRouter()
routers.register(r'familiasproveedores', views.FamiliaProveedorViewSet)


familiasproveedorespatterns = [
	url(r'^', include(routers.urls)),
]