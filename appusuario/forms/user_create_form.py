from django.contrib.auth.models import User
from django.forms import ModelForm, forms


class UserForm(ModelForm):
    class Meta:
        model = User

        fields = [
            'username',
            'password',
            'email',
            'first_name'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget.attrs['class'] = 'form-control'