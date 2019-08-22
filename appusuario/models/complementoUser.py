from django.contrib.auth.models import AbstractUser
from django.db import models

from appproduto.models import Pedido


class ComplementoUser(AbstractUser):

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, null=True, related_name='pedido_from_user')

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        app_label = 'app_auth'
        db_table = "app_user"



