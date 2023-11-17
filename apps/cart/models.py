# Django
from django.db import models

# Local
from products.models.product import Product
from auths.models import MyUser


class CartManager(models.Manager):

    def add_to_cart(
            self, 
            user_id: int, 
            product_id: int,
            # quantity: int
        ):
        user = MyUser.objects.get(id=user_id)
        product = Product.objects.get(id=product_id)
        try:
            cart = CartItem.objects.create(
                user=user,
                product=product,
                # quantity=quantity
            )
            cart.save()
        except Exception as e:
            return '[ERROR] Ошибка при добавлении товара'

    def clear_cart(self, user):
        self.filter(user=user).delete()

    def delete_item(self, product_id: int):
        item_to_delete = self.filter(product=product_id).first()
        try:
            item_to_delete.delete()
        except Exception as e:
            return '[ERROR] Ошибка при удалении товара'

class CartItem(models.Model):

    user = models.ForeignKey(
        MyUser,
        verbose_name='пользователь',
        on_delete=models.CASCADE
    )

    product = models.ForeignKey(
        Product,
        verbose_name='продукт',
        on_delete=models.CASCADE
    )

    quantity = models.PositiveIntegerField(
        verbose_name='сколько',
        default=1
    )

    objects = CartManager()
    @property
    def total_price(self):
        total_price = self.product.price * self.quantity
        return total_price

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"
    