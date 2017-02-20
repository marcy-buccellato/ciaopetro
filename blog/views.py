"""
Blog related views.
"""
from django.http import Http404
from django.views.generic.list import ListView
from django.conf import settings

from blog.models import Post


class PostListView(ListView):
    """
    A thin wrapper around the generic list view to filter on published posts.
    """
    model = Post
    allow_empty = False
    paginate_by = settings.PAGE_SIZE

    def get_queryset(self):
        return self.model.objects.published()


class CategoryPostListView(PostListView):
    """
    A thin wrapper around the Post list view to filter on a given category.
    """
    category = None

    def get_queryset(self, **kwargs):
        queryset = super(CategoryPostListView, self).get_queryset()
        if not self.kwargs.get('category'):
            raise Http404('No category provided.')
        
        posts = queryset.filter(category__slug=self.kwargs['category'])
        
        if not posts:
            raise Http404('No posts found with that category.')
        
        return posts
