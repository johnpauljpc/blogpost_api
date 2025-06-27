from django.shortcuts import render
from rest_framework import serializers, response
from rest_framework.generics import (ListAPIView, ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.decorators import api_view
from rest_framework import exceptions
from django.contrib.auth import get_user_model

from .models import Post
from .serializers import (PostSerializer,
                           CreatePostSerializer, AuthorSerializer)
from .permissions import IsAuthorOrReadOnly

User = get_user_model()

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

class Authors(ListAPIView):
    authors_id = Post.objects.values_list('author').distinct()
    queryset = User.objects.filter(id__in = authors_id)
    serializer_class = AuthorSerializer



