"""
this module is about models of todos app
"""
from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self):
        return self.title