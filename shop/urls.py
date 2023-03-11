from django.urls import path
from shop.views import *

urlpatterns = [    
    # Products
    path('products/', ListProductAPIView.as_view()),
    path('products/create/', CreateProductAPIView.as_view()),
    path('products/<product_slug>/', ProductDetailAPIView.as_view()),
    
    # Category
    path('category/', ListCategoryAPIView.as_view()),
    path('category/create/', CreateCategoryAPIView.as_view()),
    path('category/<slug>/', CategoryDetailAPIView.as_view()),
]