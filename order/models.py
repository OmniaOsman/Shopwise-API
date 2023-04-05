from django.db import models
from accounts.models import User
from shop.models import Product
from django.contrib.auth import get_user_model


# Create your models here.
class Cart(models.Model):
    user        = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at  = models.DateTimeField(auto_now_add=True)
    no_of_items = models.PositiveIntegerField(default=0)
    total       = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    
    def get_total(self):
        total = 0
        for item in self.cartitem_set.all():
            total += item.quantity * float(item.product.product_price)
        self.total = total
        self.save()
        return float(total)
    
    def get_no_of_items(self):
        no_of_items = len(self.cartitem_set.all())
        self.no_of_items = no_of_items
        self.save()
        return no_of_items
    
    def __str__(self):
        return f'{self.user.username}'


class CartItem(models.Model):
    cart     = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product  = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.cart.get_total()
        self.cart.get_no_of_items()

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        self.cart.get_no_of_items()
        self.cart.get_total()

    def __str__(self):
        return f'{self.product.product_title} - {self.quantity}'