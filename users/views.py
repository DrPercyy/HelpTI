from django.shortcuts import render, redirect, HttpResponse
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.

def login_screen(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username_form = request.POST.get('username')
        password_form = request.POST.get('password')

        user = authenticate(username = username_form, password = password_form)
        if user:
            return HttpResponse('Usuário Autenticado')
        else:
            messages.error(request, "Usuário ou Senha Invalida. Por favor tente novamente...")
            return redirect('/user/login')
def register_screen(request):
    if request.method == "GET":
        return render(request, 'register.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.filter(username=username).first()
        emailexists = User.objects.filter(email=email).first()
        if user:
            messages.error(request, "Este username já está sendo usado.")
            return redirect('/user/register')
        elif emailexists:
            messages.error(request, "Este e-mail já está cadastrado.")
            return redirect('/user/register')
        elif request.POST.get('username')=='' or request.POST.get('email')=='' or request.POST.get('password')=='':
            messages.error(request, "Os campos não podem ficar vazios.")
            return redirect('/user/register')
        else:
            user= User.objects.create_user(username=username, email=email, password=password)
            user.save()
    return HttpResponse('Usuário cadastrado no sitema')

def profile_screen(request):
    return render(request, 'profile.html')
