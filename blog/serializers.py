from  rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Post

User = get_user_model()

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class CreatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'content', 'publish']

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['full_name', 'email']