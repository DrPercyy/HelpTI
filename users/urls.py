from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginscreen, name= 'login'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name = 'profile')
]