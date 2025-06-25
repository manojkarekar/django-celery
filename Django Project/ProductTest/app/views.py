from rest_framework import generics
from .models import Products
from .serializers import ProductSerializer

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer




from django.shortcuts import render

def add_product_page(request):
    return render(request, 'index.html')
