"""
This is about api endpoints
"""
from django.shortcuts import render
from rest_framework import generics
from books.models import Book
from .serializers import BookSerializer


class BookListAPIView(generics.ListAPIView):
    "list the books"
    serializer_class = BookSerializer
    queryset = Book.objects.all()
