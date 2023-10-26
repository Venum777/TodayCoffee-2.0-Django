# Django
from django.contrib import admin

# Local
from .models import Delivery

@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = [
        'city',
        'address',
        'house',
        'apartment',
        'payment',
        'comment'
    ]
    list_filter = ['city', 'address', 'house', 'apartment']
