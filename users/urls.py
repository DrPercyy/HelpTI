from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_screen, name= 'login'),
    path('register/', views.register_screen, name='register'),
    path('profile/', views.profile_screen, name = 'profile')
]