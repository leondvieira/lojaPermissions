from django.contrib.auth.models import User
from django.db import models

from appproduto.models import Produto


class Pedido(models.Model):
    produto = models.ManyToManyField(Produto)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    numero_pedido = models.IntegerField()


    def __str__(self):
        return self.numero_pedido
