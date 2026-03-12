from django.urls import path
from .views import PostViewSet
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh")

]

router = SimpleRouter()
router.register(r"user", PostViewSet, basename="user")
urlpatterns += router.urls