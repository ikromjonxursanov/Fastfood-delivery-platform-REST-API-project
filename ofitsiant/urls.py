from django.urls import path
from .views import TaomlarViewSet, CategoryViewSet
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(),      name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

router = SimpleRouter()
router.register(r"taomlar", TaomlarViewSet, basename="taomlar")
router.register(r"category", CategoryViewSet, basename="category")
urlpatterns += router.urls


