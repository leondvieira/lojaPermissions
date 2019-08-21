from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from appusuario.models import ComplementoUser

admin.site.register(ComplementoUser, UserAdmin)