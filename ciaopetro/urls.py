from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.flatpages.sitemaps import FlatPageSitemap
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap

from django_markdown import urls as markdown_urls

from blog import urls as blog_urls
from blog.models import Post


info_dict = {
    'queryset': Post.objects.all(),
    'date_field': 'published_date',
}

sitemaps = {
    'blog': GenericSitemap(info_dict, priority=0.6),
    'flatpages': FlatPageSitemap
}

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include(blog_urls)),
    url(r'^comments/', include('django_comments.urls')),
    url(r'^markdown/', include(markdown_urls)),
    url(r'^photologue/', include('photologue.urls', namespace='photologue')),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'),
]
