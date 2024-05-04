"""
This module is about books\'s urls
"""
from django.urls import path

from books.views import BookListView

urlpatterns = [
    path('',BookListView.as_view(), name="home")
]