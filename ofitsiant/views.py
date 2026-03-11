from .models import Category, Taomlar
from .serializers import TaomlarSerializer, CategorySerializer
from rest_framework import viewsets

class TaomlarViewSet(viewsets.ModelViewSet):
    queryset = Taomlar.objects.all()
    serializer_class = TaomlarSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



