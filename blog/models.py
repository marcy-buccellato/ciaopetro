from smartfields import fields
from smartfields.dependencies import FileDependency
from smartfields.processors import ImageProcessor

from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone

from tagging.fields import TagField
from photologue.models import Gallery


class CategoryManager(models.Manager):
    def posted(self):
        return self.filter(post__category__isnull=False).distinct()


class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(primary_key=True, max_length=200, unique=True)

    objects = CategoryManager()

    class Meta:
        ordering = ["title"]
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.title


class PostQuerySet(models.QuerySet):
    def published(self):
        return self.filter(published_date__isnull=False)


class Post(models.Model):
    author = models.ForeignKey("auth.User")
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    text = models.TextField()
    short_description = models.TextField(blank=True, null=True)
    featured_image = fields.ImageField(
        dependencies=[
            FileDependency(processor=ImageProcessor(
                format='JPEG', scale={'max_width': 1000, 'max_height': 1000}))
        ],
        upload_to="photos/%Y/%m/%d")
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    tags = TagField()
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, null=True,
                                blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 blank=False, default="life")

    objects = PostQuerySet().as_manager()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"
        ordering = ["-published_date"]
