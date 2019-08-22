from django.contrib import admin

from appproduto.models import Comentario, Produto, Pedido

# Register your models here.


admin.site.register(Produto)
admin.site.register(Comentario)
admin.site.register(Pedido)
