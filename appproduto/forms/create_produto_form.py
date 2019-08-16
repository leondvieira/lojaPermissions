from django.forms import ModelForm

from appproduto.models import Produto


class ProdutoForm(ModelForm):

    class Meta:
        model = Produto
        fields = [
            'nome',
            'valor',
            'descricao'
        ]
