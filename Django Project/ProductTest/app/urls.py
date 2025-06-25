from django.urls import path
from .views import ProductListCreateAPIView  , add_product_page

urlpatterns = [
   
    path('products/', ProductListCreateAPIView.as_view(), name='product-list-create'),
]
