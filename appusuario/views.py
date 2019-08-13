from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class LoginUserView(TemplateView):
    template_name = 'appusuario/login.html'