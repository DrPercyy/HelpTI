from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Estou em usuários")

def login(request):
    pass

def register(request):
    pass

def admin(request):
    pass
