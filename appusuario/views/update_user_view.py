from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

from appusuario.models import ComplementoUser


class UserUpdateView(UpdateView):
    model = ComplementoUser
    template_name = "appusuario/user_form.html"
    fields = [
        'username',
        'email',
        'first_name'
    ]
    success_url = reverse_lazy("appproduto:list_produto_view")