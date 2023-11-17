# Django
from django.urls import path

# Local
from auths.views.login_view import LoginView
from auths.views.register_view import RegisterView
from auths.views.profile_view import ProfileView
from auths.views.change_password_view import ChangePasswordView
from auths.views.logout_view import LogoutView


urlpatterns = [
    path(
        'register/', 
        RegisterView.as_view(), 
        name='register'
    ),
    path(
        'login/', 
        LoginView.as_view(), 
        name='login'
    ),
    path(
        'change_password/', 
        ChangePasswordView.as_view(), 
        name='change_password'
    ),
    path(
        'logout/', 
        LogoutView.as_view(), 
        name='logout'
    ),
    path(
        'profile/', 
        ProfileView.as_view(), 
        name='profile'
    )
]
