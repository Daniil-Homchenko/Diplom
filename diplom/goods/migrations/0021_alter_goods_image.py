# Generated by Django 5.0.6 on 2024-07-19 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0020_remove_goods_email_alter_goods_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='image',
            field=models.FileField(blank=True, help_text='Выберите изображение товара', null=True, upload_to='img/', verbose_name='Изображение товара'),
        ),
    ]
