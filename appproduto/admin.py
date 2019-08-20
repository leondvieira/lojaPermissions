from django.contrib import admin

from .models.pedido import Pedido
from .models.produto import Produto
from .models.comentario import Comentario


# Register your models here.


admin.site.register(Produto)
admin.site.register(Comentario)
admin.site.register(Pedido)
