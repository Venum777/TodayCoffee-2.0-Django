from django.urls import path

# Local
from .views import MainView, ProductView


urlpatterns = [
    path('all/', MainView.as_view()),
    path('genre/<int:genre_id>/', ProductView.as_view()),
]