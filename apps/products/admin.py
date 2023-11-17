# Python
from typing import Union , TypeAlias

# Django
from django.contrib import admin

# Local
from products.models.genre import Genre
from products.models.product import Product
from products.models.discounts import Discounts


MyType: TypeAlias = tuple[tuple[Union[str ,dict[str,list[str]]]]]

@admin.register(Product)
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

@admin.register(Genre)
class GenresAdmin(admin.ModelAdmin):
     list_display:list[str] = (
        'name',
    )

@admin.register(Discounts)
class DiscountsAdmin(admin.ModelAdmin):
     list_display:list[str] = (
        'product_discount',
        'product_precent',
        'expiration_date_discount'
    )
