import os
import random

from django import template
from django.conf import settings

from blog.models import Category, CategoryQuerySet

register = template.Library()


@register.filter(name='get_header_image')
def get_header_image(unused):
    """
    Gets random image from header images directory.

    Hack Alert: Template tags are designed to modify an input, but since this
    is a static function, the argument is just "unused" because template tags
    expect an argument.
    :return:
    """
    return random.choice(os.listdir(settings.STATIC_ROOT + "/images/header"))


@register.simple_tag(name='get_posted_categories')
def get_posted_categories(limit=0):
    """
    Gets list of categories.

    :param limit int - limit number of categories to return:
    :return:
    """
    categories = Category.objects.all()

    # Apply limit if provided
    if limit and isinstance(limit, int):
        categories = categories[0:limit]
    categories_posted = CategoryQuerySet.posted(categories)

    return categories_posted
