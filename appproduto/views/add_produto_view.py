from random import random

from django.shortcuts import get_object_or_404
from django.views import View

from appproduto.models import Produto, Pedido


class AddProdutoView(View):

    def get(self, request, id):
        user = request.user

        produto = get_object_or_404(Produto, id=id)

        pedido = Pedido()
        pedido.user = user
        pedido.numero_pedido = random.randint(1, 10000)
        pedido.produto.add(produto)



