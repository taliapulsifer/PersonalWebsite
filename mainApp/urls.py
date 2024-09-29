from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

app_name = 'personal_website'

urlpatterns = [
    path('', views.home, name='home'),
]

