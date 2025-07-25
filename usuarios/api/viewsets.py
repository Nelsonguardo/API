from http.client import responses

from rest_framework import viewsets, permissions
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomUserSerializer
from ..models import CustomUser


class UserLogin(TokenObtainPairView):
    def post(self, request: Request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserAuthProfile(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        user = request.user
        data = {
            'id' : user.id,
            'username' : user.username,
            'first_name' : user.first_name,
            'last_name' : user.last_name,
            'email' : user.email,
        }
        return Response(data)
