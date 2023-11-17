# Django
from django.shortcuts import render, redirect
from django.views.generic import View
from django.core.handlers.wsgi import WSGIRequest
from django.http.response import HttpResponse, HttpResponseRedirect
from django.db.models.query import QuerySet
from django.forms.models import ModelFormMetaclass

# Local
from delivery.models import Delivery
from delivery.forms import DeliveryForm
from cart.models import CartItem


temp_cart_items = []

class DeliveryView(View):
    
    template_name = 'delivery.html'
    form: ModelFormMetaclass = DeliveryForm
    model_cart = CartItem

    def get(
        self,
        request: WSGIRequest,
        *args: tuple,
        **kwargs: dict
    ) -> HttpResponse:
        cart_items = CartItem.objects.filter(user=request.user)
        total_price = sum(cart_item.total_price for cart_item in cart_items)
        return render(
            request=request,
            template_name=self.template_name,
            context={
                'cart_items': cart_items,
                'ctx_form': self.form(),
                'total_price': total_price
            }
        )
    
    def post(self, request: WSGIRequest) -> HttpResponse:
        product_id = request.POST.get('product_id')
        if 'delete' in request.POST:
            CartItem.objects.delete_item(product_id=product_id)
            return redirect('delivery')
        
        form = self.form(request.POST, initial={'user': request.user})
        if form.is_valid():
            delivery = form.save(commit=False)
            delivery.user = request.user
            delivery.save()
            temp_cart_items.extend(CartItem.objects.filter(user=request.user.id))
            CartItem.objects.clear_cart(user=request.user)
            return HttpResponseRedirect('')
        else:
            print(form.errors)
        return HttpResponse("Произошла ошибка при заказе.")

