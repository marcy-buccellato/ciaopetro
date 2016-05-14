from django.contrib import admin
from blog import models
from django_markdown.admin import MarkdownModelAdmin
from django_markdown.widgets import AdminMarkdownWidget
from django.db.models import TextField


class PostAdmin(MarkdownModelAdmin):
    list_display = ("title", "created_date")
    prepopulated_fields = {"slug": ("title",)}
    # Next line is a workaround for Python 2.x
    formfield_overrides = {TextField: {'widget': AdminMarkdownWidget}}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "slug")
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Category, CategoryAdmin)

