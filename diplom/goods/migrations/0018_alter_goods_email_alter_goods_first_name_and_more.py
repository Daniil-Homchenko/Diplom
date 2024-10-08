# Generated by Django 5.0.6 on 2024-07-19 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0017_alter_goods_email_alter_goods_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='email',
            field=models.EmailField(blank=True, default='<django.db.models.query_utils.DeferredAttribute object at 0x000001E51E9EC700>', help_text='Введите почту продавца', max_length=100, null=True, verbose_name='Почта продавца'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='first_name',
            field=models.CharField(default='<django.db.models.query_utils.DeferredAttribute object at 0x000001E51E9EC5E0>', help_text='Введите имя продавца', max_length=15, verbose_name='Имя продавца'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='last_name',
            field=models.CharField(default='<django.db.models.query_utils.DeferredAttribute object at 0x000001E51E9EC670>', help_text='Введите фамилию продавца', max_length=15, verbose_name='Фамилия продавца'),
        ),
    ]
