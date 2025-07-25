from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import UserLogin, UserViewSet, UserAuthProfile

router = DefaultRouter()
router.register(r'users',UserViewSet)

urlpatterns=[
    path('login/',UserLogin.as_view(),name='login'),
    path('perfil/', UserAuthProfile.as_view(),name='perfil'),
    path('', include(router.urls))
]