# Python
import datetime

# Django
from django.db import models

# Local
from products.models.product import Product


class Discounts(models.Model):
    """Product discounts."""

    product_discount = models.ForeignKey(
        verbose_name='продукт',
        to=Product,
        on_delete=models.CASCADE,
        related_name='product_discount'
    )

    product_precent = models.IntegerField(
        verbose_name='процент',
    )

    expiration_date_discount = models.DateField(
        verbose_name='дата истечения',
        default=datetime.datetime.today() + datetime.timedelta(days=5)
    )

    @property
    def normal_precent(self):
        normalize_precent = self.product_discount.price / 100 * self.product_discount
        new_price = self.product_discount.price - normalize_precent
        return new_price

    class Meta:
        verbose_name = 'скидка'
        verbose_name_plural = 'скидки'

    def __str__(self) -> str:
        return self.discounts