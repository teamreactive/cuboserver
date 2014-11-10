from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View
from StringIO import StringIO

import json
from .models import Usuario
from lugares.models import Lugar

from django.core.exceptions import ValidationError


class HomeView(View):
    template_name = ""

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)