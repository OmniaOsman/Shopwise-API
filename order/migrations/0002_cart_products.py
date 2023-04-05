# Generated by Django 3.2.16 on 2023-03-30 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0022_remove_category_featured_product'),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(through='order.CartItem', to='shop.Product'),
        ),
    ]