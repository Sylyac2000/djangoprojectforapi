"""
This module is about post serialization
"""
from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    # queryset = Post.objects.all()
    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'body', 'created_at']