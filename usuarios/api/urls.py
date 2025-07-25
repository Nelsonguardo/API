from rest_framework.routers import DefaultRouter
from .viewsets import UserLogin, UserViewSet, UserAuthProfile
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


router = DefaultRouter()
router.register(r'users',UserViewSet)


schema_view = get_schema_view(
    openapi.Info(
        title="Docuemntacion APi Usuarios",
        default_version='v1',
        description="Explora la documentación completa la API, diseñada con drf-yasg para facilitar la integración y el desarrollo. Incluye detalles sobre endpoints, autenticación y ejemplos de uso.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@yourproject.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns=[
    path('login/',UserLogin.as_view(),name='login'),
    path('perfil/', UserAuthProfile.as_view(),name='perfil'),
    path('', include(router.urls)),
    re_path(r'^swagger(?P<format>.json|.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]