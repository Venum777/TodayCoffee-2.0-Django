# Django
from django.urls import path

# Local
from .views import ProductView

urlpatterns = [
    path('', ProductView.as_view(), name='home'),
    path('genre/<int:genre_id>/', ProductView.as_view()),
]