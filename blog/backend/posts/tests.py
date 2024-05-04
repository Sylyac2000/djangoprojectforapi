"""
this module is about blog tests
"""
from django.contrib.auth.models import User
from django.test import TestCase
# from .models import Post

# Create your tests here.
from .models import Post


class BlogTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(username="balou", password="louba")
        user.save()

        #create a post
        post = Post.objects.create(
            author = user,
            title = "peux tu parler de programmation?",
            body = "Bien sûr ! La programmation est un domaine fascinant qui consiste à écrire des instructions pour ordonner à un ordinateur d'effectuer des tâches spécifiques. Voici quelques points clés à connaître sur la programmation ",
        )
        post.save()

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        print(post)
        self.assertEqual(post.title, "peux tu parler de programmation?")
        self.assertEqual(post.body, "Bien sûr ! La programmation est un domaine fascinant qui consiste à écrire des instructions pour ordonner à un ordinateur d'effectuer des tâches spécifiques. Voici quelques points clés à connaître sur la programmation ")