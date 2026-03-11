from rest_framework.serializers import ModelSerializer
from .models import Taomlar
from .models import Category
# from django.contrib.auth.models import User
#
# class UserSerializer(ModelSerializer):
#     class Meta:
#         model = User
#         fields = "__all__"

class TaomlarSerializer(ModelSerializer):
    class Meta:
        model =Taomlar
        fields = "__all__"

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"



