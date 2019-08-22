from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from .models.complementoUser import ComplementoUser
from .models.useradmin import UserAdmin

admin.site.register(ComplementoUser, UserAdmin)