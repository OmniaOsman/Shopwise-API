# Generated by Django 3.2.16 on 2023-01-25 13:40

from django.db import migrations
import django_autoslugfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_auto_20230125_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=django_autoslugfield.fields.AutoSlugField(title_field=None, unique=True),
        ),
    ]
