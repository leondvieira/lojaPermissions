from django.contrib.auth.models import User
from django.db import models

from appproduto.models import Produto
from lojaPermissions import settings


class Pedido(models.Model):
    produto = models.ManyToManyField(Produto)
    numero_pedido = models.IntegerField()


    def __str__(self):
        return self.numero_pedido
