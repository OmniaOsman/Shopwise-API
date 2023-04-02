from django.urls import path
from shop.views import *

urlpatterns = [    
    # Products
    path('products/', ListCreateProductAPIView.as_view()),
    path('products/<product_slug>/', ProductDetailAPIView.as_view()),
    
    # Category
    path('category/', ListCreateCategoryAPIView.as_view()),
    path('category/<slug>/', CategoryDetailAPIView.as_view()),
]