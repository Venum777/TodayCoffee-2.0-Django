# Generated by Django 4.2.3 on 2023-11-17 17:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_discounts_expiration_date_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discounts',
            name='expiration_date_discount',
            field=models.DateField(default=datetime.datetime(2023, 11, 22, 23, 22, 41, 381658), verbose_name='дата истечения'),
        ),
    ]
