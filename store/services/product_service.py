from store.models import Product
from store.serializers import ProductSerializer
from django.shortcuts import get_object_or_404


def product_list():
    query_set = Product.objects.all()
    serializer = ProductSerializer(query_set , many=True)
    return serializer.data


def product_by_id(id):
    product = get_object_or_404(Product , pk=id)
    serializer = ProductSerializer(product)
    return serializer.data