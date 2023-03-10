# Generated by Django 3.2.16 on 2023-01-25 13:42

from django.db import migrations, models
import django_autoslugfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_alter_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=django_autoslugfield.fields.AutoSlugField(title_field=models.CharField(max_length=150, unique=True), unique=True),
        ),
    ]
