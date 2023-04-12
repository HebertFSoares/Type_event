from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants
from django.urls import reverse
from django.contrib import auth

import re

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    
    elif request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirma_senha = request.POST.get('confirmar_senha')
        
        if len(senha) < 7:
            messages.add_message(request, constants.ERROR, 'A senha deve ter pelo menos 8 caracteres.')
            return redirect(reverse('cadastro'))
        
        elif re.search('[0-9]',senha) is None:
           messages.add_message(request, constants.ERROR, 'A senha deve conter pelo menos um número.')
           return redirect(reverse('cadastro'))
        
        elif re.search('[A-Z]',senha) is None:
           messages.add_message(request, constants.ERROR,  'A senha deve conter pelo menos uma letra maiúscula.')
           return redirect(reverse('cadastro'))
           
        if not senha == confirma_senha:
            messages.add_message(request, constants.ERROR, 'As senhas não coincidem')
            return redirect(reverse('cadastro'))
        
        user = User.objects.filter(username=username)
        
        if user.exists():
            messages.add_message(request, constants.ERROR, 'Usuario já esta cadastrado.')
            return redirect(reverse('cadastro'))
        
        user = User.objects.create_user(username=username, email=email,password=senha)
        
        messages.add_message(request, constants.SUCCESS, 'Usuario cadastrado com sucesso')
        return redirect(reverse('login'))
    
def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    
    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        
        user = auth.authenticate(username=username, password=senha)
        
        if not user:
            messages.add_message(request, constants.ERROR, 'Username ou senha inválidos')
            return redirect(reverse('login'))
        
        auth.login(request, user)
        return redirect('/evento/novo_evento')