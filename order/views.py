from rest_framework import viewsets
from .models import Cart, CartItem
from rest_framework import permissions
from .serializers import CartSerializer, CartItemSerializer


class CartView(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = (permissions.AllowAny, )
    lookup_field = 'user'


class CartItemView(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = (permissions.AllowAny, )
    lookup_field = 'id'