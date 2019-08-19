from django.urls import path, include
from django.views.generic import TemplateView

from .views.update_user_view import UserUpdateView
from .views.logout_user_view import logout_view
from .views.login_user_view import LoginUserView
from .views.creater_user_view import UserCreateView


app_name = 'appusuario'

urlpatterns = [
    path('user/login', LoginUserView.as_view(), name='login'),
    path('user/logout', logout_view, name='logout'),
    path('user/update/<pk>', UserUpdateView.as_view(), name='update_user_view'),
    path('cadastro', UserCreateView.as_view(), name='user_create_view'),
    path('user/', include('django.contrib.auth.urls')),
]
