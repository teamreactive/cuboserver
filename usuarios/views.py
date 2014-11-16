from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from django.contrib.auth.hashers import check_password


import json
from lugares.models import *
from .models import *
from hashlib import * 


class HomeView(View):
	template_name = ""

	def get(self, request, *args, **kwargs):
		return render(request, self.template_name)


class TestView(View):
	template_name = "usuarios/test.html"

	def get(self, request, *args, **kwargs):
		return render(request, self.template_name)

class UserLoginView(View):
	template_name = "usuarios/user-login.html"

	def post(self, request, *args, **kwargs):
		username = request.POST['username']
		password = request.POST['password']
		usuario = Usuario.objects.filter(nombre=username)
		if usuario:
			usuario = usuario[0]
			password = md5(password).hexdigest()
			if usuario.password == password:				
				if usuario.tipo == '1':
					return render(request,'usuarios/admin-general.html',{})
				if usuario.tipo == '2':
					return HttpResponse('Not Created')
				if usuario.tipo == '3':
					return render(request,'usuarios/solicitante.html',{})
				if usuario.tipo == '4':
					return render(request,'usuarios/solicitante.html',{})
				if usuario.tipo == '5':
					return render(request,'usuarios/aprobadorsolicitudes.html',{})
				if usuario.tipo == '6':
					return render(request,'usuarios/comprador.html',{})
				if usuario.tipo == '7':
					return render(request,'usuarios/aprobadorcompras.html',{})
				if usuario.tipo == '8':
					return render(request,'usuarios/almacenista.html',{})
			
		else:
			return render(request, self.template_name)
		return render(request,self.template_name,{})

	def get(self, request, *args, **kwargs):
		return render(request, self.template_name)

	
def user_login(request):
		if request.method == 'POST':
			username = request['username']
			password = request['password']
			usuario = usuario.objects.filter(nombre=username)
			return render('usuarios/test.html')
