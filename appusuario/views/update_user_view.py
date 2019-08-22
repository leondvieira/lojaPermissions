
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from django.contrib.auth import get_user_model
User = get_user_model()

class UserUpdateView(UpdateView):
    model = User
    template_name = "appusuario/user_form.html"
    fields = [
        'username',
        'password',
        'email'
    ]
    success_url = reverse_lazy("appbase:home")