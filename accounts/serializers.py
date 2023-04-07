from .models import *
from rest_framework import serializers
from djoser.serializers import UserSerializer, UserCreateSerializer

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('email', 'username', 'password', 'first_name', 
                  'last_name', 'is_superuser', 'is_active')