from django.urls import path
from .views import TaomlarViewSet, CategoryViewSet
from rest_framework.routers import SimpleRouter

urlpatterns = [

]

router = SimpleRouter()
router.register(r"taomlar", TaomlarViewSet, basename="taomlar")
router.register(r"category", CategoryViewSet, basename="category")
urlpatterns += router.urls


