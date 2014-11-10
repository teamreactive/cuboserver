from django.shortcuts import render
from django.views.generic import View

import json
from lugares.models import *
from .models import *


class HomeView(View):
	template_name = ""

	def get(self, request, *args, **kwargs):
		return render(request, self.template_name)