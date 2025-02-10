from django.urls import path
from .views import products_list , product_detail

urlpatterns = [
    path("products" , products_list),
    path("products/<id>" , product_detail)
]
