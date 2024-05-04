"""
This module is about post serialization
"""
from rest_framework import serializers
from .models import Post

from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    #queryset = get_user_model().objects.all()

    class Meta:
        model = get_user_model()
        fields = ["id", "username", "email", "first_name"]

class PostSerializer(serializers.ModelSerializer):
    # queryset = Post.objects.all()
    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'body', 'created_at']