# Generated by Django 3.2.16 on 2023-01-17 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_rename_cartitems_cartitem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product_desc',
            new_name='desc',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='product_img',
            new_name='img',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='product_price',
            new_name='price',
        ),
    ]
