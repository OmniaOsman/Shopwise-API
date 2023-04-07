from rest_framework import viewsets
from .models import Cart, CartItem
from rest_framework import permissions
from .serializers import CartSerializer, CartItemSerializer


class CartView(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    lookup_field = 'user'
    
    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            permission_classes = (permissions.IsAdminUser, )
        else:
            permission_classes = (permissions.AllowAny, )
        return [permission() for permission in permission_classes]


class CartItemView(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    lookup_field = 'id'
    
    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            permission_classes = (permissions.IsAdminUser, )
        else:
            permission_classes = (permissions.AllowAny, )
        return [permission() for permission in permission_classes]