from rest_framework.response import Response
from rest_framework.decorators import api_view
from store.services import product_service


#test api for my database
@api_view()
def products_list(request):
    data = product_service.product_list()
    return Response(data)


@api_view()
def product_detail(request , id):
    data = product_service.product_by_id(id)
    return Response(data)