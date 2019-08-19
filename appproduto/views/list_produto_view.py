from django.views.generic import ListView

from appproduto.models import Produto


class ProdutoListView(ListView):
    template_name = 'appbase/produto_list.html'
    model = Produto
    paginate_by = 30

    context_object_name = 'produtos'

