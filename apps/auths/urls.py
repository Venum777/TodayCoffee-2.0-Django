# Django
from django.urls import path

# Local
from .views import LoginView, RegisterView, ProfileView, ChangePasswordView


urlpatterns = [
    path(
        'login/', 
        LoginView.as_view(), 
        name='login'
    ),
    path(
        'register/', 
        RegisterView.as_view(), 
        name='register'
    ),
    path(
        'change_password/', 
        ChangePasswordView.as_view(), 
        name='change_password'
    ),
    path(
        'profile/', 
        ProfileView.as_view(), 
        name='profile'
    )
]