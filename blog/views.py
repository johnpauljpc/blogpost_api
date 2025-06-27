from django.shortcuts import render
from rest_framework import serializers
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework import exceptions
from .models import Post
from .serializers import PostSerializer, CreatePostSerializer
from .permissions import IsAuthorOrReadOnly
# Create your views here.
class ListCreatePost(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreatePostSerializer
        return PostSerializer
    def perform_create(self, serializer):
        if not self.request.user.is_authenticated:
            raise serializers.ValidationError("To create post please login")
        serializer.save(author = self.request.user)

class RetrievePost(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly]

