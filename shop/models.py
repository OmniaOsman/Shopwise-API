from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField
    
class Category(models.Model):
    title = models.CharField(unique=True, max_length=150)
    slug  = AutoSlugField(unique=True, populate_from='title')
    
    def __str__(self) -> str:
        return self.title  


class Product(models.Model):
    product_title = models.CharField(max_length=150, unique=True)
    product_price = models.DecimalField(max_digits=8, decimal_places=2)
    product_desc  = models.TextField()
    product_brand = models.CharField(max_length=150)
    product_slug  = AutoSlugField(unique=True, populate_from='product_title')
    inventory     = models.SmallIntegerField()
    discount      = models.BooleanField(default=False)
    best_seller   = models.BooleanField(default=False)
    product_img   = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    category      = models.ForeignKey('Category', on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.product_title 
