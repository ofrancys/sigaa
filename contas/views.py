from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.messages import constants   
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib import auth
#from sigaa.contas.utils import password_is_valid
from . models import Conta


def cadastro(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, 'contas/cadastro.html')

    elif request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if not password_is_valid(request, password, confirm_password):
            return redirect('/auth/cadastro')
        
        try:
            user = User.objects.get(username=username)
            messages.add_message(request, constants.ERROR, 'Usuário já cadastrado')
            return redirect('/auth/cadastro')
        except User.DoesNotExist:
            pass

        user = User.objects.create_user(username=username, email=email, password=password, is_active=True)
        user.save()
        ativacao = Conta(user=user, ativo=True)
        ativacao.save()
        return redirect('/auth/login')

def login(request):
    return render(request, 'contas/login.html')

def logout(request):
    return render(request, 'contas/logout.html')

