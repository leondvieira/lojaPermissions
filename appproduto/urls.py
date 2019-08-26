from django.urls import path, include

from appproduto.views.add_produto_view import add_produto_view
from appproduto.views.create_produto_view import ProdutoCreateView
from appproduto.views.delete_produto_view import ProdutoDeleteView
from appproduto.views.list_produto_view import ProdutoListView

app_name = 'appproduto'

urlpatterns = [
    path('', ProdutoListView.as_view(), name='produto_list_view'),
    path('produto/add/pedido/<pk>', add_produto_view, name='produto_add_view'),
    path('produto/deletar/<pk>', ProdutoDeleteView.as_view(), name='produto_delete_view'),
    path('produto/cadastrar', ProdutoCreateView.as_view(), name='produto_create_view'),
]
