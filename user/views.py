from .models import Post
from .serializers import PostSerializer
from rest_framework import viewsets
from .permissions import IsAuthenticatedOrReadOnlyForOrder


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnlyForOrder]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
