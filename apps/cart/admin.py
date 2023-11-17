from django.contrib import admin

from cart.models import CartItem


@admin.register(CartItem)
class MyUserAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'product',
        'quantity',
    ]
    list_filter = ['user',]
