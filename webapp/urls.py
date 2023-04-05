from .views import *
from django.urls import path

urlpatterns = [
    path('', home, name='home'),
    path('register', register, name="register"),
    path('login', login, name="login"),
    path('gadget.html', Gadgets, name = 'gadget')
]
