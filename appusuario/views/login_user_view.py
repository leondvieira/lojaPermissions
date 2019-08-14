from django.contrib.auth.views import LoginView
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import TemplateView


class LoginUserView(LoginView):
    template_name = 'appusuario/login_user_form.html'
