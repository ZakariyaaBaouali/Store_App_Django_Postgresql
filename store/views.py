from rest_framework.decorators import api_view
from rest_framework.response import Response
from .servers import product_server


# Create your views here.
@api_view(["GET"])
def product_list(request):
    data = product_server.get_products(request)
    return Response(data)


@api_view(["GET"])
def product_detail(request, id):
    data = product_server.get_product_details(request, id)
    return Response(data)


@api_view(['POST'])
def create_product(request):
    data = product_server.create_new_product(request)
    return Response(data)
