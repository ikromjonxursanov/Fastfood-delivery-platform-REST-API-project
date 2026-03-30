from django.urls import path
from .views import ProfileView, RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView,


urlpatterns = [
    path('register/', RegisterView.as_view()),
    path("user/", ProfileView.as_view(), name="profil"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh")

]

