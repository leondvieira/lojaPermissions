from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView

from appusuario.forms.user_create_form import UserForm


class UserCreateView(CreateView):
    template_name = "appusuario/user_create_form.html"
    model = User
    form_class = UserForm
    success_url = reverse_lazy("appbase:home")