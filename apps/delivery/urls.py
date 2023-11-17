# Django
from django.urls import path

# Local
from .views import DeliveryView

urlpatterns = [
    path('', DeliveryView.as_view(), name='delivery'),
]