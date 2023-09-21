# Django
from django.urls import path

# Local
from .views import AllProductView, ProductView
from . import views


urlpatterns = [
    path('all/', AllProductView.as_view()),
    path('', ProductView.as_view()),
    path('genre/<int:genre_id>/', ProductView.as_view()),
]