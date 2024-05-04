"""
This module is about books admin
"""
from django.contrib import admin

from books.models import Book

admin.site.register(Book)
