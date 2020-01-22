import xadmin
from blog.models import Post,Category,Tag

class CategoryXadmin(object):
    pass


class TagXadmin(object):
    pass

class PostXadmin(object):
    list_display = ('title','excerpt','author','create_time','category','tags')
    search_fields = ('title','author')

xadmin.site.register(Tag,TagXadmin)
xadmin.site.register(Category,CategoryXadmin)
xadmin.site.register(Post,PostXadmin)