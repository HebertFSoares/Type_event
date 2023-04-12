from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User

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
           return redirect('/usuarios/cadastro')
            
        if not senha == confirma_senha:
            return redirect('/usuarios/cadastro')
        
        user  = User.objects.filter(username=username)
        
        if user.exists():
            return redirect('/usuarios/cadastro')
        
        user = User.objects.create_user(username=username,email=email,password=senha)
        
        return HttpResponse("CERTO")