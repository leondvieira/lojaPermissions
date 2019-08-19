from django.contrib import admin

from .models.produto import Produto
from .models.comentario import Comentario
from .models.nota_fiscal import NotaFiscal

# Register your models here.


admin.site.register(Produto)
admin.site.register(NotaFiscal)
admin.site.register(Comentario)