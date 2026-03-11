from django.urls import path
from .views import  OrderViewSet, OrderItemViewSet
from rest_framework.routers import SimpleRouter

urlpatterns = [

]

router = SimpleRouter()
router.register(r"order", OrderViewSet, basename="order")
router.register(r"orderitem", OrderItemViewSet, basename="orderitem")
urlpatterns += router.urls