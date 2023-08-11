from django.db import models

# Create your models here.
import datetime

from django.db import models
# from django.contrib.auth.models import User

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
        upload_to='image/',
        default='image/unknown.png'
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

    def str(self) -> str:
        return self.discounts