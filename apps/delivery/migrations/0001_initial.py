# Generated by Django 4.2.3 on 2023-11-17 17:22

import auths.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(choices=[('as', 'Астана'), ('al', 'Алматы'), ('sh', 'Шымкент'), ('ko', 'Кокшетау'), ('ak', 'Актобе'), ('ta', 'Талдыкорган'), ('at', 'Атырау'), ('ur', 'Уральск'), ('tar', 'Тараз'), ('ki', 'Кызылорда'), ('akt', 'Актау'), ('pe', 'Петропавловск'), ('tu', 'Туркестан'), ('us', 'Усть-Каменогорск'), ('se', 'Семей'), ('pa', 'Павлодар'), ('krg', 'Караганды'), ('kos', 'Костанай'), ('ek', 'Экибастуз '), ('zhe', 'Жезказган'), ('kon', 'Конаев'), ('kas', 'Каскелен'), ('zhet', 'Жетысай'), ('te', 'Темиртау'), ('ar', 'Аркалык'), ('ru', 'Рудный')], default='krg', max_length=20, verbose_name='город')),
                ('address', models.CharField(max_length=200, verbose_name='адрес')),
                ('house', models.CharField(max_length=10, verbose_name='дом')),
                ('apartment', models.IntegerField(verbose_name='квартира')),
                ('payment', models.CharField(choices=[('nal', 'Наличными'), ('ter', 'Терминал у курьера')], default='nal', max_length=20, verbose_name='метод оплаты')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='комментарий')),
                ('created_tampstamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(default=auths.models.MyUser, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'доставка',
                'verbose_name_plural': 'доставки',
                'ordering': ('city', 'address', 'house', 'apartment'),
            },
        ),
    ]
