from django.shortcuts import render

from rest_framework import generics
from .models import Todo
from .serializers import TodoSerializer


class TodoListAPIView(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoRetriveAPIView(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer