from django.shortcuts import render
from django.views import View
from .models import CustomUser
from django.contrib.auth import aauthenticate, login, authenticate, get_user_model


User = get_user_model()


class UserRegister(View):
    def get(self, request):
        return render(request,'register.html',{})


    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        user = CustomUser.objects.create_user(
            username = username,
            password = password,
            first_name = first_name,
            last_name = last_name,
            email = email
        )
        return render(request,'register.html',{'user':user})


class UserLogin(View):
    def get(self, request):
        return render(request, 'login.html', {})

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Primero validamos si el usuario existe en la base de datos
        try:
            user_obj = User.objects.get(username=username)
        except User.DoesNotExist:
            # Si no existe, devolvemos un mensaje específico
            return render(request, 'login.html', {'error': 'El usuario no existe.'})

        # Si existe, ahora validamos la contraseña
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'perfil.html', {'user': user})
        else:
            # Usuario existe pero contraseña incorrecta
            return render(request, 'login.html', {'error': 'Contraseña incorrecta.'})