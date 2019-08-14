from django.urls import path, include

from .views.login_user_view import LoginUserView
from .views.creater_user_view import UserCreateView

app_name = 'appusuario'

urlpatterns = [
    path('user/login', LoginUserView.as_view(), name='login'),
    path('cadastro', UserCreateView.as_view(), name='user_create_view'),
    path('user/', include('django.contrib.auth.urls')),
]
