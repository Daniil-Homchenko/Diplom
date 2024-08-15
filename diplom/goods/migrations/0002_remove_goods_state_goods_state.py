# Generated by Django 5.0.6 on 2024-06-27 00:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goods',
            name='state',
        ),
        migrations.AddField(
            model_name='goods',
            name='state',
            field=models.ForeignKey(help_text='Укажите состояние товара', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='goods', to='goods.state', verbose_name='Состояние'),
        ),
    ]
