from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView

from appproduto.models import Produto


class ProdutoDeleteView(DeleteView):
    template_name = 'appproduto/produto_delete.html'
    model = Produto
    context_object_name = 'produto'
    success_url = reverse_lazy('appproduto:produto_list_view')
