from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from appusuario.forms import UserForm


class UserCreateView(CreateView):
    template_name = "appusuario/user_create_form.html"
    model = User
    form_class = UserForm
    # success_url = reverse_lazy("appbase:home")

    def form_valid(self, form):
        if  form.is_valid():
            form.save()
            return redirect('appbase:home')
