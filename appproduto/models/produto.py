from django.contrib.auth.models import User
from django.db import models

from .comentario import Comentario

class Produto(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    valor = models.FloatField()
    descricao = models.CharField(max_length=500)
    comentario = models.ForeignKey(Comentario, null=True, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()

    def __str__(self):
        return self.nome