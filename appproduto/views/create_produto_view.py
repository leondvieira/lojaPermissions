from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView

from appproduto.forms.create_produto_form import ProdutoForm
from appproduto.models import Produto


class ProdutoCreateView(CreateView):
    template_name = "appproduto/produto_create_form.html"
    model = Produto
    form_class = ProdutoForm


