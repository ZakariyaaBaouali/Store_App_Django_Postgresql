from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
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


@api_view(["POST" , "PATCH"])
def manage_product(request):
    if request.method == 'POST':
        product_server.create_new_product(request)
        return Response(status=status.HTTP_201_CREATED)
    elif request.method == 'PATCH':
        return Response("ok")
