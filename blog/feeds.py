from django.contrib.syndication.views import Feed
from blog.models import Post

class LatestPostsFeed(Feed):
    title = "My Blog"
    link = "/rss/"
    description = "Updates on new posts."

    def items(self):
        return Post.objects.filter(status=True).order_by('-created_date')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content
