from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone

from tagging.fields import TagField


class PostQuerySet(models.QuerySet):
    def published(self):
        return self.filter(published_date__isnull=False)


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    text = models.TextField()
    short_description = models.TextField(blank=True, null=True)
    featured_image = models.ImageField(
        upload_to='photos/%Y/%m/%d', blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    tags = TagField()

    objects = PostQuerySet().as_manager()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"
        ordering = ["-published_date"]
