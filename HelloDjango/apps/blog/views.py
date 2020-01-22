from django.shortcuts import render, get_object_or_404,HttpResponse
import markdown
from blog.models import Post, Tag, Category
from django.core.files.base import ContentFile
# Create your views here.

def index(request):
    post_list = Post.objects.all()
    return render(request, 'blog/index.html', context={
        'post_list':post_list
    })

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.increase_views()
    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    ])
    post.body = md.convert(post.body)
    post.toc = md.toc
    return render(request, 'blog/single.html', {
        'post':post
    })

def CloudTag(request, pk):
    t = get_object_or_404(Tag, pk=pk)
    post_list = Post.objects.filter(tags=t)
    return render(request, 'blog/index.html', context={
        'post_list':post_list
    })

def CategoryInfo(request, pk):
    c = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=c)
    return render(request, 'blog/index.html', context={
        'post_list': post_list
    })


def upload_image(request):
    image = request.FILES.get('editormd-image-file',None)
    if image:
        wiki_content_image = Post(
            image=image
        )
        wiki_content_image.save()
        image_url = wiki_content_image.image.url
        res = {
            'success':'1',
            'message':'上传成功',
            'image_url':image_url
        }
        return HttpResponse(res)
    else:
        res = {
            'success': 0,
            'message': '图片上传失败',

        }
        return HttpResponse(res)

