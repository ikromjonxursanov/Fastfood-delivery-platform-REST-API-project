from django.urls import path
from .views import PostViewSet
from rest_framework.routers import SimpleRouter

urlpatterns = [

]

router = SimpleRouter()
router.register(r"post", PostViewSet, basename="post")
urlpatterns += router.urls