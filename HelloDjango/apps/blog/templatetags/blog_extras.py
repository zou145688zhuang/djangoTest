from django import template
from blog.models import Post,Category,Tag
from django.db.models.aggregates import Count

register = template.Library()

@register.inclusion_tag('blog/inclusions/_recent_posts.html',takes_context=True)
def show_recent_posts(context,num=5):
    post_list = Post.objects.all()[:num]
    return {
        'recent_post_list':post_list
    }

def show_archives(context):
    return {
        'post_list':Post.objects.dates('create_time','month',order='DESC')
    }
@register.inclusion_tag('blog/inclusions/_tag.html',takes_context=True)
def show_tag_list(context):
    tag_list = Tag.objects.annotate(num_tags = Count('post')).filter(num_tags__gt=0)
    return {
        'tag_cloud_list':tag_list
    }

@register.inclusion_tag('blog/inclusions/_category.html',takes_context=True)
def show_category_list(context):
    category_list = Category.objects.annotate(num_categorys = Count('post')).filter(num_categorys__gt=0)
    return {
        'category_list':category_list
    }