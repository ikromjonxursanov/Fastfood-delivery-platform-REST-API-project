from rest_framework.serializers import ModelSerializer
from .models import Taomlar
from .models import Category

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):

        token = super().get_token(user)

        token ["username"] = user.username
        token ["email"] = user.email

        return token

class TaomlarSerializer(ModelSerializer):
    class Meta:
        model =Taomlar
        fields = "__all__"

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"



