"""
this module is about views
"""
from django.contrib.auth import get_user_model
from django.shortcuts import render

# Create your views here.
from rest_framework import permissions, viewsets
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)


from .serializers import PostSerializer, UserSerializer
from .models import Post
from .permissions import IsAuthorOrReadOnly, IsUserOrReadOnly


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated, IsUserOrReadOnly,)
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class PostList(ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,) # view level permissions
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(RetrieveUpdateDestroyAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = [IsAuthorOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
