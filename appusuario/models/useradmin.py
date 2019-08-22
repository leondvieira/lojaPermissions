from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from appusuario.forms import UserForm


class UserAdmin(BaseUserAdmin):
    add_form = UserForm
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'pedido', 'password1', 'password2')}
        ),
    )