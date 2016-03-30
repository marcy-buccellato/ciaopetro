from django.contrib.syndication.views import Feed
from django.contrib.sites.models import Site

from blog.models import Post


class LatestPosts(Feed):
    title = "{} Blog".format(Site.objects.get_current().name)
    link = "/feed/"
    description = "Latest Posts of {}".format(Site.objects.get_current().name)

    def items(self):
        return Post.objects.published()[:100]
