# Generated by Django 5.0.6 on 2024-06-29 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0005_state_alter_goods_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='image',
            field=models.ImageField(help_text='Выберите изображение товара', upload_to='img/', verbose_name='Изображение товара'),
        ),
    ]
