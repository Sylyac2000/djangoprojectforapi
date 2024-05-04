"""
This modules is about books views
"""
from django.views.generic import ListView

from books.models import Book


class BookListView(ListView):
    model = Book
    template_name = 'books/book-list.html'
    context_object_name ='livres'
