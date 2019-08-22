from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

from django.contrib.auth.models import User

class UserUpdateView(UpdateView):
    model = User
    template_name = "appusuario/user_form.html"
    fields = [
        'username',
        'password',
        'email'
    ]
    success_url = reverse_lazy("appbase:home")