# Python
import uuid

# Django
from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.db.models.query import QuerySet
from django.views.generic import View
from django.core.files.uploadedfile import InMemoryUploadedFile

# Local
from .models import Product, Genre, Discounts

class MainView(View):
    
    def get(self, request: HttpRequest) -> HttpResponse:
        template_name: str = 'products/all_product.html'
        products: QuerySet[Product] = Product.objects.all().order_by('id')
        return render(
            request=request,
            template_name=template_name,
            context={
                'products': products,
            }
        )
    
class ProductView(View):

    def get(self, request: HttpRequest, genre_id: int) -> HttpResponse:
        try:
            genres: QuerySet[Genre] = Genre.objects.get(id=genre_id)
            products: QuerySet[Product] = Product.objects.filter(genres=genres)
        except Genre.DoesNotExist as e:
            return HttpResponse(
                f'<h1>Жанра с id {genre_id} не существует!</h1>'
            )
        return render(
            request=request,
            template_name='products/product.html',
            context={
                'genres': genres,
                'products': products
            }
        )