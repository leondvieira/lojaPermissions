from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.shortcuts import render
from django.views.generic import CreateView

from appusuario.forms import UserForm

User = get_user_model()

class UserCreateView(CreateView):
    template_name = "appusuario/user_form.html"
    model = User
    form_class = UserForm
    # success_url = reverse_lazy("appbase:home")

    def form_valid(self, form):
        if form.is_valid():
            form.save()
            return redirect('appproduto:produto_list_view')
        return render(self.template_name, {'form': form})

