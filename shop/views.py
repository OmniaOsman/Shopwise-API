from shop.models import *
from shop.serializers import *
from rest_framework import generics, filters


class ListCreateProductAPIView(generics.ListCreateAPIView):
    """
    Method: GET, POST
    URL: /api/products/
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer  
    
    # search
    filter_backends = (filters.SearchFilter, )
    search_fields = ('product_title', 'product_brand')
    
    
class ListCreateCategoryAPIView(generics.ListCreateAPIView):
    """
    Method: GET, POST
    URL: /api/category/
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer  
    
    # search
    filter_backends = (filters.SearchFilter, )
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
    