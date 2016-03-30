from django.utils import timezone

from django.test import TestCase
from django.contrib.auth import get_user_model
from blog.models import Post


class BlogPostTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(username="testuser")

    def test_create_unpublished(self):
        entry = Post(title="Title Me", text=" ", author_id=self.user.id)
        entry.save()
        self.assertEqual(Post.objects.all().count(), 1)
        self.assertEqual(Post.objects.published().count(), 0)
        entry.published_date = timezone.now()
        entry.save()
        self.assertEqual(Post.objects.published().count(), 1)


class BlogViewTests(TestCase):
    def test_feed_url(self):
        response = self.client.get('/feed/')
        self.assertIn("xml", response['Content-Type'])
