# Generated by Django 5.0.6 on 2024-07-17 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0008_alter_goods_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='image',
            field=models.ImageField(blank=True, help_text='Выберите изображение товара', upload_to='static/img/', verbose_name='Изображение товара'),
        ),
    ]
