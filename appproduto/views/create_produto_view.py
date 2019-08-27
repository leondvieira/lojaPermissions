from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import redirect
from django.shortcuts import render


# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from appproduto.forms.create_produto_form import ProdutoForm
from appproduto.models.produto import Produto
from appproduto.views.core.CoreMixinDispatch import CoreMixinDispatch


class ProdutoCreateView(CreateView, PermissionRequiredMixin):
    template_name = "appproduto/produto_create_form.html"
    model = Produto

    def get(self, request):
        form = ProdutoForm

        if not request.user.is_authenticated:
            return redirect('appproduto:produto_list_view')
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ProdutoForm(request.POST, request.FILES)

        if form.is_valid():
            produto = form.save(commit=False)

            produto.user = request.user
            produto.save()

            return redirect('appproduto:produto_list_view')

        return render(request, self.template_name, {'form': form})







