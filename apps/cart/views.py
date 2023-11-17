from django.shortcuts import get_object_or_404, redirect
from .models import CartItem


def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, pk=cart_item_id, user=request.user)
    cart_item.delete()
    return redirect('cart:cart_detail')
