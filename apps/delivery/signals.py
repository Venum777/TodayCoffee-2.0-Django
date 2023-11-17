# Django
from django.db.models.base import ModelBase
from django.db.models.signals import (
    post_delete,
    post_save,
    pre_delete,
    pre_save
)
from django.dispatch import receiver
from django.core.handlers.wsgi import WSGIRequest

# First party
from abstracts.utils import send_email
from delivery.models import Delivery
from cart.models import CartItem

# @receiver(
#     post_save,
#     sender=Delivery
# )
# def post_save_delivery(
#         sender: ModelBase,
#         instance: Delivery,
#         created: bool,
#         **kwargs: dict
#     ) -> None:
#     if created:
#         to_emails: list[str] = [
#             'venums46@gmail.com'
#         ]
#         send_email(
#             f'Заказали доставку!',
#             (f'''
#             ---------------------------------
#             ID товара: {instance.id}
#             ---------------------------------
#             Дата заказа: {instance.created_tampstamp}
#             Город: {instance.get_city_display()}
#             Адрес: {instance.address}
#             Дом: {instance.house}
#             Квартира: {instance.apartment}
#             Метод оплаты: {instance.get_payment_display()}
#             Комментарий:\n {instance.comment}
#             ---------------------------------
#             '''
#             ),
#             to_emails
#         )

@receiver(post_save, sender=Delivery)
def post_save_delivery(
        sender: ModelBase, 
        instance: Delivery,
        created: bool, 
    **kwargs) -> None:
    if created:
        to_emails = ['venums46@gmail.com']
        
        cart_items = CartItem.objects.filter(user=instance.user.id)
        total_price = sum(cart_item.total_price for cart_item in cart_items)

        message = f'''
            ---------------------------------
            ID товара: {instance.id}
            ---------------------------------
            Дата заказа: {instance.created_tampstamp}
            Город: {instance.get_city_display()}
            Адрес: {instance.address}
            Дом: {instance.house}
            Квартира: {instance.apartment}
            Метод оплаты: {instance.get_payment_display()}
            Комментарий:\n {instance.comment}
            ---------------------------------
            Товары:
        '''
        for cart_item in cart_items:
            message += f'''
                Товар: {cart_item.product.name}
                Количество: {cart_item.quantity}
                Цена за шт. : {cart_item.product.price}
                ---------------------------------
            '''
        message += f'''
        Итого: {total_price}
        ---------------------------------
        '''
        send_email(
            'Заказали доставку!',
            message,
            to_emails
        )
