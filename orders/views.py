from .models import Order, OrderItem
from .serializers import OrderSerializer, OrderItemSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.exceptions import  PermissionDenied

class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = [  IsAuthenticatedOrReadOnly ]
    serializer_class = OrderSerializer

    def get_queryset(self):
        user = self.request.user

        if user.is_staff:
            return Order.objects.all()

        return Order.objects.filter(user=user)

class OrderItemViewSet(viewsets.ModelViewSet):
    permission_classes = [ IsAuthenticatedOrReadOnly]
    serializer_class = OrderItemSerializer

    def get_queryset(self):
        user = self.request.user

        if user.is_staff:
            return OrderItem.objects.all()

        return OrderItem.objects.filter(user=user)

    def perform_create(self, serializer):
        order = serializer.validated_data.get("order")
        if order.user != self.request.user and not self.request.user.is_staff:
            raise PermissionDenied("Bu order sizga tegishlimas")
        serializer.save()