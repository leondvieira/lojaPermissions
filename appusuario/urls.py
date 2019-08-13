from django.urls import path

from appusuario.views import LoginUserView

app_name = 'appusuario'

urlpatterns = [
    path('login', LoginUserView.as_view(), name='login'),
]
