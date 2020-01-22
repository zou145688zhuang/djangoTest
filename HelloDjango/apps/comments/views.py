from django.shortcuts import render,get_object_or_404,redirect
from comments.models import Comment
from blog.models import Post
from comments.forms import CommentForm
from django.contrib import messages
from django.views.decorators.http import require_POST

# Create your views here.
def comment(request,post_pk):
    post = get_object_or_404(Post,pk = post_pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        messages.add_message(request,messages.SUCCESS,'评论成功',extra_tags='success')
        messages.add_message(request,messages.ERROR,'评论失败',extra_tags='error')
        return redirect(post)
    return render(request,'comment/preview.html',{
        'post':post,
        'form':form
    })
