from django.urls import path

from appbase.views import HomePageView

app_name = 'appbase'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
]
