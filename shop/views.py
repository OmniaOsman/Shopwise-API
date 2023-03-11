from django.shortcuts import get_object_or_404
from shop.serializers import *
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from shop.models import *
from django.urls import reverse_lazy
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Product, Category


class ListProductAPIView(ListAPIView):
    """
    Method: GET
    URL: /api/products/
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    
class CreateProductAPIView(CreateAPIView):
    """
    Method: POST
    URL: /api/products/create/
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated, )
    
    
class ListCategoryAPIView(ListAPIView):
    """
    Method: GET
    URL: /api/category/
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer  
    

class CreateCategoryAPIView(CreateAPIView):
    """
    Method: POST
    URL: /api/category/create/
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer  
    permission_classes = (IsAuthenticated, )
    
  


class ProductDetailAPIView(RetrieveUpdateDestroyAPIView):
    """
    Method: GET, PUT, DELETE
    URL: products/<product_slug>/
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'product_slug'
    

class CategoryDetailAPIView(RetrieveUpdateDestroyAPIView):
    """
    Method: GET
    URL: category/<slug>/
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'