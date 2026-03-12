from .models import Order, OrderItem
from .serializers import OrderSerializer, OrderItemSerializer
from rest_framework import viewsets
from .permissions import IsAuthenticatedOrReadOnlyForOrder
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = [  IsAuthenticatedOrReadOnlyForOrder and  IsAuthenticatedOrReadOnly ]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderItemViewSet(viewsets.ModelViewSet):
    permission_classes = [ IsAuthenticatedOrReadOnlyForOrder and IsAuthenticatedOrReadOnly]
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)