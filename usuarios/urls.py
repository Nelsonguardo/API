from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserRegister, UserLogin

app_name='usuarios'
urlpatterns=[
    path('api/',include('usuarios.api.urls')),
    path('register/',UserRegister.as_view()),
    path('login/',UserLogin.as_view()),
]