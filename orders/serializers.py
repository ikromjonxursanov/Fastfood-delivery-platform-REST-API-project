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
        fields = [
            "id",
            "user",
            "delivery_address",
            "phone_number",
            "estimated_delivery_time",
            "total_price",
            "created_at"
        ]
        read_only_fields = ["user", "estimated_delivery_time", "total_price", "created_at"]

    def create(self, validated_data):
        validated_data["user"] = self.context["request"].user
        return super().create(validated_data)


class OrderItemSerializer(ModelSerializer):
    class Meta:
        model = OrderItem
        fields = [
            "id",
            "order",
            "taom",
            "quantity",
            "unit_price",
            "subtotal",
        ]
        read_only_fields = ["unit_price", "subtotal"]
