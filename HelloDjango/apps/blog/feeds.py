from django.contrib.syndication.views import Feed
from blog.models import Post

class AllPostRssFeed(Feed):
    title = 'Django博客项目'
    link = '/'
    description = '测试文章'

    def items(self):
        return Post.objects.all()

    def item_title(self, item):
        return '[%s] %s' % (item.category,item.title)

    def item_description(self, item):
        return item.body