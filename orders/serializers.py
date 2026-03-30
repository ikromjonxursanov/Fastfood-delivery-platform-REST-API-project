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
        fields = ["id", "user", "delivery_address", "phone_number", "estimated_delivery_time", "total_price", "created_at"]
        read_only_field = ["estimated_delivery_time", "total_price", "created_at"]

class OrderItemSerializer(ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ["user", "order", "taom", "quantity", "unit_price", "subtotal", ]
        read_only_fields = ["unit_price", "subtotal",]

