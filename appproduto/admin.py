from django.contrib import admin
from .models import Produto, NotaFiscal, Comentario

# Register your models here.
admin.site.register(Produto)
admin.site.register(NotaFiscal)
admin.site.register(Comentario)