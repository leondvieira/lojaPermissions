from django.contrib.auth.views import LoginView


class LoginUserView(LoginView):
    template_name = 'appusuario/login_user_form.html'