"""
Blog related views.
"""
from django.http import Http404
from django.views.generic.list import ListView

from blog.models import Post


class CategoryListView(ListView):
    """
    A thin wrapper around
    ``django.views.generic.list.ListView`` which creates a
    ``QuerySet`` containing instances of the given queryset or model
    categoryged with the given category.

    In addition to the context variables set up by ``object_list``, a
    ``category`` context variable will contain the ``Category`` instance for the
    category.
    """
    category = None

    paginate_by = 10

    def get_queryset(self, **kwargs):
        if not self.kwargs.get('category'):
            raise Http404('No category provided.')
        
        posts = Post.objects.published().filter(category__slug=self.kwargs['category'])
        
        if not posts:
            raise Http404('No posts found with that category.')
        
        return posts
