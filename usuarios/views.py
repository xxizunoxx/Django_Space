from django.shortcuts import render, redirect
from usuarios.forms import LoginForms,CadastroForms
from django.contrib.auth.models import User
from django.contrib import auth, messages

def login(request):
    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)
        if form.is_valid():
            nome= form["nome_login"].value()
            password= form["password"].value()

            usuario = auth.authenticate(request, username=nome, password=password)
            if usuario is not None:
                auth.login(request, usuario)
                messages.success(request, f'{nome}, Bem Vindo!')
                return redirect('index')
            else:
                messages.error(request, 'Usuário ou senha inválidos.')
                return redirect('login')

    return render(request, 'usuarios/login.html', {'form': form})

def cadastro(request):
    form = CadastroForms()

    if request.method == 'POST':
        form = CadastroForms(request.POST)

        if form.is_valid():
            
            nome= form["nome_cadastro1"].value()
            sobrenome= form["nome_cadastro2"].value()
            user= form["nome_user"].value()
            email= form["email"].value()
            password= form["password1"].value()

            if User.objects.filter(username=user).exists():
                messages.error(request, 'Nome de usuário já existe.')
                return redirect('cadastro')
            
            usuario = User.objects.create_user(username=user, email=email, password=password, first_name=nome, last_name=sobrenome)
            usuario.save()
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('login')


        
        
    return render(request, 'usuarios/cadastro.html', {'form': form})

def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout realizado com sucesso!')
    return redirect('login')
