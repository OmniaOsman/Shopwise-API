from shop.serializers import *
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from shop.models import *
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated


class ListProductAPIView(ListAPIView):
    """
    Method: GET
    URL: /api/products/
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    # search
    filter_backends = (SearchFilter, )
    search_fields = ('product_title', 'product_brand')
    
    
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
    Method: GET, PATCH, POST, PUT, DELETE
    URL: products/<product_slug>/
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'product_slug'
    

class CategoryDetailAPIView(RetrieveUpdateDestroyAPIView):
    """
    Method: GET, PATCH, POST, PUT, DELETE
    URL: category/<slug>/
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'
    
    
# class ProductSearchView(ListAPIView):
#     """
#     Method: GET
#     URL: search/
#     """
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     filter_backends = [SearchFilter]
#     search_fields = ['name', 'description']