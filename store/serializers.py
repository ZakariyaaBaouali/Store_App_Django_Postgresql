from rest_framework import serializers
from models import Product, User, Collection, Order, Review, OrderItems, Discount, OrderDiscount, Wishlist


class ProductSerializer(serializers.Serializer):
    class Meta:
        model = Product
        fields = '__all__'


class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ['user_name', 'user_email', 'user_profile_url', 'created_at', 'updated_at']


class CollectionSerializer(serializers.Serializer):
    class Meta:
        model = Collection
        fields = '__all__'


class OrderSerializer(serializers.Serializer):
    class Meta:
        model = Order
        fields = '__all__'


class ReviewSerializer(serializers.Serializer):
    class Meta:
        model = Review
        fields = '__all__'


class OrderItemsSerializer(serializers.Serializer):
    class Meta:
        model = OrderItems
        fields = '__all__'


class DiscountSerialize(serializers.Serializer):
    class Meta:
        model = Discount
        fields = '__all__'


class OrderDiscountSerializer(serializers.Serializer):
    class Meta:
        model = OrderDiscount
        fields = '__all__'


class WishlistSerializer(serializers.Serializer):
    class Meta:
        model = Wishlist
        fields = '__all__'
