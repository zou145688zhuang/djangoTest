import xadmin
from comments.models import Comment

class CommentXadmin(object):
    list_display = ('name','email','url','post','create_time')
    fields = ('name','email','url','text','post')

xadmin.site.register(Comment,CommentXadmin)