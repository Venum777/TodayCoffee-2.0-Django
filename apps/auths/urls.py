# Django
from django.urls import path

# Local
from .views import(
    LoginView, 
    RegisterView, 
    ProfileView, 
    ChangePasswordView,
    LogoutView
)


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