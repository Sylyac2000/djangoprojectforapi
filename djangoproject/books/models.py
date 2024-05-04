"""
This module is about books models
"""
from django.db import models


class Book(models.Model):
    """Book model"""
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=250)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13)

    class Meta:
        verbose_name_plural = 'Livres'

    def __str__(self):
        return self.title
