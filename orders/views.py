from .models import Order, OrderItem
from .serializers import OrderSerializer, OrderItemSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly


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

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        user = self.request.user

        if user.is_staff:
            return Order.objects.all()

        return Order.objects.filter(user=user)