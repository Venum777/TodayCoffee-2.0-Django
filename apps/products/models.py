# Python
import datetime

# Django
from django.db import models

# Local
from auths.models import MyUser


def product_directory_path(instance, filename):
    return f'image/product/{instance.genres}/{filename}'

class Genre(models.Model):
    """Product genre."""

    name = models.CharField(
        verbose_name='название',
        max_length=130,
        unique=True
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'жанр'
        verbose_name_plural = 'жанры'

    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    """TodayCoffee product."""

    name = models.CharField(
        verbose_name='имя',
        max_length=250,
        unique=True
    )

    structure = models.TextField(
        verbose_name='состав',
        null=True,
        blank=True
    )

    price = models.DecimalField(
        verbose_name='цена',
        decimal_places=2,
        max_digits=12
    )

    genres = models.ForeignKey(
        verbose_name='жанр',
        to=Genre,
        on_delete=models.CASCADE,
        related_name='genre_product',
        null=True,
        blank=True
    )

    rate = models.SmallIntegerField(
        verbose_name='рейтинг',
        default=1
    )

    image = models.ImageField(
        verbose_name='изображение',
        upload_to=product_directory_path,
        default='image/product/unknown.png'
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'товар'
        verbose_name_plural = 'товары'

    def __str__(self) -> str:
        return self.name

class Discounts(models.Model):
    """Product discounts."""

    discounts = models.ForeignKey(
        verbose_name='скидки',
        to=Product,
        on_delete=models.CASCADE,
        related_name='product_discount'
    )

    expiration_date = models.DateField(
        verbose_name='дата истечения',
        default=datetime.datetime.today() + datetime.timedelta(days=7)
    )

    class Meta:
        verbose_name = 'скидка'
        verbose_name_plural = 'скидки'

    def __str__(self) -> str:
        return self.discounts


class CartItem(models.Model):

    user = models.ForeignKey(
        MyUser, 
        on_delete=models.CASCADE
    )

    product = models.ForeignKey(
        Product, on_delete=models.CASCADE
    )

    quantity = models.PositiveIntegerField(
        default=1
    )

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"
    
    class Meta:
        verbose_name = 'Товары в корзине'
        verbose_name_plural = 'Товары в корзинах'

class Cart(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    items = models.ManyToManyField(CartItem)
    created_tampstamp = models.DateTimeField(auto_now_add=True)

    def total_price(self):
        total = 0
        for item in self.items.all():
            total += item.total_price()
        return total

    class Meta:
        verbose_name = 'корзина'
        verbose_name_plural = 'корзины'
    