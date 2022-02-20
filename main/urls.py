from django.urls import path
from .views import home,register

app_name = 'main'

urlpatterns = [
    path('',home,name="home"),
    path('register/',register,name="register")
]