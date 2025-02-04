from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=255)
    user_email = models.EmailField(max_length=50 , unique=True)
    user_profile_url = models.TextField()
    user_hash_password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Collection(models.Model):
    collection_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Product(models.Model):
    product_name = models.CharField(max_length=255)
    product_description = models.TextField()
    product_price = models.DecimalField(max_digits=6 , decimal_places=2)
    product_stock_quantity = models.SmallIntegerField(default=0)
    product_category = models.ForeignKey(Collection , on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

