from django.db import models
# from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.html import strip_tags
from django.urls import reverse
import markdown
from ckeditor.fields import RichTextField
# Create your models here.


class Category(models.Model):
    '''ddd'''
    name = models.CharField(max_length=100, verbose_name='分类名称')

    def __str__(self):
        return self.name

    class Meta:
        '''meta'''
        verbose_name = '分类'
        verbose_name_plural = verbose_name
# ddd
class Tag(models.Model):
    '''tag'''
    name = models.CharField(max_length=50, verbose_name='标签名称')

    def __str__(self):
        return self.name

    class Meta:
        '''ddd'''
        verbose_name = '标签'
        verbose_name_plural = verbose_name

class Post(models.Model):
    '''post'''
    title = models.CharField(max_length=70, verbose_name='标题')
    body = RichTextField(verbose_name='内容')
    excerpt = models.CharField(max_length=200, verbose_name='摘要',blank=True)
    create_time = models.DateTimeField(verbose_name='创建时间', default=timezone.now())
    modify_time = models.DateTimeField(verbose_name='修改时间', default=timezone.now())
    author = models.ForeignKey('users.User', verbose_name='作者', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name='分类', on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, verbose_name='标签', blank=True)
    views = models.PositiveIntegerField(default=0, verbose_name='阅读量')
    image = models.ImageField(upload_to='upload/editor/',blank=True,verbose_name='封面图片')

    def __str__(self):
        return self.title

    class Meta:
        '''meta'''
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ['-create_time']

    def get_absolute_url(self):
        '''url'''
        return reverse('blog:detail', kwargs={'pk':self.pk})

    def save(self, *args, **kwargs):
        '''save'''
        self.modify_time = timezone.now()
        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite'
        ])
        self.excerpt = strip_tags(md.convert(self.body))[:200]
        super().save(*args, **kwargs)

    def increase_views(self):
        '''views'''
        self.views += 1
        self.save(update_fields=['views'])