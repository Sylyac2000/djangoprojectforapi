"""
this module is about views
"""
from django.shortcuts import render

# Create your views here.
from rest_framework import permissions
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)


from .serializers import PostSerializer
from .models import Post
from .permissions import IsAuthorOrReadOnly


class PostList(ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,) # view level permissions
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(RetrieveUpdateDestroyAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = [IsAuthorOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
