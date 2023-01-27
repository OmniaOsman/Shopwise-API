from django.shortcuts import get_object_or_404
from shop.serializers import *
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.views import APIView
from shop.models import *
from django.urls import reverse_lazy
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status


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
    
  
class ProductDetailAPIView(APIView):
    """
    Method: GET
    URL: products/<product_slug>/
    """
    # Get Product
    def get(self, request, product_slug):
        product = Product.objects.filter(product_slug= product_slug)
        product = get_object_or_404(product)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    # Edit Product
    def put(self, request, product_slug):
        product = Product.objects.get(product_slug=product_slug)
        serializer = ProductSerializer(product, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    
    # Delete Product
    def delete(self, request, product_slug):
        product = Product.objects.filter(product_slug=product_slug)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class CategoryDetailAPIView(APIView):
    """
    Method: GET
    URL: category/<slug>/
    """
    # Get Category
    def get(self, request, slug):
        category = Category.objects.filter(slug=slug)
        print(category)
        category = get_object_or_404(category)
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    
    # Edit Category
    def put(self, request, slug):
        category = Category.objects.get(slug=slug)
        serializer = CategorySerializer(category, data=request.data)
        print(category)
  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    
    # Delete Category
    def delete(self, request, slug):
        object = Category.objects.filter(slug=slug)
        object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)