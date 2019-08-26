from django.shortcuts import redirect
from django.shortcuts import render
from django.views.generic import CreateView

from appusuario.forms import UserForm
from appusuario.models import ComplementoUser


class UserCreateView(CreateView):
    template_name = "appusuario/user_form.html"
    model = ComplementoUser
    form_class = UserForm
    # success_url = reverse_lazy("appbase:home")

    def form_valid(self, form):
        if form.is_valid():
            form.save()
            return redirect('appproduto:produto_list_view')
        return render(self.template_name, {'form': form})

