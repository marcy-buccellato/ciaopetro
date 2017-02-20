from django.conf import settings
from django.conf.urls import url
from django.views.generic import DetailView

from tagging.views import TaggedObjectList

from blog import feed, models, views

urlpatterns = [
    # RSS Feed of latests posts
    url(r'^feed/$', feed.LatestPosts(), name="feed"),

    # Index: List all posts
    url(r'^$', views.PostListView.as_view(), name="index"),

    # Tag posts: List all posts for a given tag
    url(r'^tags/(?P<tag>[^/]+(?u))/$',
        TaggedObjectList.as_view(model=models.Post,
                                 paginate_by=settings.PAGE_SIZE,
                                 allow_empty=True),
        name='tag_index'),

    # Post detail: View post detail by a given slug
    url(r'^post/(?P<slug>\S+)$',
        DetailView.as_view(model=models.Post), name="post_detail"),

    # Media: path to uploaded media objects, such as photos
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),

    # If no other urls are caught, assume it's a category: site/<category>
    url(r'^(?P<category>[a-z\-]+)/$',
        views.CategoryPostListView.as_view(allow_empty=True),
        name='category_index'),
]
