from django.test import TestCase
from .models import Todo

# Create your tests here.
"""
a test database is created when testing
"""

class TodoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        #Todo.objects.create(title="What's a package in python?", body = "What's a package in python way?")
        todo = Todo()
        todo.title = "What's a package in python?"
        todo.body = "What's a package in python way?"
        todo.save()

    def test_title(self):
        todo = Todo.objects.get(id=1)
        self.assertEqual(todo.title, "What's a package in python?")

    def test_body(self):
        todo = Todo.objects.get(id=1)
        expected_body = f'{todo.body}'
        self.assertEqual(expected_body, "What's a package in python way?")
