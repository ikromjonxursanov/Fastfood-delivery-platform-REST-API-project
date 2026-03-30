from .models import Category, Taomlar
from .serializers import TaomlarSerializer, CategorySerializer
from rest_framework import viewsets
from .permissions import IsStaffOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class TaomlarViewSet(viewsets.ModelViewSet):
    permission_classes = [IsStaffOrReadOnly,  IsAuthenticatedOrReadOnly]
    queryset = Taomlar.objects.all()
    serializer_class = TaomlarSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes =[IsStaffOrReadOnly, IsAuthenticatedOrReadOnly]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



