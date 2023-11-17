# Django
from django.db import models

# Local
from products.models.genre import Genre


def product_directory_path(instance, filename):
    return f'image/product/{instance.genres}/{filename}'


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