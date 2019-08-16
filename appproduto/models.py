from django.db import models

# Create your models here.

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    valor = models.FloatField()
    descricao = models.CharField(max_length=500)

class NotaFiscal(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    data = models.DateField()
    emitida = models.BooleanField(default=False)
