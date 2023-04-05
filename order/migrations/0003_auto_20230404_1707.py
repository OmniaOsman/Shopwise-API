# Generated by Django 3.2.16 on 2023-04-04 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_cart_products'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='products',
        ),
        migrations.AddField(
            model_name='cart',
            name='no_of_items',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='cart',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=9),
        ),
    ]
