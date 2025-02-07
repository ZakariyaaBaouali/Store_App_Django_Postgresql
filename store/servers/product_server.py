from django.shortcuts import get_object_or_404
from rest_framework.request import Request
from ..models import Product
from ..serializers import ProductSerializer


def get_products(request: Request):
    query_set = Product.objects.all()
    serializer = ProductSerializer(query_set, many=True)
    return serializer.data


def get_product_details(request: Request, id):
    product = get_object_or_404(Product, pk=id)
    serializer = ProductSerializer(product)
    return serializer.data


def create_new_product(request: Request):
    serializer = ProductSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
