from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import (
    Category,
    Post,
    Comment,
    Like,
    PostNowView
)
from .serializers import (
    CategorySerializer,
    PostSerializer,
    PostNowViewSerializer,
    CommentSerializer,
    LikeSerializer
)


class CategoryView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class PostView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def post_image(self, request, *args, **kwargs):
        image = request.data['image']
        Post.objects.create(image=image)
        return HttpResponse({'message': 'Post Created'}, status=200)


class CommentView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class LikeView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostDetView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = PostNowView.objects.all()
    serializer_class = PostNowViewSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
