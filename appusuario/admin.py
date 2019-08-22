from django.contrib import admin

from appusuario.models.complementoUser import ComplementoUser
from appusuario.models import UserAdmin

admin.site.register(ComplementoUser, UserAdmin)