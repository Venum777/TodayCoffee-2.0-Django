from django.contrib import admin

from .models import Product, Genre, Discounts
from typing import Union , TypeAlias


MyType: TypeAlias = tuple[tuple[Union[str ,dict[str,list[str]]]]]

class ProductAdmin(admin.ModelAdmin):

    list_display:list[str] = (
        'name',
        'rate',
        'price',
    )

    list_filter: list[str] = (
        'genres',
    )
    fieldsets:MyType = (
        (
            'Public for my Today Coffee!',
            {
                'classes':['wide','extrapretty'],
                'fields':[
                    'name',
                    'structure',
                    'price',
                    'genres',
                    'image'
                ]
            }
        ),
        (
            'Private information',
            {
                'classes':['collapse'],
                'fields':[
                    'rate'
                ]
            }
        ),
        
    )

class GenresAdmin(admin.ModelAdmin):
     list_display:list[str] = (
        'name',
    )


class DiscountsAdmin(admin.ModelAdmin):
     list_display:list[str] = (
        'discounts',
        'expiration_date'
    )
    

admin.site.register(Product, ProductAdmin)
admin.site.register(Genre, GenresAdmin)
admin.site.register(Discounts, DiscountsAdmin)
