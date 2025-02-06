from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product , User
from .serializers import ProductSerializer , UserSerializer
from django.shortcuts import get_object_or_404

# Create your views here.
@api_view(["GET"])
def product_list(request):
    query_set = Product.objects.all()
    serializer = UserSerializer(query_set , many=True)
    print(serializer.data)
    return Response(serializer.data)

@api_view(["GET"])
def product_detail(request , id):
    product = get_object_or_404(Product ,  pk=id)
    serializer = ProductSerializer(product)
    return Response(serializer.data)