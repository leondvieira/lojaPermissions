from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from django.contrib.auth.forms import UserChangeForm

from appusuario.forms import UserForm
from appusuario.models import ComplementoUser

class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = ComplementoUser


class MyUserAdmin(UserAdmin):
    form = UserForm

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('pedido',)}),
    )


admin.site.register(ComplementoUser, MyUserAdmin)