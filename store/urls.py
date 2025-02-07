from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.product_list),
    path('products/<id>/', views.product_detail),
    path('product/create/', views.create_product),
]
