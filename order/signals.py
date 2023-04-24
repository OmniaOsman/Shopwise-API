from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import User
from .models import Cart

@receiver(post_save, sender=User)
def create_cart(sender, instance, created, **kwargs):
    if created:
        Cart.objects.create(user=instance)