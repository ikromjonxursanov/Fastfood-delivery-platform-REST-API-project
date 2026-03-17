from rest_framework.serializers import ModelSerializer
from .models import Order, OrderItem
from django.contrib.auth.models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ["user", "delivery_address", "created_at"]

class OrderItemSerializer(ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ["order", "taom"]
