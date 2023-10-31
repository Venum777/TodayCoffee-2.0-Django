# Django
from django.urls import path

# Local
from .views import Delivery

urlpatterns = [
    path('', Delivery.as_view(), name='delivery'),
]