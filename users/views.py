from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.http import HttpResponse

# Create your views here.

def login(request):
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redireciona para a página de login ou para onde desejar
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def admin(request):
    pass
