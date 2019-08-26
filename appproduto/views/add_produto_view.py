from django.shortcuts import redirect

from appproduto.models import Produto, Pedido


def add_produto_view(request, pk):

    user = request.user
    user.save()

    produto1 = Produto.objects.get(pk=pk)

    pedido1 = Pedido()
    pedido1.pk = 1
    pedido1.numero_pedido = 123
    pedido1.save()

    pedido1.produto.add(produto1)
    pedido1.save()

    user.pedido = pedido1
    user.save()

    return redirect('appproduto:produto_list_view')



