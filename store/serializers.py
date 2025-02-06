from rest_framework import serializers
from .models import Product, User, Collection, Order, Review, OrderItems, Discount, OrderDiscount, Wishlist


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'user_name', 'user_email', 'user_profile_url', 'created_at', 'updated_at']


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class OrderItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItems
        fields = '__all__'


class DiscountSerialize(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = '__all__'


class OrderDiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDiscount
        fields = '__all__'


class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = '__all__'
