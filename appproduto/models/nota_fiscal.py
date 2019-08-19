from django.contrib.auth.models import User
from django.db import models
from .produto import Produto

class NotaFiscal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    data = models.DateField()
    codigo = models.CharField(max_length=100)
    emitida = models.BooleanField(default=False)

    def __str__(self):
        return self.codigo