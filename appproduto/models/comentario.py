from django.contrib.auth.models import User
from django.db import models

from lojaPermissions import settings


class Comentario(models.Model):
    titulo = models.CharField(max_length=100)
    texto_comentario = models.CharField(max_length=500)
    #user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo