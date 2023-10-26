from django.db import models


class Delivery(models.Model):
    """Delivery class model"""

    CITIES_OF_KAZAKHSTAN: list = (
        ('as', 'Астана'),
        ('al', 'Алматы'),
        ('sh', 'Шымкент'),
        ('ko', 'Кокшетау'),
        ('ak', 'Актобе'),
        ('ta', 'Талдыкорган'),
        ('at', 'Атырау'),
        ('ur', 'Уральск'),
        ('tar', 'Тараз'),
        ('ki', 'Кызылорда'),
        ('akt', 'Актау'),
        ('pe', 'Петропавловск'),
        ('tu', 'Туркестан'),
        ('us', 'Усть-Каменогорск'),
        ('se', 'Семей'),
        ('pa', 'Павлодар'),
        ('krg', 'Караганды'),
        ('kos', 'Костанай'),
        ('ek', 'Экибастуз '),
        ('zhe', 'Жезказган'),
        ('kon', 'Конаев'),
        ('kas', 'Каскелен'),
        ('zhet', 'Жетысай'),
        ('te', 'Темиртау'),
        ('ar', 'Аркалык'),
        ('ru', 'Рудный')
    )

    METHOD_PAY = (
        ('nal', 'Наличными'),
        ('ter', 'Терминал у курьера')
    )

    city = models.CharField(
        verbose_name='город',
        choices=CITIES_OF_KAZAKHSTAN,
        default='krg',
        max_length=20
    )

    address = models.CharField(
        verbose_name='адресс',
        max_length=200
    )

    house = models.CharField(
        verbose_name='дом',
        max_length=10
    )

    apartment = models.IntegerField(
        verbose_name='квартира'
    )

    payment = models.CharField(
        verbose_name='метод оплаты',
        choices=METHOD_PAY,
        default='nal',
        max_length=20
    )

    comment = models.TextField(
        verbose_name='комментарий',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.city