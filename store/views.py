from rest_framework.response import Response
from rest_framework.decorators import api_view


#test api for my database
@api_view()
def products_list(request):
    return Response("ok")


@api_view()
def product_detail(request , id):
    return Response(f"ok id : {id}")