from django.db import models

from appproduto.models import Produto


class Pedido(models.Model):
    produto = models.ManyToManyField(Produto)
    numero_pedido = models.IntegerField()


    def __int__(self):
        return self.numero_pedido
