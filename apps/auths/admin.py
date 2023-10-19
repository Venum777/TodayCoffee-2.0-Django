# Django
from django.contrib import admin
from .models import MyUser

@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
    list_display = [
        'first_name',
        'last_name',
        'email',
        'phone_number',
        'password'
    ]
    list_filter = ['first_name', 'last_name', 'email', 'phone_number']
