from shop.serializers import *
from order.models import CartItem
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import viewsets
from shop.models import *
from rest_framework.filters import SearchFilter
from rest_framework import permissions


class ListCreateProductAPIView(generics.ListCreateAPIView):
    """
    Method: GET, POST
    URL: /api/products/
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )   
    
    # search
    filter_backends = (SearchFilter, )
    search_fields = ('product_title', 'product_brand')
    
    
class ListCreateCategoryAPIView(generics.ListCreateAPIView):
    """
    Method: GET, POST
    URL: /api/category/
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer  
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    
    # search
    filter_backends = (SearchFilter, )
    search_fields = ('title', )
    

class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Method: GET, PATCH, POST, PUT, DELETE
    URL: products/<product_slug>/
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'product_slug'
    

class CategoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Method: GET, PATCH, POST, PUT, DELETE
    URL: category/<slug>/
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'
    