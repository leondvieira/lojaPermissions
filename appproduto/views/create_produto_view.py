from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from appproduto.forms.create_produto_form import ProdutoForm
from appproduto.models import Produto


class ProdutoCreateView(CreateView):
    template_name = "appproduto/produto_create_form.html"
    model = Produto

    def get(self, request):
        form = ProdutoForm
        if not request.user.is_authenticated:
            return HttpResponseRedirect('appbase:home')
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ProdutoForm(request.POST)

        if form.is_valid():
            form.save()

            nome = request.POST['nome']
            valor = request.POST['valor']
            descricao = request.POST['descricao']
            quantidade = request.POST['quantidade']
            user = request.user

            produto = Produto.objects.latest

        print(form)
        print(user)
        print('AAAAAAAAAAAA')







