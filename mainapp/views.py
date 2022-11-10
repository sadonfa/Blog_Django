from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# from mainapp.forms import RegistroForm

# Create your views here.


def index(request):

    return render(request, 'mainapp/index.html', {
        'title': 'Inicio'
    })

def about(request):

    return render(request, 'mainapp/about.html', {
        'title': 'Sobre Nosotros'
    })

def register_user(request):

    register_form = UserCreationForm()

    if request.method == 'POST':

        register_form = UserCreationForm(request.POST)

        if register_form.is_valid():
            register_form.save()
            messages.success(request,  'Te has registrado correctamente')

            return redirect('inicio')


    return render(request, 'user/register.html', {
        'title': 'Registro',
        'register_form': register_form
    })

def login_page(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            return redirect('inicio')
        else:
            messages.warning(request, 'No te has identificado correctamente')

    return render(request, 'user/login.html', {
        'title': 'Identificate'
    })

def logout_user(request):
    logout(request)
    return redirect('inicio')