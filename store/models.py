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


class Review(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE , related_name="user_reviews")
    product = models.ForeignKey(Product , on_delete=models.CASCADE , related_name="product_reviews")
    review_rating = models.SmallIntegerField(default=0)
    review_comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class Order(models.Model):
    ORDER_STATUS_PENDING = 'P'
    ORDER_STATUS_COMPLETE = 'C'
    ORDER_STATUS_FAILED = 'F'

    ORDER_STATUS = [
        (ORDER_STATUS_PENDING , 'pending'),
        (ORDER_STATUS_COMPLETE , 'complete'),
        (ORDER_STATUS_FAILED , 'failed')
    ]

    user = models.ForeignKey(User , on_delete=models.SET_NULL , related_name="user_orders")
    order_total_amount = models.DecimalField(max_digits=6 , decimal_places=2)
    order_status = models.CharField(max_length=1 , choices=ORDER_STATUS , default=ORDER_STATUS_PENDING)
    created_at = models.DateTimeField(auto_now_add=True)



class OrderItems(models.Model):
    order = models.ForeignKey(Order , on_delete=models.PROTECT , related_name="order_items")
    product = models.ForeignKey(Product , on_delete=models.SET_NULL)
    order_item_quantity = models.SmallIntegerField()
    order_item_price = models.DecimalField(max_digits=6 , decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)


class Wishlist(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE , primary_key=True)
    product = models.OneToOneField(Product , on_delete=models.CASCADE , primary_key=True)
    product_quantity = models.DecimalField(max_digits=6 , decimal_places=2)
    added_at = models.DateTimeField(auto_now_add=True)


