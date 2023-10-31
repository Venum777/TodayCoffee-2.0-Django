from django.shortcuts import render
from django.views.generic import View
from django.core.handlers.wsgi import WSGIRequest
from django.http.response import HttpResponse
from django.db.models.query import QuerySet
from django.forms.models import ModelFormMetaclass


from products.models import Cart, CartItem
from .models import Delivery
from .forms import DeliveryForm


class Delivery(View):
    
    template_name = 'delivery.html'
    form: ModelFormMetaclass = DeliveryForm

    def get(
        self,
        request: WSGIRequest,
        *args: tuple,
        **kwargs: dict
    ) -> HttpResponse:
        cart_item: QuerySet[CartItem] = CartItem.objects.all().filter(user=request.user)
        return render(
            request=request,
            template_name=self.template_name,
            context={
                'cart_item': cart_item,
                'ctx_form': self.form()
            }
        )

    def post(
        self,
        request: WSGIRequest,
        *args: tuple,
        **kwargs: dict
    ) -> HttpResponse:
        cart_item: QuerySet[CartItem] = CartItem.objects.all()
        return render(
            request=request,
            template_name=self.template_name,
            context={
                'cart_item': cart_item,
                'ctx_form': self.form()
            }
        )