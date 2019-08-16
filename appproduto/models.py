from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Comentario(models.Model):
    titulo = models.CharField(max_length=100)
    texto_comentario = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Produto(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    valor = models.FloatField()
    descricao = models.CharField(max_length=500)
    comentario = models.ForeignKey(Comentario, on_delete=models.CASCADE)

class NotaFiscal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    data = models.DateField()
    emitida = models.BooleanField(default=False)