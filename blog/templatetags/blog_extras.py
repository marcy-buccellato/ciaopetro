import os
import random

from django import template
from django.conf import settings

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
