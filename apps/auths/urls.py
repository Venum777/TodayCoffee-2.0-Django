# Django
from django.urls import path

# Local
from .views import LoginView, RegisterView


urlpatterns = [
    path('auth/', LoginView.as_view()),
    path('register/', RegisterView.as_view())
]