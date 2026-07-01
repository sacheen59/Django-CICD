from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from . serializers import ProductSerializer

class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

