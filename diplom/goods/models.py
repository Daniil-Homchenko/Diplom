from django.contrib.auth.models import User
from django.db import models

from diplom import settings


# Create your models here.
class Goods(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(verbose_name="Описание товара", help_text="Введите описание товара")
    state = models.ForeignKey('State', related_name='goods', verbose_name='Состояние',
                                          help_text='Укажите состояние товара', on_delete=models.CASCADE, null=True)
    image = models.FileField(upload_to='img/', verbose_name='Изображение товара', help_text='Выберите изображение товара', null=True, blank=True)
    price = models.DecimalField(default=0.00, decimal_places=2, max_digits=8, verbose_name="Цена",
                                help_text="Укажите цену товара")
    created_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    first_name = models.CharField(max_length=15, verbose_name='Имя продавца', help_text='Введите имя продавца')
    last_name = models.CharField(max_length=15, verbose_name='Фамилия продавца', help_text='Введите фамилию продавца')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    phone_number = models.IntegerField(verbose_name='Номер телефона', help_text='Введите номер телефона')

    def str(self):
        return f'{self.first_name}{self.last_name}'
class State(models.Model):
    state = models.CharField(max_length=15, verbose_name='Название жанра', help_text='Введите название жанра')

