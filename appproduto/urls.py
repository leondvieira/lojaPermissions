from django.urls import path, include

from appproduto.views.create_produto_view import ProdutoCreateView

app_name = 'appproduto'

urlpatterns = [
    path('produto/cadastrar', ProdutoCreateView.as_view(), name='produto_create_view'),
]