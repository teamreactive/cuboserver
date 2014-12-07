from django.core.mail import send_mail
from django.http import HttpResponse
from django.views.generic import View

import django
from django.conf import settings
from django.core.mail import send_mail

from .models import *
import json
import hashlib
import random
import string

class MailView(View):

	def post(self, request, *args, **kwargs):
		data = json.loads(request.body)
		user = data.get("user")
		mail = data.get("mail")
		target = Usuario.objects.get(nombre=user)
		if not mail or not user or not target: return HttpResponse(status=400)
		if mail != target.contacto.email: return HttpResponse(status=403)
		subject = "Olvido de contrasena"
		message = ("Este es un mensaje enviado para la recuperacion de\n" +
		"tu contrasena olvidada, si crees que esto fue un error, \n" +
		"ignora este mensaje, de lo contrario, sigue leyendo:\n\n")
		
		newpass = ""
		for i in range(10): newpass += random.choice(string.ascii_uppercase + string.digits)
		target.password = hashlib.sha512(newpass).hexdigest()
		target.password = hashlib.sha512(target.password).hexdigest()
		target.save()
		message += ("Se te ha asignado una contrasena nueva,\n"+
				"el valor de la misma es:\n")
		message += newpass + "\n"
		message += "Nombre de usuario: " + user

		fmail = mail
		tmail = "jcbages@outlook.com"
		send_mail(subject, message,	fmail, [tmail], fail_silently=False)
		return HttpResponse(status=200)


	def options(self, request):
		return response(status=200)