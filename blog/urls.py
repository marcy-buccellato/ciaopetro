from django.conf import settings
from django.conf.urls import url
from django.views.generic import ListView, DetailView

from tagging.views import TaggedObjectList

from blog import feed, models

urlpatterns = [
    url(r'^feed/$', feed.LatestPosts(), name="feed"),
    url(r'^$',
        ListView.as_view(
            model=models.Post, paginate_by=settings.PAGE_SIZE,
            allow_empty=True),
        name="index"),
    url(r'^tags/(?P<tag>[^/]+(?u))/$',
        TaggedObjectList.as_view(
            model=models.Post, paginate_by=settings.PAGE_SIZE,
            allow_empty=True),
        name='tag_index'),
    url(r'^post/(?P<slug>\S+)$',
        DetailView.as_view(model=models.Post), name="post_detail"),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
]
