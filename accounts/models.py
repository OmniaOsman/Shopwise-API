from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(max_length=254, unique=True)
    is_active = models.BooleanField(default=True)
    REQUIRED_FIELDS = ('first_name', 'last_name', 'username', )
    USERNAME_FIELD = 'email'
    
    def __str__(self):
        return self.username
    