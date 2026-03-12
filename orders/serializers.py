from rest_framework.serializers import ModelSerializer
from .models import Order, OrderItem
from django.contrib.auth.models import User

# from apps.ofitsiant.serializers import MyTokenObtainPairSerializer

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]

class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"

class OrderItemSerializer(ModelSerializer):
    class Meta:
        model = OrderItem
        fields = "__all__"
